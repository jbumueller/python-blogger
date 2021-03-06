from setuptools import setup, find_packages
import sys, os

version = '1.1'

setup(name='pyblog',
	version=version,
	description="This library provides a python interface for the various blogging API.",
	long_description=open('README.md').read(),
	classifiers=[
	"Intended Audience :: Developers",
	"Programming Language :: Python",
	"Development Status :: 6 - Mature"
	],
	keywords='blog api',
	author='The Atlantic',
	author_email='atmoprogrammers@theatlantic.com',
	url='http://code.google.com/p/python-blogger/',
	license='BSD',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	include_package_data=True,
	zip_safe=True,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points="""
	# -*- Entry points: -*-
	""",
	)
