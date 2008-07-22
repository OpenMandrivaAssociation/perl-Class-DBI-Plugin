%define module	Class-DBI-Plugin
%define name	perl-%{module}
%define version 0.03
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Abstract base class for Class::DBI plugins
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

