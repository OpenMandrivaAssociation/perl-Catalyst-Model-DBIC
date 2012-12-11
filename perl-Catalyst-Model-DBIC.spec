%define	upstream_name	 Catalyst-Model-DBIC
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst DBI Model Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl-DBIx-Class
BuildRequires:	perl-DBIx-Class-Loader
BuildRequires:	perl(Class::Accessor::Chained::Fast)
BuildArch:	noarch
Requires:	perl(Class::Accessor::Chained::Fast)

%description
This is the DBIC model class for Catalyst. It is nothing more than a
simple wrapper for DBIx.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 680721
- mass rebuild

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 467873
- update to 0.17

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 408940
- rebuild using %%perl_convert_version

* Thu Mar 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.1
+ Revision: 180638
- update to new version 0.16

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Buchan Milne <bgmilne@mandriva.org> 0.15-1mdv2008.0
+ Revision: 24861
- Import perl-Catalyst-Model-DBIC

