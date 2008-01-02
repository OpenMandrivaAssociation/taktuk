%define name taktuk
%define version 3.5.2
%define release %mkrel 2
%define lib_name_orig lib%{name}
%define major 0
%define lib_name %mklibname %name%{major}
%define module %name
%define pname perl-%{module}


Summary: 	Parallel, scalable launcher for cluster and lightweight grids
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.gz
License: 	GPLv2+
Group: 		Networking/Remote access
url:		http://taktuk.gforge.inria.fr/
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  autoconf, automake
requires:	%{lib_name} = %version-%release
Provides: 	parallel-tools

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
%configure
%make
pushd Perl-Module
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
popd

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
pushd Perl-Module
%makeinstall_std pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
popd
cp taktuk-light %buildroot/%{_bindir}/taktuk-light

%post -n %{lib_name}
/sbin/ldconfig

%postun -n %{lib_name}
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/taktuk
%attr(755,root,root) %{_bindir}/taktuk-light
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
