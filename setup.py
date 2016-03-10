from setuptools import find_packages, setup


install_requires = [
    'django>=1.8,<1.10',
    'django-simple-history>=1.8,<1.9',
    'django-autoslug>=1.9,<2.0',
    'djangorestframework>=3.3,<3.4',
    'reportlab>=3.3,<3.4'
]

docs_require = [
    'sphinx'
]

test_require = [
    'flake8',
    'pytest',
    'pytest-cov',
    'pytest-django',
    'pytest-factoryboy',
    'tox'
]

setup(
    name='django-technology-radar',
    version='0.1.0',
    description='A Django app for building your own Technology Radar.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    url='https://github.com/moorinteractive/django-technology-radar',
    download_url='https://github.com/moorinteractive/django-technology-radar/tarball/0.1.0',
    install_requires=install_requires,
    extras_require={
        'docs': docs_require,
        'test': test_require
    },
    packages=find_packages(exclude=[
        '*tests',
        '*fixtures',
        'sandbox'
    ]),
    include_package_data=True,
    classifier=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
