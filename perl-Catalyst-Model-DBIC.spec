%define	upstream_name	 Catalyst-Model-DBIC
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Catalyst DBI Model Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl-DBIx-Class
BuildRequires:	perl-DBIx-Class-Loader
BuildRequires:	perl(Class::Accessor::Chained::Fast)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(Class::Accessor::Chained::Fast)

%description
This is the DBIC model class for Catalyst. It is nothing more than a
simple wrapper for DBIx.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
