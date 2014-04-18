import os
import sys
from setuptools import setup, find_packages
from snapper import __version__

description = "Snapper balance from the confort of your terminal"

setup(
    name = "snapperbal",
    version = __version__,
    url = 'http://example.org/',
    license = 'BSD',
    description = description,
    long_description = description,
    author = 'Filype Pereira',
    author_email = 'pereira.filype@gmail.com',
    # packages = find_packages('.'),
    py_modules=['snapper'],
    package_dir = {'': '.'},
    install_requires = ['prettytable', 'BeautifulSoup'],
    entry_points= {'console_scripts': [
            'snapperbal = snapper:main'
        ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ],
)