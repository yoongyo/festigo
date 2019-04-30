from django import template
import re

register = template.Library()


@register.filter
def add_link(value):
    hash_tag = value.tag
    tags = value.tag_set.all()
    for tag in tags:
        hash_tag = re.sub(r'\#'+tag.name+r'\b', '<a href="/festival/explore/tags/'+tag.name+'">#'+tag.name+'</a>', hash_tag)
    return hash_tag