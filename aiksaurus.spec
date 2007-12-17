%define name	aiksaurus
%define version	1.2.1
%define release	%mkrel 3

%define api_version	1.2
%define lib_major	0
%define lib_name	%mklibname %{name}- %{api_version} %{lib_major}
%define lib_namegtk	%mklibname %{name}gtk- %{api_version} %{lib_major}


Summary:	An English-language thesaurus library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Office
URL:		http://sourceforge.net/projects/aiksaurus/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel
BuildRequires:	autoconf2.5 automake1.7
BuildRequires:	gnome-common
Requires:	%{name}-data
Provides:	Aiksaurus
Obsoletes:	Aiksaurus

%description
Aiksaurus is an English-language thesaurus library that can be 
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.  
This package contains a basic command line thesaurus program.

Install Aiksaurus if you want to have a thesaurus available on 
your computer.

%package -n %name-data
Summary:        An English-language thesaurus library
Group:          Office
Provides:	Aiksaurus-data
Obsoletes:	Aiksaurus-data

%description -n %name-data
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains the datafiles.

%package -n %lib_name
Summary:	An English-language thesaurus library
Group:          Office
Requires:	%{name}-data
Provides:	libAiksaurus0
Obsoletes:	libAiksaurus0

%description -n %lib_name
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains these libraries.

Install Aiksaurus if you want to have a thesaurus available on
your computer.

%package -n %lib_name-devel
Summary:	Libraries and include files for Aiksuarus
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	aiksaurus-devel = %{version}-%{release}
Provides:	aiksaurus-%{api_version}-devel = %{version}-%{release}

%description -n %lib_name-devel
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

%package -n %{lib_namegtk}
Summary:        Libraries for aiksaurusgtk
Group:          Office
Provides:	AiksaurusGTK
Obsoletes:	AiksaurusGTK

%description -n %{lib_namegtk}
Aiksaurusgtk is a GTK+ interface to the Aiksaurus library.
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.
This package provides the library files for aiksaurusgtk.


%package -n %{lib_namegtk}-devel
Summary:        A GTK+ thesaurus library
Group:          Development/C
Requires:       %{lib_namegtk} = %{version}-%{release}
Provides:       aiksaurusgtk-devel = %{version}-%{release}
Provides:       aiksaurusgtk-%{api_version}-devel = %{version}-%{release}

%description -n %{lib_namegtk}-devel
This package contains the libraries and includes files necessary to develop
applications with Aiksaurusgtk.


%prep
%setup -q -n %{name}-%{version}

# run with cvs release
#./autogen.sh

%build

%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -n %lib_name -p /sbin/ldconfig
%post -n %lib_namegtk -p /sbin/ldconfig

%postun -n %lib_name -p /sbin/ldconfig
%postun -n %lib_namegtk -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc ChangeLog README COPYING AUTHORS
%{_bindir}/aiksaurus
%{_bindir}/caiksaurus

%files -n %name-data
%defattr(-, root, root)
%dir %{_datadir}/aiksaurus
%{_datadir}/aiksaurus/*.dat

%files -n %lib_name
%defattr(-, root, root)
%{_libdir}/libAiksaurus-*.so.*

%files -n %lib_name-devel
%defattr(-, root, root)
%{_libdir}/libAiksaurus.so
%{_libdir}/libAiksaurus.*a
%{_libdir}/pkgconfig/aiksaurus-1.0.pc
%dir %{_includedir}/Aiksaurus
%{_includedir}/Aiksaurus/Aiksaurus.h
%{_includedir}/Aiksaurus/AiksaurusC.h


%files -n %{name}gtk
%defattr(-, root, root)
%{_bindir}/gaiksaurus

%files -n %{lib_namegtk}
%defattr(-, root, root)
%{_libdir}/libAiksaurusGTK-*.so.*

%files -n %{lib_namegtk}-devel
%defattr(-, root, root)
%{_libdir}/libAiksaurusGTK.*a
%{_libdir}/libAiksaurusGTK.so
%{_libdir}/pkgconfig/gaiksaurus-1.0.pc
%{_includedir}/Aiksaurus/AiksaurusGTK*.h


