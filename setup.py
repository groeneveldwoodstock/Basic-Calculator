"""
This is a setup.py script generated by py2applet

Usage:
    Docs at https://py2app.readthedocs.io/en/latest/
    python3 setup.py py2app
"""

from setuptools import setup

APP = ['TkinterCalc2.py']
# location of these files is dependent upon your machine. 
DATA_FILES = ['/Users/groeneveld/Documents/Coding/Python/BasicCalculator/Calc1/icon.icns']
OPTIONS = {'iconfile': '/Users/groeneveld/Documents/Coding/Python/BasicCalculator/Calc1/icon.icns'}

setup(
    name = "Basic Calc",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
