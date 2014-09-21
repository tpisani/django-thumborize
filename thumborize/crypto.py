from libthumbor import CryptoURL

from thumborize import conf

crypto = CryptoURL(key=conf.THUMBOR_SECURITY_KEY)


def _parse_filters(filters):
    return filters.split(":")


def url(image_url, **kwargs):
    filters = kwargs.get("filters")
    if isinstance(filters, basestring):
        kwargs["filters"] = _parse_filters(filters)
    encrypted = crypto.generate(image_url=image_url, **kwargs)
    return conf.THUMBOR_SERVER + encrypted
