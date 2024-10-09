from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='jogo_campo_minado',
    version='0.0.2',
    author='Lucas Valencio Fonseca',
    author_email='lucas.angawende@hotmail.com',
    description='Jogo Campo Minado',
    long_description=page_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires = requirements,
)