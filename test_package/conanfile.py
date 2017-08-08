from conans import ConanFile

class SevenZipInstallerConan(ConanFile):

    def test(self):
        self.run('7z.exe --help')