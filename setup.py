# setup.py
from setuptools import setup, find_packages

setup(
    name='captchabusters',
    version='1.0.0',
    author='Its3rr0rsWRLD',
    description='Python package for interacting with the CaptchaBusters API',
    url='https://github.com/yourusername/captchabusters-python',
    packages=find_packages(),
    install_requires=['requests'],
)