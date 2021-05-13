from setuptools import setup

with open("requirements.txt", 'r') as f:
    install_requires = f.read()

setup(
    name='chadutils',
    version='0.1.0',
    description='chadutils',
    zip_safe=False,
    install_requires=install_requires.split(),
)
