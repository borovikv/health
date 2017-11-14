from django import template

register = template.Library()


@register.filter
def get(collection, type):
    return next((element.value for element in collection if element.type == type), '')