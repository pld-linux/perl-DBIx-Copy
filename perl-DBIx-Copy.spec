#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Copy
Summary:	DBIx::Copy Perl module - for copying database content from one db to another
Summary(pl):	Modu³ Perla DBIx::Copy - do kopiowania zawarto¶ci jednej bazy danych do innej
Name:		perl-DBIx-Copy
Version:	0.02
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e453a98258a27fe6704811d075746862
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For copying a DB.  Future versions might handle mirroring as well,
but it's generally better if the source might send over a transaction
log somehow.

%description -l pl
Modu³ s³u¿y do kopiowania baz danych. Byæ mo¿e przysz³e wersje bêd±
obs³ugiwa³y tak¿e mirroring, ale lepiej, je¶li ¼ród³o mo¿e wysy³aæ log
transakcji.

%prep
%setup -q -n %{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
