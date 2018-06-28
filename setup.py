from setuptools import setup

setup(
    name='temperature',
    version='1.0.0',
    packages=['temperature'],
    url='',
    license='MIT',
    author='PERL',
    author_email='per.voie@gmail.com',
    description='Temperature conversions. Example project to familiarize with GitHub and TravisCI',
    entry_points={
        'console_scripts': ['convert-temperature=temperature.conversion:main'],
    },
    zip_safe=True
)
