%define	module	Catalyst-Model-DBIC
%define name	perl-%{module}
%define	modprefix Catalyst

%define version 0.15

%define	rel	1
%define release %mkrel %{rel}

Summary:	Catalyst DBI Model Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl-DBIx-Class
BuildRequires:	perl-DBIx-Class-Loader
BuildRequires:	perl(Class::Accessor::Chained::Fast)
Requires:	perl(Class::Accessor::Chained::Fast)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This is the DBIC model class for Catalyst. It is nothing more than a
simple wrapper for DBIx.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


