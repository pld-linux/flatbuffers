Summary:	Memory efficient serialization library
Summary(pl.UTF-8):	Wydajna pamięciowo biblioteka do serializacji
Name:		flatbuffers
Version:	22.12.06
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://github.com/google/flatbuffers/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	33977086e1e28bb73c53cdf0d0584eac
URL:		https://google.github.io/flatbuffers/
BuildRequires:	cmake >= 3.16
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
%cmake \
	-DFLATBUFFERS_BUILD_FLATLIB=OFF \
	-DFLATBUFFERS_BUILD_SHAREDLIB=ON \
	-DFLATBUFFERS_BUILD_TESTS=OFF \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# somewhy not installed by make
cd build
install -d $RPM_BUILD_ROOT%{_bindir}
install -p flatc flathash $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflatbuffers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflatbuffers.so.22

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flatc
%attr(755,root,root) %{_bindir}/flathash
%{_includedir}/flatbuffers
%{_libdir}/cmake/flatbuffers
%{_libdir}/libflatbuffers.so
%{_pkgconfigdir}/flatbuffers.pc
