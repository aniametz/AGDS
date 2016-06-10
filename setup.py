from cx_Freeze import setup, Executable

setup(
    name="console_app",
    version="0.1",
    description=" ",
    executables=[Executable("console_app.py")]
    )