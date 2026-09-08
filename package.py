name = "imath"

version = "3.1.5.hh.1.0.2"

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

private_build_requires = ["visual_studio"]

variants = [
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
]


def commands():
    env.REZ_IMATH_ROOT = "{root}"
    env.Imath_ROOT = "{root}"
    env.Imath_DIR = "{root}/lib/cmake/Imath"
    env.LIB.append("{root}/lib")
    env.LD_LIBRARY_PATH.append('{root}/bin')
    # Renamed output (IMATH_LIB_SUFFIX) avoids colliding with Maya's own
    # bundled Imath-3_1.dll, which is missing exports OCIO needs.
    env.PATH.append("{root}/bin")

    if "python" in resolve:
        env.PYTHONPATH.append("{root}/lib")
        env.UE_PYTHONPATH.append("{root}/lib")


uuid = "repository.Imath"
