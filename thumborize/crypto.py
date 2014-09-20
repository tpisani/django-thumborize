from libthumbor import CryptoURL

from thumborize import conf

crypto = CryptoURL(key=conf.THUMBOR_SECURITY_KEY)


def url(image_url, **kwargs):
    encrypted = crypto.generate(image_url=image_url, **kwargs)
    return conf.THUMBOR_SERVER + encrypted
