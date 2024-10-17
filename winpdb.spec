%define name	winpdb
%define version 1.4.8
%define release 3

Summary: 	An advanced Python debugger
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.gz
License: 	GPLv2+
Group: 	 	Development/Python
Url:   	 	https://www.winpdb.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:  	python, wxPython >= 2.6.0
BuildRequires: 	python-devel

%description
Winpdb is an advanced Python debugger. It supports smart breakpoints,
multiple threads, namespace modification, embedded debugging, and
encrypted communication, and is up to 20 times faster than pdb.

%prep
%setup -q
sed -i 's/\r//g' README.txt

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}/%{_bindir}
%__mkdir -p %{buildroot}/{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
%__python setup.py install --skip-build --root=%{buildroot}


%__mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=An advanced Python debugger
Exec=%{_bindir}/winpdb
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;X-MandrivaLinux-Development-Tools;
EOF

%__install -m 644 artwork/winpdb-icon-32.png %{buildroot}/%{_iconsdir}/%{name}.png
%__install -m 644 artwork/winpdb-icon-16.png %{buildroot}/%{_miconsdir}/%{name}.png
%__install -m 644 artwork/winpdb-icon-64.png %{buildroot}/%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README.txt
%{_bindir}/*
%{python_sitelib}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 1.4.8-2mdv2011.0
+ Revision: 599642
- rebuild for py2.7

* Mon Aug 23 2010 Lev Givon <lev@mandriva.org> 1.4.8-1mdv2011.0
+ Revision: 572464
- Update to 1.4.8.

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.4.6-2mdv2010.0
+ Revision: 445800
- rebuild

  + Lev Givon <lev@mandriva.org>
    - Update to 1.4.6.

* Mon Feb 16 2009 Lev Givon <lev@mandriva.org> 1.4.4-1mdv2009.1
+ Revision: 340962
- Update to 1.4.4.

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1.4.2-1mdv2009.1
+ Revision: 324526
- Rename

* Sun Oct 12 2008 Lev Givon <lev@mandriva.org> 1.4.0-1mdv2009.1
+ Revision: 292702
- Update to 1.4.0.

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.3.8-2mdv2009.0
+ Revision: 269691
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Apr 13 2008 Lev Givon <lev@mandriva.org> 1.3.8-1mdv2009.0
+ Revision: 192647
- Update to 1.3.8.

* Sun Mar 09 2008 Lev Givon <lev@mandriva.org> 1.3.6-1mdv2008.1
+ Revision: 183167
- Update to 1.3.6.

* Wed Jan 16 2008 Lev Givon <lev@mandriva.org> 1.3.4-1mdv2008.1
+ Revision: 153699
- Update to 1.3.4.

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 07 2007 Lev Givon <lev@mandriva.org> 1.3.2-1mdv2008.1
+ Revision: 116301
- Update to 0.3.2.
- Update tarball to include last minute bug fix.

* Thu Nov 01 2007 Lev Givon <lev@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 104400
- Update to 1.3.0.

* Tue Oct 23 2007 Lev Givon <lev@mandriva.org> 1.2.5-1mdv2008.1
+ Revision: 101541
- Update to 1.2.5.

* Tue Oct 16 2007 Lev Givon <lev@mandriva.org> 1.2.2-2mdv2008.1
+ Revision: 99076
- Patch to support use of xfce terminal.

* Tue Oct 16 2007 Lev Givon <lev@mandriva.org> 1.2.2-1mdv2008.1
+ Revision: 99006
- import winpdb


* Tue Oct 15 2007 Lev Givon <lev@mandriva.org> 1.2.2-1mdv2008.0
- Initial Mandriva package.
