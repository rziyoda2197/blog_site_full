from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter(name='reading_time')
def reading_time(text):
    """Calculate reading time in minutes."""
    word_count = len(text.split())
    minutes = max(1, word_count // 200)
    return f"{minutes} daqiqa"


@register.filter(name='truncate_words_html')
def truncate_words_html(value, length=30):
    """Truncate text preserving HTML."""
    words = value.split()
    if len(words) > length:
        return ' '.join(words[:length]) + '...'
    return value
