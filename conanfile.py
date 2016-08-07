from conans import ConanFile
from conans.tools import download, unzip

class NLJsonConan(ConanFile):
    name = "nlJson"
    version = "2.0.2"
    url = "https://github.com/arnemertz/conan-nlJson.git"
    license = "MIT"
    author = "Arne Mertz (arne-mertz.de/contact-me)"
    settings = None #header only

    def source(self):
	download("https://github.com/nlohmann/json/releases/download/v%s/json.hpp" % self.version, "json.hpp")

    def build(self):
        None #header only

    def package(self):
        self.copy("*.hpp", dst="include")

