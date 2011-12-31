%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-kid
Version:        0.9.6
Release:        5.1%{?dist}
Summary:        Kid - A simple and pythonic XML template language

Group:          Applications/Publishing
License:        MIT
URL:            http://www.kid-templating.org/
Source0:        http://www.kid-templating.org/dist/%{version}/kid-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools-devel
BuildRequires:  python-docutils


%description
Kid is a simple Python based template language for generating and
transforming XML vocabularies. Templates are compiled to native Python 
byte-code and may be imported and used like normal Python modules.


%prep
%setup -q -n kid-%{version}


%build
%{__python} setup.py build
pushd doc
sed -i -e 's|rst2html\.py|rst2html|' makefile
make
popd


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT \
    --single-version-externally-managed
rm -rf $RPM_BUILD_ROOT%{python_sitelib}/kid/test
rm -f $RPM_BUILD_ROOT%{python_sitelib}/*egg-info/requires.txt
# Avoid requiring setuptools
chmod 0755 $RPM_BUILD_ROOT%{python_sitelib}/kid/{run,compile}.py
rm -f $RPM_BUILD_ROOT%{_bindir}/*
ln -s ../..%{python_sitelib}/kid/run.py $RPM_BUILD_ROOT%{_bindir}/kid
ln -s ../..%{python_sitelib}/kid/compile.py $RPM_BUILD_ROOT%{_bindir}/kidc


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README doc/*.txt doc/*.css doc/*.html test
%{python_sitelib}/kid*
%{_bindir}/*


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.9.6-5.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.6-3
- Rebuild for Python 2.6

* Tue Aug 28 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.6-2
- BR: python-setuptools-devel
- Drop explicit BR: python-devel

* Fri Aug 17 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.6-1
- Upstream 0.9.6

* Sun Jan 28 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.5-1
- Upstream 0.9.5
- Drop the py-def patch

* Tue Jan 02 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.4-2
- Add hotfix for broken py-def (#220843)
- Simplify kid and kidc to not require setuptools to run (#220844)

* Sun Dec 17 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.4-1
- Version 0.9.4
- Ghostbusting

* Sun Jul 23 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.3-1
- Version 0.9.3
- Adjusting urls to point to kid-templating.org

* Tue Jun 27 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.2-1
- Version 0.9.2
- BR python-setuptools >= 0.6a11

* Tue May 23 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.1-3
- Fix 'elementtree requried' regression

* Sat May 20 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.1-2
- Update project URL

* Fri May 19 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.1-1
- Version 0.9.1

* Mon Feb 27 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9-1
- Version 0.9
- Switch to using setuptools.
- Handle .egg data.
- Don't list python-abi namely -- FC4 and above does it automatically.

* Fri Dec 02 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.8-1
- Version 0.8

* Fri Nov 11 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.7.1-2
- Rebuild.

* Thu Nov 10 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.7.1-1
- Version 0.7.1
- Avoid setuptools using a patch to use standard distutils
- Avoid cruft in doc dir

* Mon Jun 13 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.6.4-1
- Version 0.6.4
- Disttagging

* Sat Apr 16 2005 Seth Vidal <skvidal at phy.duke.edu> 0.6.3-2
- BuildRequires python-elementtree

* Tue Mar 29 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.6.3-2
- Add docs and list files instead of using INSTALLED_FILES (safer)
- Trim description a little
- Require python-abi
- BuildRequire python-devel
- Use python_sitelib
- Remove test directory from site_packages
- Use ghosting for .pyo

* Mon Mar 14 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.6.3-1
- Version 0.6.3

* Thu Mar 10 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.6.2-1
- Initial build in Fedora Extras format.
