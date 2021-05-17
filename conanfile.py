from conans import ConanFile, CMake, tools


class VaultConan(ConanFile):
    name = "vault"
    version = "0.41.0"
    license = "MIT"
    author = "Aaron Bedra aaron@aaronbedra.com"
    url = "https://github.com/abedra/libvault"
    description = "A C++ Library for HashiCorp Vault"
    topics = ("hashicorp", "vault", "security")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    _cmake = None

    def requirements(self):
        self.requires("libcurl/7.75.0")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/abedra/libvault.git")

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.definitions["LINK_CURL"] = True
        self._cmake.configure(source_folder="libvault")
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["vault"]

