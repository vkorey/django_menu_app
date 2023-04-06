from django import template
from app.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name, parent=None):
    request = context['request']
    menu = Menu.objects.filter(menu_name=menu_name, parent=parent)

    for item in menu:
        item.is_active = is_menu_item_in_active_path(item, request)
        item.has_active_child = has_active_child(item, request)

    return {'menu': menu, 'parent': parent, 'request': request}


def is_menu_item_in_active_path(menu_item, request):
    if menu_item.get_url() == request.path:
        return True
    for child in menu_item.menu_set.all():
        if is_menu_item_in_active_path(child, request):
            return True
    return False


def has_active_child(menu_item, request):
    for child in menu_item.menu_set.all():
        if is_menu_item_in_active_path(child, request):
            return True
    return False
