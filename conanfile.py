from conans import ConanFile
from conans import __version__ as conan_version
from conans.model.version import Version
import os


class SevenZinstallerConan(ConanFile):
    name = "7z_installer"
    version = "1.0"
    license = "GNU LGPL + unRAR restriction"
    url = "http://github.com/lasote/conan-7z-installer"
    if conan_version < Version("0.99"):
        settings = {"os": ["Windows"]}
    else:
        settings = {"os_build": ["Windows"]}
    exports_sources = "sources/*"

    build_policy = "missing"
    description = "7-Zip is open source software. Most of the source code is under the GNU LGPL " \
                  "license. The unRAR code is under a mixed license: GNU LGPL + unRAR restrictions."

    def package(self):
        self.copy("*", dst="bin", src="sources")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
