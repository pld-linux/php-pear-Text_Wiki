%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Wiki
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - parsing and rendering rules for Wiki markup in structured text
Summary(pl):	%{_pearname} - regu³y analizy i renderowania dla znaczników Wiki w tek¶cie
Name:		php-pear-%{_pearname}
Version:	0.12.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b51a44ef402a8c09fa46eb984062195d
URL:		http://pear.php.net/package/Text_Wiki/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstracts parsing and rendering rules for Wiki markup in structured
plain text.

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa tworzy abstrakcjê regu³ do analizy i renderowania dla
znaczników Wiki w czystym tek¶cie z odpowiedni± struktur±.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Rule

install %{_pearname}-%{version}/%{_class}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Rule/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Rule

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs/*,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
