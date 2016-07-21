from conans import ConanFile
from conans.tools import download, unzip

class NLJsonConan(ConanFile):
    name = "nlJson"
    version = "2.0.1"

    def source(self):
	download("https://github.com/nlohmann/json/releases/download/v%s/json.hpp" % self.version, "json.hpp")

    def package(self):
        self.copy("*.hpp", dst="include")

