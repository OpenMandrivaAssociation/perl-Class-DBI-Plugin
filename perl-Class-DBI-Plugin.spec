%define upstream_name	 Class-DBI-Plugin
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Abstract base class for Class::DBI plugins
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class::DBI::Plugin is an abstract base class for Class::DBI plugins.
Its purpose is to make writing plugins easier. Writers of plugins
should be able to concentrate on the functionality their module
provides, instead of having to deal with the symbol table hackery
involved when writing a plugin module. Only three things must be
remembered:

1 All methods which are to exported are given the "Plugged"
attribute. All other methods are not exported to the plugged-in
class.
2 Method calls which are to be sent to the plugged-in class are
put in the init() method. Examples of these are set_sql(),
add_trigger() and so on.
3 The class parameter for the init() method and the "Plugged"
methods is the plugged-in class, not the plugin class.

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
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 680793
- mass rebuild

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 398796
- rebuild
- using %%perl_convert_version
- fixed license field

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.03-5mdv2009.0
+ Revision: 241181
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-3mdv2008.0
+ Revision: 86097
- rebuild


* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.03-2mdk
- add description

* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.03-1mdk
- initial Mandriva package

