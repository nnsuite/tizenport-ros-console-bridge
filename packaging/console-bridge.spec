Name:           console-bridge
Version:        0.3.2
Release:        0
Summary:        Console bridge - library
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://wiki.ros.org/urdf
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%define sover 0
%define prjname urdfdom
%define srcname console_bridge

%description
A ROS-independent package for logging that seamlessly pipes into 
rosconsole/rosout for ROS-dependent packages.

%package -n     lib%{name}%{sover}
Summary:        C++ library for %{prjname}
Group:          System/Libraries
Provides:       lib%{name}%{sover} = %{version}

%description -n lib%{name}%{sover}
A ROS-independent package for logging that seamlessly pipes into 
rosconsole/rosout for ROS-dependent packages.

This package contains the shared library.

%package -n     lib%{name}-devel
Summary:        Development files for %{prjname}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description -n lib%{name}-devel
A ROS-independent package for logging that seamlessly pipes into 
rosconsole/rosout for ROS-dependent packages.

This package contains the header files and libraries needed to develop
application that use %{prjname}.

%prep
%setup -q
cp %{SOURCE1001} .

# Change path to includedir
#sed -e 's|@CMAKE_INSTALL_FULL_INCLUDEDIR@|%{_includedir}/%{srcname}|' \
#    -i $(grep -rl 'CMAKE_INSTALL_FULL_INCLUDEDIR')

%build
cmake . -DCMAKE_INSTALL_PREFIX="%{_prefix}"
make %{?_smp_mflags}

%install
%make_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/lib%{srcname}.so.*

%files -n lib%{name}-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/
%{_includedir}/%{srcname}/
%{_libdir}/%{srcname}/
%{_libdir}/lib%{srcname}.so
%{_libdir}/pkgconfig/%{srcname}.pc

%changelog
