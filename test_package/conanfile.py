from conans import ConanFile


class SevenZipInstallerConan(ConanFile):
    """ 7Zip installer Conan package test """

    settings = "os"

    def test(self):
        self.run('7z.exe --help')