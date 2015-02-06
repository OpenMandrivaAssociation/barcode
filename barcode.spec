Summary:	GNU barcode
Name:		barcode
Version:	0.99
Release:	2
License:	GPLv2+
Group:		Publishing
Source:		ftp://ftp.gnu.org/gnu/barcode/%name-%{version}.tar.xz
Patch0:		barcode-0.98-fix-str-fmt.patch
URL:		http://gnu.systemy.it/software/barcode

%description
This is GNU-barcode.
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Ouput is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f %{buildroot}/usr/bin/sample

%files
%doc COPYING ChangeLog README TODO
%{_bindir}/barcode
%{_datadir}/info/*
