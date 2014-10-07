import re

from collections import Iterable

from libthumbor import CryptoURL

from thumborize import conf

crypto = CryptoURL(key=conf.THUMBOR_SECURITY_KEY)

filter_pattern = re.compile("(?P<name>\w+)(?P<param>\(.*\))")


class ThumborURL(object):
    """
    Manages arguments and options of thumbor URLs.
    """

    def __init__(self, image_url, reset_filters=False, **options):
        filters = options.pop("filters", {})
        self.image_url = image_url
        self.options = options
        self.filters = self._parse_filters(filters)
        if not reset_filters:
            self._merge_default_filters()

    def __unicode__(self):
        return self.generate()

    def __str__(self):
        return self.generate()

    def __repr__(self):
        return "<{classname}: {url}>".format(classname=self.__class__.__name__,
                                             url=self.generate())

    def _merge_default_filters(self):
        defaults = conf.THUMBOR_DEFAULT_FILTERS.copy()
        defaults.update(self.filters)
        self.filters = defaults

    def _filters_dict(self, filters):
        filters_dict = {}
        for item in filters:
            sre = filter_pattern.match(item)
            name, param = sre.groups()
            filters_dict[name] = param
        return filters_dict

    def _parse_filters(self, filters):
        if isinstance(filters, basestring):
            return self._filters_dict(filters.split(":"))
        elif isinstance(filters, Iterable):
            return self._filters_dict(filters)
        elif isinstance(filters, dict):
            return filters
        raise TypeError("Filters must be either a string, iterable or dict.")

    @property
    def filter_list(self):
        return ["{k}{v}".format(k=key, v=value) for key, value in self.filters.items()]

    def add_filters(self, *filters, **kwfilters):
        parsed = self._parse_filters(filters)
        self.filters.update(parsed)
        self.filters.update(kwfilters)

    def remove_filters(self, *filters):
        for key in filters:
            self.filters.pop(key, None)

    def generate(self):
        encrypted = crypto.generate(image_url=self.image_url,
                                    filters=self.filter_list,
                                    **self.options)
        return conf.THUMBOR_SERVER + encrypted


def url(image_url, **options):
    """
    Small shortcut for generating URLs by ThumborURL.
    """
    thumbor_url = ThumborURL(image_url, **options)
    return thumbor_url.generate()
