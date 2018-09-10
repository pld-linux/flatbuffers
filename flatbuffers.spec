Summary:	Memory efficient serialization library
Name:		flatbuffers
Version:	1.9.0
Release:	0.1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/google/flatbuffers/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8be7513bf960034f6873326d09521a4b
URL:		https://google.github.io/flatbuffers/
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlatBuffers is an efficient cross platform serialization library for
C++, C#, C, Go, Java, JavaScript, Lobster, Lua, TypeScript, PHP,
Python, and Rust. It was originally created at Google for game
development and other performance-critical applications.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries

%description devel
Header files for %{name} library.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flatc
