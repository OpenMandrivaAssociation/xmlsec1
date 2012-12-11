%define major 1

%define libname %mklibname xmlsec1_ %{major}
%define libname_devel %mklibname -d xmlsec1

%define libname_gnutls %mklibname xmlsec1-gnutls %{major}
%define libname_nss %mklibname xmlsec1-nss %{major}
%define libname_openssl %mklibname xmlsec1-openssl %{major}
%define libname_gcrypt %mklibname xmlsec1-gcrypt %{major}

Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Name: xmlsec1
Version: 1.2.18
Release: 2
License: MIT
Group: Development/C
URL: http://www.aleksey.com/xmlsec
Source0: http://www.aleksey.com/xmlsec/download/%{name}-%{version}.tar.gz
Patch1: xmlsec1-1.2.16-linkage.patch
BuildRequires: gnutls-devel
BuildRequires: libgcrypt-devel
BuildRequires: libxml2-devel >= 2.7.4
BuildRequires: libxslt-devel >= 1.0.20
BuildRequires: nss-devel
BuildRequires: openssl-devel >= 0.9.6
BuildRequires: libtool-devel

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package -n %{libname}
Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Group: Development/C
Obsoletes: %{_lib}xmlsec1-1 < 1.2.16

%description -n %{libname}
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package -n %{libname_devel}
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support
Group: Development/C
Requires: %{libname} = %{version}
Requires: %{libname_openssl} = %{version}
Requires: %{libname_gnutls} = %{version}
Requires: %{libname_nss} = %{version}
Requires: %{libname_gcrypt} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xmlsec1-gnutls-devel < 1.2.16
Obsoletes: %{_lib}xmlsec1-nss-devel < 1.2.16
Obsoletes: %{_lib}xmlsec1-openssl-devel < 1.2.16

%description -n %{libname_devel}
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package -n %{libname_openssl}
Summary: OpenSSL crypto plugin for XML Security Library
Group: Development/C

%description -n %{libname_openssl}
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library

%package -n %{libname_nss}
Summary: NSS crypto plugin for XML Security Library
Group: Development/C

%description -n %{libname_nss}
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package -n %{libname_gnutls}
Summary: Gnutls crypto plugin for XML Security Library
Group: Development/C

%description -n %{libname_gnutls}
gnutls plugin for XML Security Library provides gnutls based crypto services
for the xmlsec library

%package -n %{libname_gcrypt}
Summary: Gcrypt crypto plugin for XML Security Library
Group: Development/C

%description -n %{libname_gcrypt}
gcrypt plugin for XML Security Library provides gcrypt based crypto services
for the xmlsec library

%prep
%setup -q
%patch1 -p1

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc %{_mandir}/man1/xmlsec1.1*
%{_bindir}/xmlsec1

%files -n %{libname}
%{_libdir}/libxmlsec1.so.%{major}*

%files -n %{libname_devel}
%doc AUTHORS HACKING ChangeLog NEWS README Copyright
%doc %{_mandir}/man1/xmlsec1-config.1*
%{_bindir}/xmlsec1-config
%{_includedir}/xmlsec1
%{_datadir}/aclocal/xmlsec1.m4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libexecdir}/xmlsec1Conf.sh
%{_docdir}/xmlsec1/*

%files -n %{libname_openssl}
%{_libdir}/libxmlsec1-openssl.so.%{major}*

%files -n %{libname_nss}
%{_libdir}/libxmlsec1-nss.so.%{major}*

%files -n %{libname_gnutls}
%{_libdir}/libxmlsec1-gnutls.so.%{major}*

%files -n %{libname_gcrypt}
%{_libdir}/libxmlsec1-gcrypt.so.%{major}*


%changelog
* Fri Jan 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.18-2
+ Revision: 760706
- removed la files from 2011

* Fri Jan 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.18-2
+ Revision: 760695
- rebuild

* Thu May 12 2011 Funda Wang <fwang@mandriva.org> 1.2.18-1
+ Revision: 673698
- update to new version 1.2.18

* Sun Apr 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.17-1
+ Revision: 649995
- 1.2.17

* Sun Oct 03 2010 Funda Wang <fwang@mandriva.org> 1.2.16-1mdv2011.0
+ Revision: 582711
- modify lib name according to our policy
- New version 1.2.16 (merge all devel packages into one)

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 1.2.14-3mdv2010.1
+ Revision: 536658
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.14-2mdv2010.1
+ Revision: 511664
- rebuilt against openssl-0.9.8m

* Sun Dec 06 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.14-1mdv2010.1
+ Revision: 474141
- 1.2.14 (fixes CVE-2009-3736)
- rediff patches

* Mon Nov 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.13-2mdv2010.1
+ Revision: 471767
- P2: security fix for CVE-2009-3637 (eugeni)

* Sat Oct 10 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.13-1mdv2010.0
+ Revision: 456540
- 1.2.13
- rediffed 2/2 patches

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 1.2.11-1mdv2010.0
+ Revision: 381490
- New version 1.2.11
- build with latest gnutls 2.8

* Fri Nov 21 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.10-8mdv2009.1
+ Revision: 305428
- rebuild to get rid of 'rpmlib(PayloadIsLzma) <= 4.4.2.2-1' dependency

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-7mdv2009.0
+ Revision: 226068
- rebuild
- fix summary-not-capitalized

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 22 2008 Funda Wang <fwang@mandriva.org> 1.2.10-6mdv2008.1
+ Revision: 156357
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Mon Jul 02 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.2.10-5mdv2008.0
+ Revision: 47090
- Fix regexp so match 64bit requires too

* Mon Jul 02 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.2.10-4mdv2008.0
+ Revision: 47085
- Added devel provides for inter-arch stuff.

* Tue Jun 26 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.2.10-3mdv2008.0
+ Revision: 44766
- There are no devel() provides for libnss3 libs.

* Tue Jun 26 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.2.10-2mdv2008.0
+ Revision: 44753
- Added missing buildrequires to gnutls-devel
- Fix requires.
- Import xmlsec1

