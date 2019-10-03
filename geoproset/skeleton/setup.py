import json
try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

with open("config.json", "r") as read_file:
    config = json.load(read_file)

setup(**config)
