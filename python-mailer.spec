%global _empty_manifest_terminate_build 0
Name:		python-mailer
Version:	0.8.1
Release:	1
Summary:	A module to send email simply in Python
License:	MIT
URL:		https://bitbucket.org/ginstrom/mailer
Source0:	https://files.pythonhosted.org/packages/30/e7/c3a932fc03ab95c96ff911d8ee3e89b937205596a5c1f00849401a2468e0/mailer-0.8.1.zip
BuildArch:	noarch

%description
A module to send email simply in Python

%package -n python3-mailer
Summary:	A module to send email simply in Python
Provides:	python-mailer
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr

%description -n python3-mailer
A module to send email simply in Python

%package help
Summary:	Development documents and examples for mailer
Provides:	python3-mailer-doc

%description help
A module to send email simply in Python

%prep
%autosetup -n mailer-0.8.1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-mailer -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Jun 17 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
