from django import template
from main.views import searchbar


register = template.Library()
 
from django import template
from django.utils.safestring import mark_safe
from markdown import markdown # type: ignore

register = template.Library()

@register.simple_tag(name='md_html')
def madrdown_to_html(text):
    html_content = markdown(text, extensions=['extra', 'fenced_code', 'tables'])

    return mark_safe(html_content)

@register.simple_tag(name='is_member')
def user_is_member(group, user):
    return group.members.filter(pk=user.pk).exists()

@register.simple_tag(name='searchbar')
def get_searchbar():
    lst = []
    for i in searchbar.keys():
        lst.append({'name': i, 'title': searchbar[i]['title']})
    return lst