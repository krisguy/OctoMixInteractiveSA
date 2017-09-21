import sys
from setuptools import setup, find_packages

if sys.version_info<(3, 5):
    raise Exception("interactive_python makes use of asyncio, async, and await,"
                    "and therefore requires Python >= 3.5.x")

setup(
    name='interactive_python',
    version='0.1.0',
    description='Hook for Octoprint to use Mixer Interactive 2.0',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries'
    ],
    author='Kris Gainsforth',
    author_email='krisguy@krisguy.com',
    url='https://github.com/krisguy/OctoMixInteractive-StandAlone',
    license='GPLv2',
    packages=find_packages(exclude=['tests']),
    install_requires=['websockets>=3.3', 'varint>=1.0.2', 'pyee>=3.0.3',
                      'aiohttp>=2.0.7'],
    include_package_data=True,
)
