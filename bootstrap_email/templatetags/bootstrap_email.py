import pkg_resources
from django import template

register = template.Library()


@register.simple_tag
def bootstrap_email_min():
    css_file = pkg_resources.resource_string('bootstrap_email', 'static/bootstrap-email.min.css')
    return css_file


@register.simple_tag
def bootstrap_email():
    css_file = pkg_resources.resource_string('bootstrap_email', 'static/bootstrap-email.css')
    return css_file