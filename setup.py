from setuptools import find_packages, setup


install_requires = [
    'django>=1.9,<1.10',
    'django-simple-history>=1.8,<1.9',
    'djangorestframework>=3.3,<3.4'
]

tests_require = [
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
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
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
