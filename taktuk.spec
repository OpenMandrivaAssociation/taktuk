%define name taktuk
%define version 3.6.2
%define release %mkrel 1
%define lib_name_orig lib%{name}
%define major 0
%define lib_name %mklibname %name%{major}
%define module %name
%define pname perl-%{module}


Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Parallel, scalable launcher for cluster and lightweight grids
License: 	GPLv2+
Group: 		Networking/Remote access
url:		http://taktuk.gforge.inria.fr/
Source0: 	https://gforge.inria.fr/frs/download.php/5255/%{name}-%{version}.tar.gz
Provides: 	parallel-tools
BuildRoot:	 %{_tmppath}/%{name}-%{version}

%description
TakTuk is a tool for deploying parallel remote executions of commands to a
potentially large set of remote nodes. It spreads itself using an adaptive 
algorithm and sets up an interconnection network to transport commands and 
perform I/Os multiplexing/demultiplexing. The TakTuk mechanics dynamically
 adapt to environment (machine performance and current load, network 
contention) by using a reactive work-stealing algorithm that mix local 
parallelization and work distribution.

%package -n %{lib_name}-devel
Summary:        Taktuk header files and static libraries
Group:          Development/Other
Requires:       %{name} = %{version}

%description -n %{lib_name}-devel
Taktuk header files and static libraries

%package        -n %{lib_name}
Summary:        Parallel, scalable launcher for cluster devel
Group:          Development/Other

%description -n %{lib_name}
TakTuk is a tool for deploying parallel remote executions of commands to a
potentially large set of remote nodes.
All libs.

%package -n %{pname}
Summary:        Taktuk Perl file
Group:          Development/Perl
Requires:       %{name} = %{version}

%description -n %{pname}
Taktuk Perl Package

%prep
%setup -q -n %name-%version

%build
%configure2_5x
%make
pushd Perl-Module
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
popd

%install
rm -rf %{buildroot}
%makeinstall pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
pushd Perl-Module
%makeinstall_std pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
popd
cp taktuk-light %buildroot/%{_bindir}/taktuk-light
chmod 755 %buildroot/%{_bindir}/taktuk-light

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/taktuk
%{_bindir}/taktuk-light
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_defaultdocdir}/%name-%version

%files -n %{lib_name}
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL NEWS README sample_session.txt TODO *.html
%defattr(-,root,root)
%{_libdir}/*.so*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_libdir}/*.*a
%{_includedir}/*
%{_libdir}/pkgconfig/%name.pc

%files -n %{pname}
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL NEWS README sample_session.txt TODO *.html
%{perl_vendorlib}/*
