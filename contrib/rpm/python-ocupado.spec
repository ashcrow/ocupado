# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-ocupado
Version:        0.0.2
Release:        1%{?dist}
Summary:        Plug-in based user checking tool

License:        AGPLv3+
URL:            https://github.com/ashcrow/ocupado
Source0:        ocupado-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%description
Plug-in based tool which checks a user data source against an
authoritative source and alerts on any anomalies.

%prep
%setup -qc
mv ocupado-%{version} python2

%build
pushd python2
%{__python2} setup.py build
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd python2
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

%check
pushd python2
%{__python2} setup.py test
popd

%files
%doc python2/AUTHORS python2/COPYING python2/LICENSE python2/README.md python2/docs/*rst python2/docs/api/
# For noarch packages: sitelib
%{python2_sitelib}/*
%{_bindir}/ocupado

%changelog
* Mon Aug 31 2015 Steve Milner <stevem@gnulinux.net> - 0.0.2-1
- smtp_subject support added.
- Enhanced unittesting.

* Wed Jul 22 2015 Steve Milner <stevem@gnulinux.net> - 0.0.1-1
- Initial spec.
