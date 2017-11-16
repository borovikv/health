from django.conf.urls import url

import log.views as v

subject = r'subj/(?P<subject_pk>\d+)'
subject_type = fr'{subject}/types/(?P<type_pk>\d+)'
group = r'groups/(?P<group_pk>\d+)'

urlpatterns = [
    url(r'^$', v.SubjectListView.as_view(), name='subject-list'),

    url(fr'{subject_type}/groups/create$', v.CreateGroup.as_view(), name='create-group'),

    url(fr'{subject_type}/events/create$', v.CreateLog.as_view(), name='create-log'),
    url(fr'{subject_type}/{group}/events/create$', v.CreateLog.as_view(), name='create-log'),

    url(r'events/(?P<pk>\d+)/update$', v.UpdateLog.as_view(), name='update-log'),

    url(fr'{subject}/types$', v.TypeListView.as_view(), name='type-list'),

    url(fr'{subject_type}/events$', v.EventListView.as_view(), name='event-list'),
    url(fr'{subject_type}/{group}/events$', v.EventListView.as_view(), name='event-list'),
]
