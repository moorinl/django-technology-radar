# Django Technology Radar

[![Build Status](https://travis-ci.org/moorinteractive/django-technology-radar.svg?branch=master)](https://travis-ci.org/moorinteractive/django-technology-radar)

A Django app for building your own Technology Radar, inspired by [ThoughtWorks](https://www.thoughtworks.com/).

## Usage

Install the ``technology_radar`` package from GitHub:

    pip install git+git://github.com/moorinteractive/django-technology-radar.git

This will also install it's dependencies.

### Settings

In your settings file, add the following apps to ``INSTALLED_APPS``:

    'rest_framework',
    'simple_history',
    'technology_radar',

Add the following entries to ``MIDDLEWARE_CLASSES``:

    'simple_history.middleware.HistoryRequestMiddleware',

### URL Configuration

Add the following additions to your ``urls.py`` file:

    url(r'', include('technology_radar.urls'))
