from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-mfa-utility',
    version='0.0.1',
    description='Manage AWS MFA Security Credentials',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sri Sowmya Rupa Putta',
    author_email='SXP10090@UCMO.EDU',
    packages=['awsmfa'],
    scripts=['aws-mfa'],
    entry_points={
        'console_scripts': [
            'aws-mfa=awsmfa:main',
        ],
    },
    url='https://github.com/RupaPutta/aws-mfa-utility',
    install_requires=['boto3']
)