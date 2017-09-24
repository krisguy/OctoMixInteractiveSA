import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 5):
    raise Exception("OctoMixInteractiveSA makes use of asyncio, async," +
                    "and await, and therefore requires Python >= 3.5.x")

setup{
    name='OctoMixInteractiveSA',
    version='0.1.0'
    description='Server to act as middleman for Octoprint and Mixer Interactive 2.0'
}
