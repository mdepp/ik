from conans import ConanFile, CMake, tools


class IKConan(ConanFile):
    name = "ik"
    version = "1.1"
    license = "MIT"
    url = "https://github.com/mdepp/ik"
    description = "Unnoficial package for the inverse kinematics library ik"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    exports_sources = "ik/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="ik")
        cmake.build()
        self.run("mv lib/ik.a lib/libik.a")

    def package(self):
        self.copy("*.h", dst="include/ik", src="include/public/ik")
        self.copy("*.h", dst="include/ik", src="ik/include/public/ik")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ik"]
