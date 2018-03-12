from setuptools import setup, find_packages
import os,sys

def readme():
    with open('README.md') as f:
        return f.read()

# Hackishly inject a constant into builtins to enable importing of the
# package before the library is built.
import sys
if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins

builtins.__THISTOTHAT_SETUP__ = True
import thistothat
version = thistothat.__version__

setup(name = "thistothat",
    version = version,
    description = "Tools for interpolating various astrophysical relations, many related to M dwarf physical properties.",
    long_description = readme(),
    author = "Zachory K. Berta-Thompson",
    author_email = "zach.bertathompson@colorado.edu",
    url = "https://github.com/zkbt/thistothat",
    packages = find_packages(),
    package_data = {'thistothat':['data/*.txt', 'data/baraffe/*.txt']},
    include_package_data=True,
    scripts = [],
    classifiers=[
      'Intended Audience :: Science/Research',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    install_requires=['numpy', 'astropy', 'scipy', 'matplotlib' ],
    zip_safe=False,
    license='MIT',

)
