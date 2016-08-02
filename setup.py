import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='webpage_core',
    version='0.1',
    packages=['webpage_core'],
    install_requires = [
            'django-modeltranslation',
            'django-tinymce==2.0.6',
            'django-model-utils==2.4',
            #'Pillow==3.0.0',
        ],
    zip_safe = False,
    include_package_data=True,
    license='BSD License',  # example license
    description='Una app para paginas genericas creada por 10Grapes',
    long_description=README,
    url='https://www.10grapes.com.ar/',
    author='10Grapes',
    author_email='info@10grapes.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)