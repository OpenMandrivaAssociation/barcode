%define name	barcode
%define version	0.98
%define release	%mkrel 9

%define lib_name_orig %mklibname barcode
%define lib_major 0
%define lib_name %lib_name_orig%lib_major


Summary:	GNU barcode
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Publishing
Source:		ftp://ar.linux.it/pub/barcode/%name-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		http://gnu.systemy.it/software/barcode

%description
This is GNU-barcode.
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Ouput is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

%package -n %lib_name-devel
Summary:	GNU barcode files for development
Group:		Development/Other
Obsoletes:	barcode-devel <= 0.98-4mdk
Provides:	barcode-devel

%description -n %lib_name-devel
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


%build
export -n LANG LINGUAS LC_ALL 
%configure
export -n LANG LINGUAS LC_ALL 
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} \
    LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
    MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    MAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
    INFODIR=$RPM_BUILD_ROOT%{_infodir} install


%post
if [[ -f %{_infodir}/%{name}.info.bz2 ]];then /sbin/install-info %{_infodir}/%{name}.info.bz2 --dir=%{_infodir}/dir;fi

%postun
if [ "$1" = "0" ]; then if [[ -f %{_infodir}/%{name}.info.bz2 ]];then /sbin/install-info %{_infodir}/%{name}.info.bz2 --dir=%{_infodir}/dir --remove ;fi; fi


%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING ChangeLog README TODO doc/*.pdf doc/*.ps
%{_bindir}/barcode
%{_datadir}/info/*
%{_mandir}/man1/*

%files -n %lib_name-devel
%defattr(-, root, root)
%{_includedir}/barcode.h
%{_libdir}/libbarcode.a
%{_mandir}/man3/*

