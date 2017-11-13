import re
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.text import Truncator

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(force_text(value), extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'del_ins'], safe_mode=True, enable_attributes=False))

@register.filter(is_safe=True)
@stringfilter
def cut_summary(value):
    length = value.find(r'<p>[HTML_REMOVED]</p>', 0)
    return value[:length] if length > 0 else value

@register.filter(is_safe=True)
@stringfilter
def clear_more_mark(value):
    return re.sub(r'<p>\[HTML_REMOVED\]</p>', '', value)
