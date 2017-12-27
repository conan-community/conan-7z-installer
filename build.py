from conan.packager import ConanMultiPackager
from conans import __version__ as conan_version
from conans.model.version import Version


if __name__ == "__main__":
    builder = ConanMultiPackager()
    os_name = "os" if conan_version < Version("0.99") else "os_build"
    builder.add({os_name: "Windows"}, {}, {}, {})
    builder.run()
