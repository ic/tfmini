from __future__ import print_function
from setuptools import setup, find_packages

# check rst
# python setup.py check --restructuredtext

PACKAGE_NAME = 'tfmini'

setup(
	author='Kevin Walchko',
	author_email='walchko@users.noreply.github.com',
	name=PACKAGE_NAME,
	version='0.1.3',
	description='A driver for the TFmini LiDAR sold by Sparkfun',
	long_description=open('readme.rst').read(),
	url='http://github.com/walchko/{}'.format(PACKAGE_NAME),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Libraries :: Application Frameworks'
	],
	license='MIT',
	keywords=['robot', 'pi', 'serial', 'sensor', 'range', 'ranging', 'robotics', 'tf'],
	packages=find_packages('.'),
	install_requires=['pyserial'],
)
