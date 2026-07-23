from setuptools import find_packages, setup

setup(
    name='helloworld-plugin',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        'testy': [
            'helloworld-plugin=helloworld_plugin:HelloWorldConfig'
        ]
    },
)

from setuptools import find_packages, setup

setup(
    name='helloworld-plugin',
    version='0.2.0',
    description='Example of testy plugin',
    install_requires=['openpyxl==3.1.1'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={'testy': ['helloworld-plugin=helloworld_plugin']},
)