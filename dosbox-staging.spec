#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : dosbox-staging
Version  : 0.79.0
Release  : 263
URL      : file:///aot/build/clearlinux/packages/dosbox-staging/dosbox-staging-v0.79.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/dosbox-staging/dosbox-staging-v0.79.0.tar.gz
Summary  : DOS/x86 emulator focusing on ease of use
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : SDL2
BuildRequires : SDL2-dev
BuildRequires : SDL2_image
BuildRequires : SDL2_image-dev
BuildRequires : SDL2_net
BuildRequires : SDL2_net-dev
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : alsa-lib
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : alsa-plugins
BuildRequires : alsa-tools
BuildRequires : alsa-tools-dev
BuildRequires : alsa-ucm-conf
BuildRequires : alsa-utils
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : breeze
BuildRequires : breeze-gtk
BuildRequires : breeze-icons
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cairomm-dev
BuildRequires : calf
BuildRequires : calf-dev
BuildRequires : calf-staticdev
BuildRequires : clr-avx-tools
BuildRequires : clr-rpm-config
BuildRequires : cmake
BuildRequires : cmake-dev
BuildRequires : colord-dev
BuildRequires : cups
BuildRequires : cups-dev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : docutils
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expat
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : extra-cmake-modules-data
BuildRequires : fftw-dev
BuildRequires : fftw-staticdev
BuildRequires : findutils
BuildRequires : flac
BuildRequires : flac-dev
BuildRequires : flac-dev32
BuildRequires : flac-staticdev
BuildRequires : flac-staticdev32
BuildRequires : flex
BuildRequires : fluidsynth
BuildRequires : fluidsynth-dev
BuildRequires : fluidsynth-staticdev
BuildRequires : fmt
BuildRequires : fmt-dev
BuildRequires : fmt-staticdev
BuildRequires : fomp
BuildRequires : fomp-dev
BuildRequires : fontconfig
BuildRequires : fontconfig-dev
BuildRequires : fonts-clear
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : fribidi-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : gdk-pixbuf
BuildRequires : gdk-pixbuf-dev
BuildRequires : git
BuildRequires : glib
BuildRequires : glib-bin
BuildRequires : glib-dev
BuildRequires : glib-networking
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : glslang
BuildRequires : gmp-dev
BuildRequires : gnutls
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : googletest-dev
BuildRequires : gperf
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : graphviz
BuildRequires : graphviz-extras
BuildRequires : gtk+-dev
BuildRequires : gtk3
BuildRequires : gtk3-dev
BuildRequires : gtk4
BuildRequires : gtk4-dev
BuildRequires : gtkmm4
BuildRequires : gtkmm4-dev
BuildRequires : gtkmm4-staticdev
BuildRequires : guile
BuildRequires : harfbuzz-dev
BuildRequires : icu4c-dev
BuildRequires : icu4c-lib
BuildRequires : json
BuildRequires : json-dev
BuildRequires : keyutils
BuildRequires : keyutils-dev
BuildRequires : krb5
BuildRequires : krb5-dev
BuildRequires : ladspa_sdk
BuildRequires : ladspa_sdk-dev
BuildRequires : ladspa_sdk-staticdev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfixes-dev
BuildRequires : libXfont2-dev
BuildRequires : libXft
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libcanberra-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libcap-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libfdk_aac-dev
BuildRequires : libfdk_aac-staticdev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt-dev
BuildRequires : libgit2
BuildRequires : libgit2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libjpeg-turbo-lib
BuildRequires : libjpeg-turbo-lib32
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : liblo
BuildRequires : liblo-dev
BuildRequires : liblo-staticdev
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : libogg-staticdev
BuildRequires : libogg-staticdev32
BuildRequires : libpng
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : libpthread-stubs-dev
BuildRequires : librsvg-dev
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-staticdev
BuildRequires : libsigc++-dev
BuildRequires : libsigc++-staticdev
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-staticdev
BuildRequires : libstdc++
BuildRequires : libtool-dev
BuildRequires : libunwind-dev
BuildRequires : libusb-dev
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-dev32
BuildRequires : libvorbis-staticdev
BuildRequires : libvorbis-staticdev32
BuildRequires : libwebp-dev
BuildRequires : libwebp-staticdev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : libxslt-bin
BuildRequires : lilv
BuildRequires : lilv-dev
BuildRequires : lilv-staticdev
BuildRequires : lsp-plugins
BuildRequires : lsp-plugins-dev
BuildRequires : lsp-plugins-staticdev
BuildRequires : lua-dev
BuildRequires : lua-staticdev
BuildRequires : lv2
BuildRequires : lv2-dev
BuildRequires : lxml
BuildRequires : m4
BuildRequires : mda-lv2
BuildRequires : mda-lv2-dev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : meson
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : octave-dev
BuildRequires : openssh
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : opus
BuildRequires : opus-dev
BuildRequires : opus-lib
BuildRequires : opus-staticdev
BuildRequires : opusfile
BuildRequires : opusfile-dev
BuildRequires : opusfile-staticdev
BuildRequires : pango-dev
BuildRequires : pangomm-dev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : perl
BuildRequires : perl(Test::More)
BuildRequires : perl(XML::Parser)
BuildRequires : pipewire
BuildRequires : pipewire-dev
BuildRequires : pipewire-tests
BuildRequires : pixman-dev
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-player-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk4)
BuildRequires : pkgconfig(gtk4-unix-print)
BuildRequires : pkgconfig(gtk4-x11)
BuildRequires : pkgconfig(gtkmm-4.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgcab-1.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(lv2)
BuildRequires : pkgconfig(rubberband)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : procps-ng
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : pygobject
BuildRequires : pypi(html5lib)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(isodate)
BuildRequires : pypi(pyparsing)
BuildRequires : python-graphviz
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rdflib
BuildRequires : readline-dev
BuildRequires : requests
BuildRequires : rubberband-dev
BuildRequires : rubberband-staticdev
BuildRequires : sassc
BuildRequires : sed
BuildRequires : serd
BuildRequires : serd-dev
BuildRequires : serd-staticdev
BuildRequires : setxkbmap
BuildRequires : shared-mime-info
BuildRequires : shared-mime-info-dev
BuildRequires : sord
BuildRequires : sord-dev
BuildRequires : sord-staticdev
BuildRequires : speex-dev
BuildRequires : speex-staticdev
BuildRequires : speexdsp-dev
BuildRequires : speexdsp-staticdev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sratom
BuildRequires : sratom-dev
BuildRequires : sratom-staticdev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : tiff-dev
BuildRequires : tiff-staticdev
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : vamp-sdk
BuildRequires : vamp-sdk-dev
BuildRequires : vamp-sdk-staticdev
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : xauth
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
DOSBox Staging is full x86 CPU emulator (independent of host architecture),
capable of running DOS programs that require real or protected mode.

It features built-in DOS-like shell terminal, emulation of several PC variants
(IBM PC, IBM PCjr, Tandy 1000), CPUs (286, 386, 486, Pentium I), graphic
chipsets (Hercules, CGA, EGA, VGA, SVGA), audio solutions (Sound Blaster,
Gravis UltraSound, Disney Sound Source, Tandy Sound System), CD Digital Audio
emulation (also with audio encoded as FLAC, Opus, OGG/Vorbis, MP3 or WAV),
joystick emulation (supports modern game controllers), serial port emulation,
IPX over UDP, GLSL shaders, and more.

DOSBox Staging is highly configurable, well-optimized and fast enough to run
any old DOS game using modern hardware.

%prep
%setup -q -n dosbox-staging
cd %{_builddir}/dosbox-staging

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641492156
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export ASMFLAGS="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export CXXFLAGS="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export GSETTINGS_SCHEMA_DIR="/usr/share/glib-2.0/schemas"
## altflags1 end
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both  --buildtype=release \
-Ddefault_library=static \
-Duse_alsa=true \
-Duse_fluidsynth=true \
-Duse_opengl=true \
-Duse_png=true \
-Dtry_static_libs=png,opusfile,png \
-Dfluidsynth:enable-floats=true builddir
ninja --verbose %{?_smp_mflags} -C builddir


%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
