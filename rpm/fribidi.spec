Summary: Library implementing the Unicode Bidirectional Algorithm
Name: fribidi
Version: 1.0.5
Release: 1
URL: https://github.com/fribidi/fribidi/
Source: https://github.com//%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
License: LGPLv2+ and UCD
Group: System Environment/Libraries
Patch1: 0001-Avoid-compiling-doc-dir.patch

%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package devel
Summary: Libraries and include files for FriBidi
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Include files and libraries needed for developing applications which use
FriBidi.

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch1 -p1

%build
%autogen --disable-static
make

%check
make check

%install
make DESTDIR=$RPM_BUILD_ROOT install INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.*

%files devel
%doc README AUTHORS THANKS NEWS TODO
%{_includedir}/fribidi
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/*.pc

