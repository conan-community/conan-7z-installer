from conans import ConanFile, CMake, tools
import os


class SevenZinstallerConan(ConanFile):
    name = "7z_installer"
    version = "0.1"
    license = "GNU LGPL + unRAR restriction"
    url = "http://github.com/lasote/conan-7z-installer"
    settings = {"os": ["Windows"], "arch": ["x86_64"]}
    exports = "sources/*"

    def package(self):
        self.copy("*", dst="bin", src="sources")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
