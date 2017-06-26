from distutils.core import setup
from Cython.Build import cythonize

setup(name="rbf_network_cython", ext_modules=cythonize("rbf_network_cython.pyx"))
