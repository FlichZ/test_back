from django import template
from menu_app.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).prefetch_related('children')

    def render_menu_items(items):
        menu_html = ''
        for item in items:
            menu_html += f'<li><a href="{item.url}">{item.title}</a>'
            children = item.children.all()
            if children:
                menu_html += '<ul>'
                menu_html += render_menu_items(children)
                menu_html += '</ul>'
            menu_html += '</li>'
        return menu_html

    menu_html = f'<ul class="menu">{render_menu_items(menu_items)}</ul>'
    return menu_html