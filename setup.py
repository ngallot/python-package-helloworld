import setuptools
from pyhw import __version__

setuptools.setup(
    name='pyhw',
    version=__version__,
    author='ngallot',
    description='A minimal python package',
    packages=setuptools.find_packages(),
    install_requires=[
        "pydantic==1.6.2"
    ]
)