# Django Technology Radar

[![Build Status](https://travis-ci.org/moorinteractive/django-technology-radar.svg?branch=master)](https://travis-ci.org/moorinteractive/django-technology-radar) [![Coverage Status](https://coveralls.io/repos/github/moorinteractive/django-technology-radar/badge.svg?branch=master)](https://coveralls.io/github/moorinteractive/django-technology-radar?branch=master) [![Dependency Status](https://gemnasium.com/moorinteractive/django-technology-radar.svg)](https://gemnasium.com/moorinteractive/django-technology-radar) [![Documentation](https://readthedocs.org/projects/django-technology-radar/badge/?version=latest)](http://django-technology-radar.readthedocs.org/en/latest/?badge=latest)

A Django app for building your own Technology Radar, inspired by [ThoughtWorks](https://www.thoughtworks.com/).

## Documentation

See the [documentation](http://django-technology-radar.readthedocs.org/) for more information.

## Usage

Install the ``technology_radar`` package from GitHub:

    $ pip install django-technology-radar

This will also install it's dependencies.

### Settings

In your settings file, add the following apps to ``INSTALLED_APPS``:

    'rest_framework',
    'simple_history',
    'technology_radar',

Add the following entries to ``MIDDLEWARE_CLASSES``:

    'simple_history.middleware.HistoryRequestMiddleware',

Choose a renderer class (default ``PDFRenderer``):

    TECHNOLOGY_RADAR_RENDER_CLASS = 'technology_radar.renderers.PDFRenderer'

### URL Configuration

Add the following additions to your ``urls.py`` file:

    url(r'', include('technology_radar.urls')),
