from distutils.core import setup

### Change 0.1dev to 1.0 when ready to release
setup(
    name='Price Alert',
    version='0.1dev',
    packages=['pricealert',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
