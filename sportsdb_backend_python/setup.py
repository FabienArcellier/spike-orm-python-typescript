from setuptools import setup, find_packages

setup(
    name='sportsdb_backend',
    version='1.0',
    packages=find_packages(),
    license='',
    classifiers= [
        'Programming Language :: Python :: 3'
    ],
    install_requires = [
        'alembic',
        'ariadne',
        'psycopg2-binary',
        'SQLAlchemy',
        'sqlacodegen',
        'uvicorn'
    ],
)
