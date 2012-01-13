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
