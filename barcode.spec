%define major 0
%define libname	  %mklibname barcode %{major}
%define develname %mklibname barcode -d

Summary:	GNU barcode
Name:		barcode
Version:	0.98
Release:	15
License:	GPLv2+
Group:		Publishing
Source:		ftp://ftp.gnu.org/gnu/barcode/%name-%{version}.tar.bz2
Patch0:		barcode-0.98-fix-str-fmt.patch
Patch1:		barcode-0.98-fix-installation.patch
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
%makeinstall_std

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.98-14mdv2011.0
+ Revision: 610052
- rebuild

* Wed Apr 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.98-13mdv2010.1
+ Revision: 537479
- fix SOURCE
- don't define name, version, release on top of spec
- clean spec

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.98-12mdv2010.0
+ Revision: 436800
- rebuild

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 0.98-11mdv2009.1
+ Revision: 317778
- fix str ftm
- use standard DESTDIR to install
- fix post script

* Tue Aug 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.98-10mdv2009.0
+ Revision: 276155
- apply devel policy
- fix license
- replace old RPM_BUILD_ROOT

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.98-9mdv2009.0
+ Revision: 240437
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.98-7mdv2008.0
+ Revision: 70145
- use %%mkrel


* Tue Apr 05 2005 Marcel Pol <mpol@mandriva.org> 0.98-6mdk
- fix libdir on x86-64

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.98-5mdk
- Libification

* Fri May 14 2004 Marcel Pol <mpol@mandrake.org> 0.98-4mdk
- rebuild

* Wed Apr 16 2003 Marcel Pol <mpol@gmx.net> 0.98-3mdk
- undo previous change, spec-helper does that (thanks thierry)

* Wed Apr 16 2003 Marcel Pol <mpol@gmx.net> 0.98-2mdk
- bzip man and info pages

* Mon Apr 14 2003 Marcel Pol <mpol@gmx.net> 0.98-1mdk
- initial mandrake release

