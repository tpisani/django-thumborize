from libthumbor import CryptoURL

crypto = CryptoURL(key="MY_SECURE_KEY")


def url(image_url, **kwargs):
    return crypto.generate(image_url=image_url, **kwargs)
