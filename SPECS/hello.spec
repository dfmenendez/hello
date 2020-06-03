Name:		hello
Version:	2.9
Release:	0%{?dist}
Summary:	The GNU Hello World program

License:	GPL
URL:		https://www.gnu.org/software/hello
Source0:	http://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz

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
%global _prefix		%{_basedir}/%{name}/%{version}
# On RHEL6 redefine _mandir and _infodir based on GNU Coding Standards (GCS)
%global _datarootdir	%{_prefix}/share
%global _infodir	%{_datarootdir}/info
%global _mandir		%{_datarootdir}/man


%prep
tar xzf %{SOURCE0}


%build
cd %{name}-%{version}
./configure --prefix=%{_prefix}
make %{?_smp_mflags}


%install
cd %{name}-%{version}
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%{_prefix}
%docdir %{_infodir}
%docdir %{_mandir}



%changelog
