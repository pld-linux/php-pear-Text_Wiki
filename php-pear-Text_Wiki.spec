# ToDo:
# - pl-ize me (summary/description)
# - en summary shouldn't be the same as description
%include	/usr/lib/rpm/macros.php
%define         _class          Text
%define         _subclass     	Wiki
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Abstracts parsing and rendering rules for Wiki markup in structured plain text.
#Summary(pl):	%{_pearname} -
Name:		php-pear-%{_pearname}
Version:	0.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2a0b6e7dd0568e0bc9246ebefe8f48e8
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstracts parsing and rendering rules for Wiki markup in structured
plain text.

This class has in PEAR status: %{_status}.

#%description -l pl
#
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
#cd %{_pearname}-%{version}
%patch0 -p0

# it looks like %%doc gets confused when it has to process file containing
# space in its name
mv %{_pearname}-%{version}/%{_pearname}/docs/{"free links.wiki.txt",free_links.wiki.txt}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/rules

install %{_pearname}-%{version}/Text_Wiki.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Wiki.php
install %{_pearname}-%{version}/%{_pearname}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Wiki.php
install %{_pearname}-%{version}/%{_pearname}/rules/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_pearname}/{docs,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
