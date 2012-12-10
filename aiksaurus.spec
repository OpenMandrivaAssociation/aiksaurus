%define api		1.2
%define major	0
%define libname		%mklibname %{name} %{api} %{major}
%define develname	%mklibname -d %{name}
%define libgtk		%mklibname %{name}gtk %{api} %{major}
%define develgtk 	%mklibname -d %{name}gtk


Summary:	An English-language thesaurus library
Name:		aiksaurus
Version:	1.2.1
Release:	8
License:	GPLv2+
Group:		Office
URL:		http://sourceforge.net/projects/aiksaurus/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		aiksaurus-1.2.1-gcc43.patch
Patch1:		%{name}-1.2.1-fix-str-fmt.patch

BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	%{name}-data

%description
Aiksaurus is an English-language thesaurus library that can be 
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.  
This package contains a basic command line thesaurus program.

Install Aiksaurus if you want to have a thesaurus available on 
your computer.

%package data
Summary:	An English-language thesaurus library
Group:		Office

%description data
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains the datafiles.

%package -n %{libname}
Summary:	An English-language thesaurus library
Group:		System/Libraries
Requires:	%{name}-data

%description -n %{libname}
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains these libraries.

Install Aiksaurus if you want to have a thesaurus available on
your computer.

%package -n %{develname}
Summary:	Libraries and include files for Aiksuarus
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains the libraries and includes files necessary to develop
applications with Aiksaurus.

%package -n %{name}gtk
Summary:	A GTK+ thesaurus application
Group:		Office

%description -n %{name}gtk
Aiksaurusgtk is a GTK+ interface to the Aiksaurus library.  
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.  
This package provides the standalone GTK+ interface.

%package -n %{libgtk}
Summary:	Libraries for aiksaurusgtk
Group:		System/Libraries

%description -n %{libgtk}
Aiksaurusgtk is a GTK+ interface to the Aiksaurus library.
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.
This package provides the library files for aiksaurusgtk.


%package -n %{develgtk}
Summary:	A GTK+ thesaurus library
Group:		Development/C
Requires:	%{libgtk} = %{version}-%{release}
Provides:	aiksaurusgtk-devel = %{version}-%{release}

%description -n %{develgtk}
This package contains the libraries and includes files necessary to develop
applications with Aiksaurusgtk.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc ChangeLog README COPYING AUTHORS
%{_bindir}/aiksaurus
%{_bindir}/caiksaurus

%files data
%dir %{_datadir}/aiksaurus
%{_datadir}/aiksaurus/*.dat

%files -n %{libname}
%{_libdir}/libAiksaurus-*.so.%{major}*

%files -n %{develname}
%{_libdir}/libAiksaurus.so
%{_libdir}/pkgconfig/aiksaurus-1.0.pc
%dir %{_includedir}/Aiksaurus
%{_includedir}/Aiksaurus/Aiksaurus.h
%{_includedir}/Aiksaurus/AiksaurusC.h

%files -n %{name}gtk
%{_bindir}/gaiksaurus

%files -n %{libgtk}
%{_libdir}/libAiksaurusGTK-*.so.%{major}*

%files -n %{develgtk}
%{_libdir}/libAiksaurusGTK.so
%{_libdir}/pkgconfig/gaiksaurus-1.0.pc
%{_includedir}/Aiksaurus/AiksaurusGTK*.h



%changelog
* Sun Mar 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-8
+ Revision: 786650
- rebuild
- cleaned up spec
- disabled static build

* Fri Jun 12 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.1-7mdv2011.0
+ Revision: 385614
- fix str fmt

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 1.2.1-6mdv2009.1
+ Revision: 301225
- add gcc 4.3 patch
- new devel package name policy
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 25 2008 Emmanuel Andry <eandry@mandriva.org> 1.2.1-4mdv2008.1
+ Revision: 189871
- Fix lib group

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.2.1-3mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import aiksaurus


* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 1.2.1-3mdv2007.0
- rebuild

* Fri Sep 02 2005 Marcel Pol <mpol@mandriva.org> 1.2.1-2mdk
- rebuild

* Mon Aug 09 2004 Marcel Pol <mpol@mandrake.org> 1.2.1-1mdk
- 1.2.1
- increase api version
- no need to run aclocal anymore

* Wed Jun 09 2004 Marcel Pol <mpol@mandrake.org> 1.0.2-0.cvs20040609.1mdk
- cvs snapshot

* Wed Dec 16 2003 Marcel Pol <mpol@mandrake.org> 1.0.1-5mdk
- use better 64bit (build)requires

* Sun Oct 19 2003 Marcel Pol <mpol@gmx.net> 1.0.1-4mdk
- buildrequires

* Fri Aug 29 2003 Marcel Pol <mpol@gmx.net> 1.0.1-3mdk
- buildrequires

* Mon Jul 21 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.1-2mdk
- Rebuild

* Wed Jul 16 2003 Marcel Pol <mpol@gmx.net> 1.0.1-1mdk
- rebuild for provides/requires
- s/Aiksaurus/aiksaurus
- new url
- source now includes gtk frontend
- drop patch0
- run aclocal to avoid libtool problems
- new soname

* Thu May 22 2003 Marcel Pol <mpol@gmx.net> 0.15-2mdk
- rebuild for provides/requires

* Mon Mar 10 2003 Marcel Pol <mpol@gmx.net> 0.15-1mdk
- initial mandrake release
