from distutils.core import setup, Extension
import numpy

cos_module_np = Extension('cos_module_np', sources=['cos_module_np.c'],
                          include_dirs=[numpy.get_include()])

setup(ext_modules=[cos_module_np])
