from distutils.core import setup
import inspect, os
from py2exe.build_exe import py2exe

APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path = os.path.join(APP_ROOT, 'csv_files')
db_path = os.path.join(APP_ROOT, 'db_files')

data_files = [('csv_files', [os.path.join(path, "iris.csv")]), ('csv_files', [os.path.join(path, "abalone.csv")]),
              ('db_files', [os.path.join(db_path, "iris.db")]), ('db_files', [os.path.join(db_path, "abalone.db")])]
setup(console=["console_app.py"], data_files=data_files, zipfile=None, skip_archive=True)