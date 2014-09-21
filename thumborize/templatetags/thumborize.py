from django.template import Library

# Workaround to allow users to import thumborize
# and load it's templatetags just about the same way.
from .. import url

register = Library()


@register.simple_tag(name="thumborize")
def do_thumborize(image_url, **kwargs):
    return url(image_url, **kwargs)
