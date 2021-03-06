%global pkg_name	hello
%global pkg_cmp_name	%{getenv:LMOD_FAMILY_COMPILER}
%global pkg_cmp_ver	%(basename `echo %{getenv:MODULEPATH} | sed -e 's/:/\\n/g' | grep Compiler`)
%global pkg_summ	The GNU Hello World program
%global pkg_desc	The GNU Hello program produces a familiar, friendly greeting. Yes, this is\
another implementation of the classic program that prints "Hello, world!" when\
you run it.\
\
However, unlike the minimal version often seen, GNU Hello processes its argument\
list to modify its behavior, supports greetings in many languages, and so on.\
The primary purpose of GNU Hello is to demonstrate how to write other programs\
that do these things; it serves as a model for GNU coding standards and GNU\
maintainer practices.

Version:	2.10
Name:		%{pkg_name}%{version}-%{pkg_cmp_name}%{pkg_cmp_ver}
Release:	1%{?dist}
Summary:	%{pkg_summ}

License:	GPL
URL:		https://www.gnu.org/software/hello
Source0:	http://ftp.gnu.org/gnu/hello/%{pkg_name}-%{version}.tar.gz
Source1:	%{pkg_name}.lua.in

#BuildRequires:
#Requires:
Provides:	%{pkg_name} = %{version}

%description
%{pkg_desc}

# Preamble for Lua modulefile (Lmod) subpackage
%package lmod
Summary:        %{pkg_name}/%{version} modulefile
Requires:	%{name}
BuildArch:	noarch

%description lmod
This package contains the %{pkg_name}/%{version} modulefile.

%global _basedir	/opt/packages
%global _prefix		%{_basedir}/%{pkg_name}/%{version}_%{pkg_cmp_name}-%{pkg_cmp_ver}
%global _moddir		%{_basedir}/modulefiles/Compiler/%{pkg_cmp_name}/%{pkg_cmp_ver}/%{pkg_name}
# On RHEL6 redefine _mandir and _infodir based on GNU Coding Standards (GCS)
%global _datarootdir	%{_prefix}/share
%global _infodir	%{_datarootdir}/info
%global _mandir		%{_datarootdir}/man


%prep
%setup -q -n %{pkg_name}-%{version}

# Inject spec file variables into Lua modulefile (Lmod)
cat << EOF > %{version}.lua
%include %{SOURCE1}
EOF


%build
%configure
make %{?_smp_mflags}


%install
%make_install

# Install Lua modulefile (Lmod)
install -m 755 -d %{buildroot}%{_moddir}
install -m 0644 %{version}.lua %{buildroot}%{_moddir}


%files
%defattr(-,root,root,-)
%{_prefix}
%docdir %{_infodir}
%docdir %{_mandir}

# Manifest for Lua module file
%files lmod
%{_moddir}/%{version}.lua



%changelog
* Wed Jun 03 2020 Diego Menéndez <dmenendez@psu.edu> - 2.10-1
- New upstream software version.

* Wed Jun 03 2020 Diego Menéndez <dmenendez@psu.edu> - 2.9-1
- Enable simultaneous installation of multiple versions built with different
  compilers or compiler versions.
- Add optional modulefile subpackage dependent on main package to avoid leaving
  an orphaned environment module upon uninstalling main package.
