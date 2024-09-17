from django import template


register = template.Library()

@register.inclusion_tag('main/includes/list_posts')
def show_posts():
    pass

@register.simple_tag(name='prinfo')
def print_info(x):

    for i in x:
        print(i)