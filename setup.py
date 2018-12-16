import sys
from setuptools import setup, find_packages


setup(
    name='koala-serializer',
    version='0.6.2',
    description='A tool designed for creating serializable objects among different programming languages',
    long_description='',
    author='Koala',
    author_email='mdan.hagh@gmail.com',
    url='https://github.com/koala-team/serializer',
    keywords='serialize deserialize object compile binary',

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
    ],

    license='MIT',

    install_requires=[
        'configparser==3.5.0',
        'enum34==1.1.6'
    ],

    packages=find_packages(),

    # Make this executable from command line when installed
    scripts=['koalasc'],
    provides=['koalasc']
)
