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

