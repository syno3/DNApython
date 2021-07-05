from setuptools import find_packages, setup
setup(
    name='mypythonlib',
    packages=find_packages(include=['DNApython']),
    version='0.1.0',
    description='DNA genome sequence analysis with python',
    author='Festus murimi',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)