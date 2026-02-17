#!/bin/sh

set -e
ls .
mkdir /build
cmake -S /cont -B /build -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_TOOLCHAIN_FILE=docker/windows/mingw-w64-x86_64.cmake
cmake --build /build --parallel
cmake --install /build --prefix "/install"

# HACK: Manual fixup, would be nice to not need this eventually
cp /usr/x86_64-w64-mingw32/lib/libwinpthread-1.dll /install/bin/