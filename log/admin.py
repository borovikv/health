from django.contrib import admin

import log.models


# class TPerson(log.models.Person):
#     class Meta:
#         proxy = True


class TemperatureInlines(admin.TabularInline):
    model = log.models.Temperature
    readonly_fields = ['created_at', 'updated_at']
    extra = 1


@admin.register(log.models.LogGroup)
class TemperatureGroupAdmin(admin.ModelAdmin):
    inlines = [TemperatureInlines, ]
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(log.models.Person)


class NosebleedConditionInlines(admin.TabularInline):
    model = log.models.NosebleedCondition
    readonly_fields = ['created_at', 'updated_at']
    extra = 1


@admin.register(log.models.Nosebleed)
class NosebleedAdmin(admin.ModelAdmin):
    inlines = [NosebleedConditionInlines, ]
    readonly_fields = ['created_at', 'updated_at']
