from setuptools import find_packages
from setuptools import setup


setup(
	include_package_data=True,
	install_requires=[
		'pyramid',
	],
	name='pyramid-heroku-redis',
	packages=find_packages(),
)
