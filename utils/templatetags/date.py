from django import template

import utils.datetime_utils as d

register = template.Library()


@register.filter
def is_today(date):
    return d.is_today(date)


@register.filter
def is_yesterday(date):
    return d.is_yesterday(date)
