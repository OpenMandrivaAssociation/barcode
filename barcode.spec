%define name	barcode
%define version	0.98
%define release	%mkrel 10

%define major 0
%define libname %mklibname barcode %{major}
%define develname %mklibname barcode -d

Summary:	GNU barcode
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Publishing
Source:		ftp://ar.linux.it/pub/barcode/%name-%{version}.tar.bz2
Patch0:		barcode-0.98-fix-str-fmt.patch
Patch1:		barcode-0.98-fix-installation.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		http://gnu.systemy.it/software/barcode

%description
This is GNU-barcode.
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Ouput is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

%package -n %{develname}
Summary:	GNU barcode files for development
Group:		Development/Other
Obsoletes:	%{libname}-devel
Provides:	%{name}-devel

%description -n %{develname}
This is GNU-barcode.
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Ouput is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

This package contain the C header, the static library and man page
for development.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure2_5x
%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%post
%_install_info %name

%postun
%_remove_install_info %name

%files
%defattr(-, root, root)
%doc COPYING ChangeLog README TODO doc/*.pdf doc/*.ps
%{_bindir}/barcode
%{_datadir}/info/*
%{_mandir}/man1/*

%files -n %{develname}
%defattr(-, root, root)
%{_includedir}/barcode.h
%{_libdir}/libbarcode.a
%{_mandir}/man3/*
