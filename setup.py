from distutils.core import setup
import os
from py2exe.build_exe import py2exe

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

data_files = [('csv_files', [os.path.join(APP_ROOT, "iris.csv")]), ('csv_files', [os.path.join(APP_ROOT, "abalone.csv")])]
setup(console=[{"script": "console_app.py"}], data_files=data_files, options={"py2exe":{"unbuffered": True, "optimize": 2}}, zipfile = None)