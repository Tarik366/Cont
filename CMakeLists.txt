cmake_minimum_required(VERSION 3.20)
project(ContController)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(ANDROID)
    set(SDL_STATIC ON CACHE BOOL "Build static SDL library" FORCE)
    set(SDL_SHARED OFF CACHE BOOL "Build shared SDL library" FORCE)
endif()

include(FetchContent)

# ---------- SDL3 ----------
FetchContent_Declare(
    SDL3
    GIT_REPOSITORY https://github.com/libsdl-org/SDL.git
    GIT_TAG release-3.2.0   # sabit versiyon!
)

FetchContent_MakeAvailable(SDL3)

# ---------- YAML ----------
FetchContent_Declare(
  yaml-cpp
  GIT_REPOSITORY https://github.com/jbeder/yaml-cpp.git
  GIT_TAG yaml-cpp-0.9.0 # Can be a tag (yaml-cpp-x.x.x), a commit hash, or a branch name (master)
)
FetchContent_MakeAvailable(yaml-cpp)

if(ANDROID)
    find_library(GLES3_LIB GLESv3 REQUIRED)
    find_library(ANDROID_LOG_LIB log REQUIRED)
    find_library(ANDROID_LIB android REQUIRED)
    
    set(PLATFORM_LIBS ${GLES3_LIB} ${ANDROID_LOG_LIB} ${ANDROID_LIB})
else()
    find_package(OpenGL REQUIRED)
    set(PLATFORM_LIBS OpenGL::GL)
endif()

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

target_include_directories(ContController PUBLIC 
    "${PROJECT_SOURCE_DIR}/include"
)

include_directories(include/)

set(SOURCES src/)

add_executable(ContController ${SOURCES})

if(NOT ANDROID)
    add_custom_command(TARGET ContController POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CMAKE_CURRENT_SOURCE_DIR}/default_config.yaml"
        "$<TARGET_FILE_DIR:ContController>/default_config.yaml"
    )
endif()

install(TARGETS ContController
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Runtime bağımlılıklarını (DLL'ler vb.) yükle
install(RUNTIME_DEPENDENCY_SET cont_runtime_deps
    DESTINATION bin
)

# Eğer Windows ise SDL3.dll'i manuel kopyalamak gerekebilir (FetchContent kullandığın için)
if(WIN32)
    install(FILES $<TARGET_FILE:SDL3::SDL3> DESTINATION .)
endif()