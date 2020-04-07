from setuptools import setup, find_packages

setup(
    name='ci_tests',
    version='1.0',
    packages=find_packages(),
    license='',
    classifiers= [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    entry_points = {
        'console_scripts': [
            'wait_datastore = ci_tests.wait_datastore:main',
        ],
    },
    install_requires = [
        'click',
        'psycopg2-binary',
        'retrying'
    ],
)
