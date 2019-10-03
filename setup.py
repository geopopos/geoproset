try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'This is a simple package to set up a new python project directory with a specified name',
    'author': 'Georgios Roros',
    'author_email': 'george@georgiosroros.com',
    'version': '0.1',
    'install_requires': [
        'nose',
        'Click',
    ],
    'entry_points': '''
          [console_scripts]
          geoproset=geoproset:main
    ''',
    'py_modules': ['geoproset'],
    'scripts': [],
    'name': 'geoproset'
}

setup(**config)
