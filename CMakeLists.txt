cmake_minimum_required(VERSION 3.20)
project(ContController)

set(CMAKE_CXX_STANDARD 20)

include(FetchContent)

# ---------- SDL3 ----------
FetchContent_Declare(
    SDL3
    GIT_REPOSITORY https://github.com/libsdl-org/SDL.git
    GIT_TAG release-3.2.0   # sabit versiyon!
)

FetchContent_MakeAvailable(SDL3)

# OpenGL
find_package(OpenGL REQUIRED)

# ImGui
add_library(imgui
    include/imgui_b/imgui.cpp
    include/imgui_b/imgui_draw.cpp
    include/imgui_b/imgui_tables.cpp
    include/imgui_b/imgui_widgets.cpp
    include/imgui_b/backends/imgui_impl_sdl3.cpp
    include/imgui_b/backends/imgui_impl_opengl3.cpp
    include/imgui_b/imgui_demo.cpp
)

target_include_directories(imgui PUBLIC
    include/imgui_b
    include/imgui_b/backends
)

add_executable(ContController src/main.cpp)

target_link_libraries(ContController
    imgui
    SDL3::SDL3
    OpenGL::GL
)
