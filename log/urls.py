from django.conf.urls import url

import log.views as v

urlpatterns = [
    url(r'^$', v.SubjectListView.as_view(), name='subject-list'),
    url(r'create/(?P<subject_pk>\d+)/(?P<type_pk>\d+)$', v.CreateLog.as_view(), name='create-log'),
    url(r'update/(?P<pk>\d+)$', v.UpdateLog.as_view(), name='update-log'),
    url(r'types/(?P<subject_pk>\d+)$', v.TypeListView.as_view(), name='type-list'),
    url(r'events/(?P<subject_pk>\d+)/(?P<type_pk>\d+)$', v.EventListView.as_view(), name='event-list'),
]