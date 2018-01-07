import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='almvotes',
    version='0.1',
    packages=['almvotes', 'almvotos'],
    description='Libreria para el almacenamiento de los votos en la BD',
    long_description=README,
    author='Equipo almacenamiento',
    author_email='juasanpar@hotmail.com',
    url='',
    license='MIT',
    install_requires=[
        'Django>=1.8',
    ]
)