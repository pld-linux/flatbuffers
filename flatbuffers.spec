# TODO - other languages:
# dart >= 2.17.0
# go >= 1.19
# java >= 1.8
# kotlin
# lobster
# lua >= 5.1
# C#
# nim >= 1.4.0
# PHP
# Python (2, 3)
# Rust
# Swift
# JavaScript/TypeScript
Summary:	Memory efficient serialization library
Summary(pl.UTF-8):	Wydajna pamięciowo biblioteka do serializacji
Name:		flatbuffers
Version:	25.2.10
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/google/flatbuffers/releases
Source0:	https://github.com/google/flatbuffers/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2153b63d029086c5ba5e943b4c6f0324
URL:		https://google.github.io/flatbuffers/
BuildRequires:	cmake >= 3.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlatBuffers is an efficient cross platform serialization library for
C++, C#, C, Go, Java, JavaScript, Lobster, Lua, TypeScript, PHP,
Python, and Rust. It was originally created at Google for game
development and other performance-critical applications.

%description -l pl.UTF-8
FlatBuffers to wydajna, wieloplatformowa biblioteka do serializacji
dla języków C++, C#, C, Go, Java, JavaScript, Lobster, Lua,
TypeScript, PHP, Python i Rust. Powstała oryginalnie w Google na
potrzeby tworzenia gier i innych aplikacji krytycznych wydajnościowo.

%package devel
Summary:	Header files for FlatBuffers library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FlatBuffers
Group:		Development/Libraries

%description devel
Header files for FlatBuffers library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FlatBuffers.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DFLATBUFFERS_BUILD_FLATHASH=ON \
	-DFLATBUFFERS_BUILD_FLATLIB=OFF \
	-DFLATBUFFERS_BUILD_SHAREDLIB=ON \
	-DFLATBUFFERS_BUILD_TESTS=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# not installed by make
install -d $RPM_BUILD_ROOT%{_bindir}
install -p build/flathash $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflatbuffers.so.%{version}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flatc
%attr(755,root,root) %{_bindir}/flathash
%{_libdir}/libflatbuffers.so
%{_includedir}/flatbuffers
%{_libdir}/cmake/flatbuffers
%{_pkgconfigdir}/flatbuffers.pc
