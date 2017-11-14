import django.utils.timezone as tz
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.urls.base import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

import log.forms as f
import log.models as m


def parameters_formset(extra=0):
    return inlineformset_factory(m.Event, m.Parameter, fields=['type', 'value'], can_delete=False, extra=extra)


class CreateLog(CreateView):
    form_class = f.EventForm
    model = m.Event
    template_name = 'event/form.html'

    def get_success_url(self):
        return reverse('log:event-list',
                       kwargs={'subject_pk': self.kwargs['subject_pk'], 'type_pk': self.kwargs['type_pk']})

    def get_context_data(self, **kwargs):
        ctx = super(CreateLog, self).get_context_data(**kwargs)
        t: m.Type = m.Type.objects.get(pk=self.kwargs['type_pk'])
        subject: m.Person = m.Type.objects.get(pk=self.kwargs['subject_pk'])
        ctx['type'] = t
        if self.request.POST:
            ctx['form'] = f.EventForm(self.request.POST)
            ctx['inlines'] = parameters_formset()(self.request.POST)
        else:
            ctx['form'] = f.EventForm(initial={'type': t, 'subject': subject, 'event_time': tz.now()})
            initial = [{'type': p} for p in t.parameters.all()]
            ctx['inlines'] = parameters_formset(extra=len(initial))(initial=initial)
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()
            self.save_inlines()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def save_inlines(self):
        for f in parameters_formset()(self.request.POST, instance=self.object):
            if f.is_valid() and f.cleaned_data['value'] is not None:
                f.save()

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SubjectListView(ListView):
    model = m.Person
    context_object_name = 'subjects'
    template_name = 'subjects.html'


class TypeListView(ListView):
    model = m.Type
    context_object_name = 'types'
    template_name = 'types.html'

    def get_context_data(self, **kwargs):
        ctx = super(TypeListView, self).get_context_data(**kwargs)
        ctx['subject_pk'] = self.kwargs['subject_pk']
        return ctx


class EventListView(ListView):
    model = m.Event
    context_object_name = 'events'
    template_name = 'events.html'

    def get_queryset(self):
        return super(EventListView, self).get_queryset().filter(type=self.get_type(), subject=self.get_subject())

    def get_subject(self):
        return m.Person.objects.get(pk=self.kwargs['subject_pk'])

    def get_context_data(self, **kwargs):
        ctx = super(EventListView, self).get_context_data(**kwargs)
        ctx['parameters'] = self.get_parameters()
        ctx['type'] = self.get_type()
        ctx['subject'] = self.get_subject()
        return ctx

    def get_type(self):
        return m.Type.objects.get(pk=self.kwargs['type_pk'])

    def get_parameters(self):
        first = self.get_queryset().first()
        if first:
            return first.type.parameters.all()
        return []


class UpdateLog(UpdateView):
    form_class = f.EventForm
    model = m.Event
    template_name = 'event/form.html'

    def get_success_url(self):
        return reverse('log:event-list',
                       kwargs={'subject_pk': self.object.subject.pk, 'type_pk': self.object.type.pk})

    def get_context_data(self, **kwargs):
        ctx = super(UpdateView, self).get_context_data(**kwargs)
        event: m.Type = m.Event.objects.get(pk=self.kwargs['pk'])
        if self.request.POST:
            ctx['form'] = f.EventForm(self.request.POST)
            ctx['inlines'] = parameters_formset(self.request.POST)
        else:
            ctx['form'] = f.EventForm(instance=event)
            existed_params = [p.type for p in event.parameters.all()]
            initial = [{'type': p} for p in event.type.parameters.all() if p not in existed_params]
            ctx['inlines'] = parameters_formset(extra=len(initial))(instance=event, initial=initial)
        return ctx

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.save_inlines()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def save_inlines(self):
        for f in parameters_formset()(self.request.POST, instance=self.object):
            if f.is_valid() and f.cleaned_data['value'] is not None:
                f.save()

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
