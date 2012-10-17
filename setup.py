#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
# 
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from setuptools import setup, find_packages

setup(
    name='cdr-stats',
    version='0.1',
    description='CDR-Stats is a CDR viewer for Asterisk/Freeswitch Call Data Records. It allows you to interrogate your CDR to provide reports and statistics via a simple to use, yet powerful, web interface.',
    long_description=open('README.rst').read(),
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    url='http://www.cdr-stats.org/',
    download_url='https://github.com/Star2Billing/cdr-stats/tarball/master',
    packages=find_packages(),
    include_package_data=True,
    license='MPL 2.0 License',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers, Users',
        'License :: OSI Approved :: MPL 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python, Javascript, HTML',
        'Topic :: Call Analytic Software'
    ],
    zip_safe = False,
)
