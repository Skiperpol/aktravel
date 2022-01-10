from django import template

register = template.Library()

@register.filter 
def get_item(Queryset, id):
    return Queryset[int(id)*3]

@register.filter 
def get_item2(Queryset, id):
    return Queryset[(int(id)*3)+1]

@register.filter 
def get_item3(Queryset, id):
    return Queryset[(int(id)*3)+2]
