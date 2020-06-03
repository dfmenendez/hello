%global pkg_name	hello
%global pkg_cmp_name	%{getenv:LMOD_FAMILY_COMPILER}
%global pkg_cmp_ver	%(basename `echo %{getenv:MODULEPATH} | sed -e 's/:/\\n/g' | grep Compiler`)

Version:	2.9
Name:		%{pkg_name}%{version}-%{pkg_cmp_name}%{pkg_cmp_ver}
Release:	0%{?dist}
Summary:	The GNU Hello World program

License:	GPL
URL:		https://www.gnu.org/software/hello
Source0:	http://ftp.gnu.org/gnu/hello/%{pkg_name}-%{version}.tar.gz

#BuildRequires:
#Requires:

%description
The GNU Hello program produces a familiar, friendly greeting. Yes, this is
another implementation of the classic program that prints "Hello, world!" when
you run it.

However, unlike the minimal version often seen, GNU Hello processes its argument
list to modify its behavior, supports greetings in many languages, and so on.
The primary purpose of GNU Hello is to demonstrate how to write other programs
that do these things; it serves as a model for GNU coding standards and GNU
maintainer practices.

%global _basedir	/opt/packages
%global _prefix		%{_basedir}/%{pkg_name}/%{version}_%{pkg_cmp_name}-%{pkg_cmp_ver}
# On RHEL6 redefine _mandir and _infodir based on GNU Coding Standards (GCS)
%global _datarootdir	%{_prefix}/share
%global _infodir	%{_datarootdir}/info
%global _mandir		%{_datarootdir}/man


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%defattr(-,root,root,-)
%{_prefix}
%docdir %{_infodir}
%docdir %{_mandir}



%changelog
