import sys
from setuptools import setup, find_packages

<<<<<<< HEAD
if sys.version_info<(3, 5):
    raise Exception("interactive_python makes use of asyncio, async, and await,"
                    "and therefore requires Python >= 3.5.x")

setup(
    name='OctoMixInteractiveSA',
    version='0.1.0',
    description='Server to integrate Octoprint to use Mixer Interactive 2.0',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development',
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
=======
if sys.version_info < (3, 5):
    raise Exception("OctoMixInteractiveSA makes use of asyncio, async," +
                    "and await, and therefore requires Python >= 3.5.x")

setup{
    name='OctoMixInteractiveSA',
    version='0.1.0'
    description='Server to act as middleman for Octoprint and Mixer Interactive 2.0'
}
>>>>>>> 7c6fa32d5d4ecfa72be7fd36ac1a992f971536a6
