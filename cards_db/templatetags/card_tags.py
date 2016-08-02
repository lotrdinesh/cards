from django import template

register = template.Library()

@register.filter(name = 'get_image')
def get_image(value):

    name = value

    if name:
	return "images/"+name+".jpg"
    else:
	return "images/noimage.jpg"
