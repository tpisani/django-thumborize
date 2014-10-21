=================
django-thumborize
=================

.. image:: https://api.travis-ci.org/tpisani/django-thumborize.svg

Minimal interface for `thumbor <http://thumbor.org/>`_ imaging service.


Features
========

Easy thumbor URLs
-----------------

Easily build thumbor URLs with arguments and filters by calling simple functions.


Default filters
---------------

Set default filters to be used on thumborized URLs.
These filters can be overridden by any calls that specify the same filters with different parameters.


Flexible filters specification
------------------------------

Filters can be either a string delimited by ``:``, a ``list`` or ``dict``. See usage for more.


Chaining
--------

Easy, queryset like chaining for applying filters and resizing.


*For a full list of available filters, check* `thumbor's wiki <https://github.com/thumbor/thumbor/wiki/Filters>`_.


Usage
=====

.. code:: python

    from thumborize import ThumborURL

    # Filters as string.
    thumbor_url = ThumborURL("http://path/to/image.png", width=320,
                             filters="quality(80):grayscale()")

    # Filters as list.
    thumbor_url = ThumborURL("http://path/to/image.png", width=320,
                             filters=["quality(80)", "grayscale()"])

    # Filters as dict.
    thumbor_url = ThumborURL("http://path/to/image.png", width=320,
                             filters={
                                 "quality": "(80)",
                                 "grayscale": "()",
                             })

    thumbor_url.generate()
    'http://localhost:8888/JiuVg9d5Mry_kw4odvb5Zh1C_BY=/320x0/filters:quality(80):grayscale()/http://path/to/image.png'


Chaining
--------

.. code:: python

    from thumborize import ThumborURL

    thumbor_url = ThumborURL("http://path/to/image.png")

    small_gray_image = thumbor_url.grayscale().resize(width=100, height=100)

    small_gray_image.generate()
    'http://localhost:8888/RFsfJakG9BsJUcbY2l1M6D5tthQ=/100x100/filters:grayscale()/http://path/to/image.png'

    low_quality_image = thumbor_url.quality(40).width(200)
    'http://localhost:8888/SB1ILIArmGzsd90-Mz-TxJVHwqI=/200x0/filters:quality(40)/http://path/to/image.png'

    # Original ThumborURL instance.
    thumbor_url.generate()
    'http://localhost:8888/O0Zqo6DMqqXHORdYncuspoaJlr0=/http://path/to/image.png'


Shortcut
--------

.. code:: python

    import thumborize

    thumborize.url("http://path/to/image.png", width=320, height=300)
    'http://localhost:8888/DYStA-Xwisc37dVz7bdXZ3u63QI=/320x300/http://path/to/image.png'


Templates
---------

.. code:: html

    {% load thumborize %}

    <!-- Filters as string -->
    <img src="{% thumborize some_url width=320 filters='quality(80):grayscale()' %}"/>

    <!-- Filters as a list object -->
    <img src="{% thumborize some_url width=320 filters=filter_list %}"/>


Installation
============

Install using **pip**:

::

    $ pip install django-thumborize


In order to use **django-thumborize** templatetags, you must add the app to ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = (
        # Other django apps..
        "thumborize", # Any order is fine.
    )


Configure basic thumbor settings:

.. code:: python

    # Thumbor host URL.
    THUMBOR_SERVER = "http://localhost:8888/"

    # This key must be the same used in thumbor
    # host to build safe URLs correctly.
    THUMBOR_SECURITY_KEY = "MY_SECURE_KEY"

    # Default filters are optional.
    THUMBOR_DEFAULT_FILTERS = {
        "quality": "(80)",
        "grayscale": "()",
    }


Testing
=======


Install
-------

First clone the repository, then run ``make install`` to install dev requirements.


Run tests
---------

Run ``make test`` to run tests.
