%define lib_name_orig lib%{name}
%define major 3
%define lib_name %mklibname %name%{major}
%define module %name
%define pname perl-%{module}


Name: 		taktuk
Version: 	3.7.7
Release: 	1
Summary: 	Parallel, scalable launcher for cluster and lightweight grids
License: 	GPLv2+
Group: 		Networking/Remote access
Url:		https://taktuk.gforge.inria.fr/
Source0:	https://gforge.inria.fr/frs/download.php/33412/%{name}-%{version}.tar.gz
Source1:	taktuk.rpmlintrc
Provides:	parallel-tools
BuildRequires:	perl-devel

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

# FIXME for correct assignment of rights of files and for file-not-utf8
chmod 0644 {AUTHORS,README,NEWS,COPYING,TODO}
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS

%build
%configure2_5x
%make
pushd Perl-Module
%{__perl} Makefile.PL INSTALLDIRS=vendor DESTDIR=%buildroot
%make_build
popd

%install
%make_install pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
pushd Perl-Module
%make_install pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
popd
cp taktuk-light %buildroot/%{_bindir}/taktuk-light
chmod 755 %buildroot/%{_bindir}/taktuk-light

%files
%doc %{_defaultdocdir}/%{name}
%{_bindir}/taktuk
%{_bindir}/taktuk-light
%{_mandir}/man1/*
%{_mandir}/man3/*


%files -n %{lib_name}
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL NEWS README TODO
%{_libdir}/*.so*

%files -n %{lib_name}-devel
%{_includedir}/*
%{_libdir}/pkgconfig/%name.pc

%files -n %{pname}
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL NEWS README TODO
%{perl_vendorlib}/*
