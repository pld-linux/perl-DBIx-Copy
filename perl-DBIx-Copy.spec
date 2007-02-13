#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	Copy
Summary:	DBIx::Copy Perl module - for copying database content from one db to another
Summary(pl.UTF-8):	Moduł Perla DBIx::Copy - do kopiowania zawartości jednej bazy danych do innej
Name:		perl-DBIx-Copy
Version:	0.02
Release:	4
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e453a98258a27fe6704811d075746862
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For copying a DB.  Future versions might handle mirroring as well,
but it's generally better if the source might send over a transaction
log somehow.

%description -l pl.UTF-8
Moduł służy do kopiowania baz danych. Być może przyszłe wersje będą
obsługiwały także mirroring, ale lepiej, jeśli źródło może wysyłać log
transakcji.

%prep
%setup -q -n %{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
