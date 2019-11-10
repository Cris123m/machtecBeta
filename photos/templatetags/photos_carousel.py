from django import template
from photos.models import Photo

register=template.Library()

@register.simple_tag

def get_photo_list():
    photos=Photo.objects.all()
    return photos