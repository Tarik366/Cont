cmake_minimum_required(VERSION 3.20)
project(ContController)

set(CMAKE_CXX_STANDARD 20)
set(SDL_STATIC ON CACHE BOOL "" FORCE)
set(SDL_SHARED OFF CACHE BOOL "" FORCE)
# SDL3 uses another names sometime:
set(SDL_STATIC_ENABLED_BY_DEFAULT ON)

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
    include/imgui/imgui.cpp
    include/imgui/imgui_draw.cpp
    include/imgui/imgui_tables.cpp
    include/imgui/imgui_widgets.cpp
    include/imgui/backends/imgui_impl_sdl3.cpp
    include/imgui/backends/imgui_impl_opengl3.cpp
    include/imgui/imgui_demo.cpp
)

target_include_directories(imgui PUBLIC
    include/imgui
    include/imgui/backends
)

target_link_libraries(imgui PUBLIC SDL3::SDL3)

add_executable(ContController src/main.cpp)

target_link_libraries(ContController
    imgui
    SDL3::SDL3
    OpenGL::GL
)

install(TARGETS ContController
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Runtime bağımlılıklarını (DLL'ler vb.) yükle
install(RUNTIME_DEPENDENCY_SET cont_runtime_deps
    DESTINATION bin
)

# SDL3'ün runtime dosyalarını (DLL) yükleme klasörüne kopyalamasını sağla
install(TARGETS ContController
    RUNTIME DESTINATION .
    BUNDLE DESTINATION .
)

# Eğer Windows ise SDL3.dll'i manuel kopyalamak gerekebilir (FetchContent kullandığın için)
if(WIN32)
    install(FILES $<TARGET_FILE:SDL3::SDL3> DESTINATION .)
endif()