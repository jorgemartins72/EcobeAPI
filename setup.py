import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
	content = ""
	with io.open(
		os.path.join(os.path.dirname(__file__), *paths),
		encoding=kwargs.get("encoding", "utf8"),
	) as open_file:
		content = open_file.read().strip()
	return content


def read_requirements(path):
	return [
		line.strip()
		for line in read(path).split("\n")
		if not line.startswith(('"', "#", "-", "git+"))
	]


setup(
	name="ecobe",
	version="0.0.1",
	description="Ecobe Api",
	url="http://ecobecienciacomvida.com.br/",
	python_requires=">=3.12",
	long_description="Ecobe Api",
	author="Jorge Martins",
	packages=find_packages(exclude=["tests"]),
	include_package_data=True,
	install_requires=read_requirements("requirements.txt"),
	entry_points={
		"console_scripts": ["ecobe = cli:main"]
	}
)