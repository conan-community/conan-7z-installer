from conans import ConanFile
import os


class SevenZinstallerConan(ConanFile):
    name = "7z_installer"
    version = "0.1"
    license = "GNU LGPL + unRAR restriction"
    url = "http://github.com/lasote/conan-7z-installer"
    settings = {"os": ["Windows"]}
    exports = "sources/*"
    build_policy = "missing"

    def package(self):
        self.copy("*", dst="bin", src="sources")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
