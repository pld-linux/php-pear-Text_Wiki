%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Wiki
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - parsing and rendering rules for Wiki markup in structured text
Summary(pl.UTF-8):   %{_pearname} - reguły analizy i renderowania dla znaczników Wiki w tekście
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	51fa387ef59ff2feab38ad087820faa3
URL:		http://pear.php.net/package/Text_Wiki/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstracts parsing and rendering rules for Wiki markup in structured
plain text.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa tworzy abstrakcję reguł do analizy i renderowania dla
znaczników Wiki w czystym tekście z odpowiednią strukturą.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
