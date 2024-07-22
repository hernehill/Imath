name = "imath"

version = "3.1.5.hh.1.0.0"

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
    "boost",
]

private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
]


def commands():
    env.REZ_IMATH_ROOT = "{root}"
    env.Imath_ROOT = "{root}"
    env.Imath_DIR = "{root}/lib64/cmake/Imath"
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 7:
                env.PYTHONPATH.append("{root}/lib/python3.7/site-packages")
            elif python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib/python3.9/site-packages")
            elif python_ver.minor == 10:
                env.PYTHONPATH.append("{root}/lib/python3.10/site-packages")
            elif python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib/python3.11/site-packages")
            elif python_ver.minor == 12:
                env.PYTHONPATH.append("{root}/lib/python3.12/site-packages")


uuid = "repository.Imath"
