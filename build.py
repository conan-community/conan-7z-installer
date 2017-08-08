import platform
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add({"os": "Windows"}, {}, {}, {}) 
    builder.run()
