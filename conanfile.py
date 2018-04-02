from conans import ConanFile, tools
import os


class SevenZinstallerConan(ConanFile):
    name = "7z_installer"
    version = "1.0"
    license = "GNU LGPL + unRAR restriction"
    homepage = "http://www.7-zip.org/"
    url = "http://github.com/conan-community/conan-7z-installer"
    settings = {"os_build": ["Windows"]}
    exports_sources = "sources/*"
    build_policy = "missing"
    description = "7-Zip is open source software. Most of the source code is under the GNU LGPL " \
                  "license. The unRAR code is under a mixed license: GNU LGPL + unRAR restrictions."

    def package(self):
        self.copy("*", dst="bin", src="sources")
        self.copy("*", dst="bin_32", src="sources_32")

    def package_info(self):
        if tools.detected_architecture == "x86":
            self.env_info.path.append(os.path.join(self.package_folder, "bin_32"))
        else:
            self.env_info.path.append(os.path.join(self.package_folder, "bin"))
