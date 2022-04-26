from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

os.environ["CXX"] = "/opt/hipSYCL/bin/syclcc-clang --hipsycl-targets='hip:gfx900'"# -frtti"
os.environ["CC"] = "/opt/hipSYCL/bin/syclcc-clang --hipsycl-targets='hip:gfx900'"# -frtti"
os.environ['LDSHARED'] = "/opt/hipSYCL/bin/syclcc-clang --hipsycl-targets='hip:gfx900' -shared"

examples_extension = Extension(
    name="pyexamples",
    language="c++",
    sources=["pyexamples.pyx"],
    libraries=["examples"], #, "cudart", "rt-backend-cuda","rt-backend-omp", "hipSYCL_clang"],
    library_dirs=["lib",], # "/usr/local/cuda/lib64","/opt/hipSYCL/lib/hipSYCL","/opt/hipSYCL/lib"],
    include_dirs=["lib",], # "/opt/hipSYCL/incude"],
    extra_compile_args=[], # "-L/opt/hipSYCL/lib/hipSYCL", "-lrt-backend-cuda", "-L/opt/hipSYCL/lib"],
)
setup(
    name="pyexamples",
    ext_modules=cythonize([examples_extension])
)
