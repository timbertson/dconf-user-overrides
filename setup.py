from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

def read(relpath):
	with open(path.join(here, *relpath.split('/')), encoding='utf-8') as f:
		return f.read()

setup(
	name='dconf-user-overrides',
	version=read('VERSION'),
	description='dconf-user-overrides',
	long_description=read('README.rst'),
	url='https://github.com/timbertson/dconf-user-overrides',
	package_data={
		'share/applications': ['dconf-user-overrides.desktop'],
	},

	# packages=find_packages(exclude=['doc', 'test']),
	# or, for a single module:
		# py_modules=["my_module"],

	install_requires=[ 'pygobject' ],

	scripts = [ 'dconf-user-overrides' ],
)

