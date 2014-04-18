import os
import sys
from setuptools import setup, find_packages

description = "Snapper balance from the confort of your terminal"

setup(
    name = "snapperbal",
    version = "1.0",
    url = 'http://example.org/',
    license = 'BSD',
    description = description,
    long_description = description,
    author = 'Filype Pereira',
    author_email = 'pereira.filype@gmail.com',
    packages = find_packages('.'),
    package_dir = {'': '.'},
    install_requires = ['prettytable', 'BeautifulSoup'],
    entry_points= {'console_scripts': [
            'snapperbal = snapper:main'
        ]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ],
)