# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name = "mapView",
    packages = ["roadSegmentation"],
    version = "0.1",
    install_requires = [
        'psycopg2',
        'geojson',
        'matplotlib',
        'numpy',
        'opencv-python'
    ],
    tests_require=['nose']
)
