FROM debian:bookworm

ARG ARCH=x86_64
ENV ARCH=${ARCH}

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN if [ "${ARCH}" = "aarch64" ]; then export DEBARCH="arm64"; export DEBGCC="gcc-aarch64-linux-gnu g++-aarch64-linux-gnu"; \
    elif [ "${ARCH}" = "x86_64" ]; then export DEBARCH="amd64"; export DEBGCC="gcc g++"; \
    else export DEBARCH="${ARCH}"; export DEBGCC="gcc g++"; fi \
    && dpkg --add-architecture $DEBARCH \
    && apt -y update \
    && apt -y install $DEBGCC git wget pkg-config make libtool \
    && apt -y install libgl1-mesa-dev:$DEBARCH \
    && apt -y install libegl-dev:$DEBARCH \
    && apt -y install libopengl-dev:$DEBARCH \
    && apt -y install xorg-dev:$DEBARCH 

# Install newer version of CMake
ENV CMAKE_VER=3.31.5
RUN wget https://github.com/Kitware/CMake/releases/download/v3.31.5/cmake-3.31.5-linux-$(uname -m).sh \
    && chmod +x cmake-$CMAKE_VER-linux-$(uname -m).sh \
    && ./cmake-$CMAKE_VER-linux-$(uname -m).sh --prefix=/usr --skip-license

RUN ls /
RUN chmod +x /Cont/docker/linux/build.sh

ENTRYPOINT [ "/Cont/docker/linux/build.sh" ]