from django.contrib import admin

import log.models

admin.site.register(log.models.Person)
admin.site.register(log.models.Type)
admin.site.register(log.models.Group)


# class TPerson(log.models.Person):
#     class Meta:
#         proxy = True


class ParameterInlines(admin.TabularInline):
    model = log.models.Parameter
    readonly_fields = ['created_at', 'updated_at']
    extra = 1


class NoteInlines(admin.TabularInline):
    model = log.models.Note
    readonly_fields = ['created_at', 'updated_at']
    extra = 0


@admin.register(log.models.Event)
class TemperatureGroupAdmin(admin.ModelAdmin):
    inlines = [ParameterInlines, ]
    readonly_fields = ['created_at', 'updated_at']
