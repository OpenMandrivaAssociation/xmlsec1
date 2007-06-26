%define major 1

%define libname %mklibname xmlsec1- %{major}
%define libname_devel %mklibname -d xmlsec1

%define libname_gnutls %mklibname xmlsec1-gnutls %{major}
%define libname_gnutls_devel %mklibname -d xmlsec1-gnutls

%define libname_nss %mklibname xmlsec1-nss %{major}
%define libname_nss_devel %mklibname -d xmlsec1-nss

%define libname_openssl %mklibname xmlsec1-openssl %{major}
%define libname_openssl_devel %mklibname -d xmlsec1-openssl

Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Name: xmlsec1
Version: 1.2.10
Release: %mkrel 1
License: MIT
Group: Development/C
Source: ftp://ftp.aleksey.com/pub/xmlsec/releases/xmlsec1-%{version}.tar.gz
BuildRoot: %{_tmppath}/xmlsec1-%{version}-root
URL: http://www.aleksey.com/xmlsec
Requires: libxml2 >= 2.6.12
Requires: libxslt >= 1.0.20
BuildRequires: libxml2-devel >= 2.6.12
BuildRequires: libxslt-devel >= 1.0.20
BuildRequires: openssl-devel >= 0.9.6
BuildRequires: nss-devel

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package -n %{libname}
Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Group: Development/C

%description -n %{libname}
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package -n %{libname_devel}
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support.
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: libxml2-devel >= 2.6.12
Requires: libxslt-devel >= 1.0.20
Requires: openssl-devel >= 0.9.6
Requires: zlib-devel

%description -n %{libname_devel}
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package -n %{libname_openssl}
Summary: OpenSSL crypto plugin for XML Security Library
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.6.12
Requires: libxslt >= 1.0.20
Requires: openssl >= 0.9.6

%description -n %{libname_openssl}
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library

%package -n %{libname_openssl_devel}
Summary: OpenSSL crypto plugin for XML Security Library
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: xmlsec1-devel = %{version}
Requires: xmlsec1-openssl = %{version}
Requires: libxml2-devel >= 2.6.12
Requires: libxslt-devel >= 1.0.20
Requires: openssl >= 0.9.6
Requires: openssl-devel >= 0.9.6

%description -n %{libname_openssl_devel}
Libraries, includes, etc. for developing XML Security applications with OpenSSL

%package -n %{libname_nss}
Summary: NSS crypto plugin for XML Security Library
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.6.12
Requires: libxslt >= 1.0.20
#Requires: mozilla-nss >= 1.4

%description -n %{libname_nss}
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package -n %{libname_nss_devel}
Summary: NSS crypto plugin for XML Security Library
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: xmlsec1-devel = %{version}
Requires: xmlsec1-nss = %{version}
Requires: libxml2-devel >= 2.6.12
Requires: libxslt-devel >= 1.0.20
#Requires: mozilla-nss-devel >= 1.4

%description -n %{libname_nss_devel}
Libraries, includes, etc. for developing XML Security applications with NSS

%package -n %{libname_gnutls}
Summary: gnutls crypto plugin for XML Security Library
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: libxml2 >= 2.6.12
Requires: libxslt >= 1.0.20

%description -n %{libname_gnutls}
gnutls plugin for XML Security Library provides gnutls based crypto services
for the xmlsec library

%package -n %{libname_gnutls_devel}
Summary: gnutls crypto plugin for XML Security Library
Group: Development/C
Requires: xmlsec1 = %{version}
Requires: xmlsec1-devel = %{version}
Requires: xmlsec1-gnutls = %{version}
Requires: libxml2-devel >= 2.6.12
Requires: libxslt-devel >= 1.0.20

%description -n %{libname_gnutls_devel}
Libraries, includes, etc. for developing XML Security applications with gnutls.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/usr/include/xmlsec1
mkdir -p %buildroot/usr/lib
mkdir -p %buildroot/usr/man/man1
make install DESTDIR=%buildroot

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README Copyright
%doc %{_mandir}/man1/xmlsec1.1*
%{_bindir}/xmlsec1

%files -n %{libname}
%{_libdir}/libxmlsec1.so.*

%files -n %{libname_devel}
%defattr(-,root,root)
%doc AUTHORS HACKING ChangeLog NEWS README Copyright
%doc %{_mandir}/man1/xmlsec1-config.1*
%{_bindir}/xmlsec1-config
%{_includedir}/xmlsec1/xmlsec/*.h
%{_includedir}/xmlsec1/xmlsec/private/*.h
%{_libdir}/libxmlsec1.*a
%{_libdir}/libxmlsec1.so
%{_libdir}/pkgconfig/xmlsec1.pc
%{_libdir}/xmlsec1Conf.sh
%{_docdir}/xmlsec1/*

%files -n %{libname_openssl}
%defattr(-,root,root)
%{_libdir}/libxmlsec1-openssl.so.*

%files -n %{libname_openssl_devel}
%defattr(-,root,root)
%{_includedir}/xmlsec1/xmlsec/openssl/*.h
%{_libdir}/libxmlsec1-openssl.*a
%{_libdir}/libxmlsec1-openssl.so
%{_libdir}/pkgconfig/xmlsec1-openssl.pc

%files -n %{libname_nss}
%defattr(-,root,root)
%{_libdir}/libxmlsec1-nss.so.*

%files -n %{libname_nss_devel}
%defattr(-,root,root)
%{_includedir}/xmlsec1/xmlsec/nss/*.h
%{_libdir}/libxmlsec1-nss.*a
%{_libdir}/libxmlsec1-nss.so
%{_libdir}/pkgconfig/xmlsec1-nss.pc

%files -n %{libname_gnutls}
%defattr(-,root,root)
%{_libdir}/libxmlsec1-gnutls.so.*

%files -n %{libname_gnutls_devel}
%defattr(-,root,root)
%{_includedir}/xmlsec1/xmlsec/gnutls/*.h
%{_libdir}/libxmlsec1-gnutls.*a
%{_libdir}/libxmlsec1-gnutls.so
%{_libdir}/pkgconfig/xmlsec1-gnutls.pc
