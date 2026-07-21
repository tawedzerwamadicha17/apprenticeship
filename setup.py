from setuptools import find_packages, setup

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in apprenticeship/__init__.py
from apprenticeship import __version__ as version

setup(
	name="apprenticeship",
	version=version,
	description="Apprenticeship training and workplace assessment",
	author="Tawe",
	author_email="mtawedzerwadonald17@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
