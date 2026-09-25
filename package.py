name = "imath"

version = "3.2.2.hh.1.0.0"

authors = [
    "ILM & AcademySoftwareFoundation",
]

description = (
    """Basic, light-weight C++ representation of 2D and 3D vectors and matrices"""
)

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = []

variants = [
    ["python-3.13.9", "boost-1.88"],
    ["python-3.13.10", "boost-1.88"],
]


def commands():
    env.REZ_IMATH_ROOT = "{root}"
    env.Imath_ROOT = "{root}"
    env.Imath_DIR = "{root}/lib64/cmake/Imath"
    env.IMATH_INCLUDE_DIR = "{root}/include"
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake/Imath")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 13:
                env.PYTHONPATH.append("{root}/lib/python3.13/site-packages")


uuid = "repository.Imath"
