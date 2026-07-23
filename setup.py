from setuptools import find_packages, setup

setup(
    name='helloworld-plugin',
    version='0.1.0',
    description='My first plugin',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={'testy': ['helloworld-plugin=helloworld_plugin']},
)