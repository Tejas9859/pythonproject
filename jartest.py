import PyInstaller.__main__

PyInstaller.__main__.run([
    'testpython.py','new.py'
    '--onefile',
    '--name=myjar'
])
