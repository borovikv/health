from django.contrib import admin

import log.models

admin.site.register(log.models.Person)
admin.site.register(log.models.Type)
admin.site.register(log.models.Group)
admin.site.register(log.models.ParameterType)
admin.site.register(log.models.Parameter)
admin.site.register(log.models.Event)
admin.site.register(log.models.Note)


# class TPerson(log.models.Person):
#     class Meta:
#         proxy = True
