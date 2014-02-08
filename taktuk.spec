%define name taktuk
%define version 3.7.4
%define release 2
%define lib_name_orig lib%{name}
%define major 3
%define lib_name %mklibname %name%{major}
%define module %name
%define pname perl-%{module}


Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Parallel, scalable launcher for cluster and lightweight grids
License: 	GPLv2+
Group: 		Networking/Remote access
Url:		http://taktuk.gforge.inria.fr/
Source0: 	https://gforge.inria.fr/frs/download.php/5255/%{name}-%{version}.tar.gz
Provides: 	parallel-tools
BuildRequires:	 perl-devel

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
%{__perl} Makefile.PL INSTALLDIRS=vendor DESTDIR=%buildroot
%make
popd

%install
%makeinstall pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
pushd Perl-Module
%makeinstall pkgdocdir=%buildroot/%_defaultdocdir/%name-%version
popd
cp taktuk-light %buildroot/%{_bindir}/taktuk-light
chmod 755 %buildroot/%{_bindir}/taktuk-light

%files
%{_bindir}/taktuk
%{_bindir}/taktuk-light
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_defaultdocdir}/%name-%version

%files -n %{lib_name}
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL NEWS README TODO *.html
%defattr(-,root,root)
%{_libdir}/*.so*

%files -n %{lib_name}-devel
%{_libdir}/*.*a
%{_includedir}/*
%{_libdir}/pkgconfig/%name.pc

%files -n %{pname}
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL NEWS README TODO *.html
%{perl_vendorlib}/*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.7-3mdv2011.0
+ Revision: 615110
- the mass rebuild of 2010.1 packages

* Tue Jan 26 2010 Antoine Ginies <aginies@mandriva.com> 3.7-2mdv2010.1
+ Revision: 496522
- remove old version
- taktuk 3.7
- release 3.6.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Sep 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.6.1-1mdv2009.0
+ Revision: 280628
- new version

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 3.5.2-7mdv2009.0
+ Revision: 261370
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 3.5.2-6mdv2009.0
+ Revision: 254107
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - normalize call to ldconfig in %%post/%%postun

* Mon Mar 10 2008 Erwan Velu <erwan@mandriva.org> 3.5.2-4mdv2008.1
+ Revision: 183366
- Rebuild

* Mon Jan 21 2008 Thierry Vignaud <tv@mandriva.org> 3.5.2-3mdv2008.1
+ Revision: 155650
- rebuild for new perl
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 07 2007 Funda Wang <fwang@mandriva.org> 3.5.2-2mdv2008.1
+ Revision: 106708
- rebuild for new lzma

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 3.5.2-1mdv2008.1
+ Revision: 104064
- new tarball
- new release 3.5.2


* Thu Mar 01 2007 aginies <aginies> 3.0.2-1mdv2007.0
+ Revision: 130602
- Import taktuk

* Thu Mar 01 2007 Antoine Ginies <aginies@mandriva.com> 3.0.2-1mdviggi
- first release

