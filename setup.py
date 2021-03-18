from setuptools import setup, find_packages

setup(
    name='dask-lightgbm',
    packages=find_packages(),
    install_requires=[
        'lightgbm==2.3.1',
        'dask[complete]==2021.2.0',
        'dask-ml==1.8.0',
        'numpy==1.20.1',
    ],
    python_requires = '>=3.8'
)
