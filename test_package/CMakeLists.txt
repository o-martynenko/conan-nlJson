project(NLJsonTest)
cmake_minimum_required(VERSION 3.7.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(greet main.cpp)
target_link_libraries(greet ${CONAN_LIBS})
set_property(TARGET greet PROPERTY CXX_STANDARD 11)
