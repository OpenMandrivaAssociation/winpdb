%define name	winpdb
%define version 1.2.2
%define release %mkrel 1

Summary: An advanced Python debugger
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: 	 Development/Python
Url:   	 http://www.digitalpeers.com/pythondebugger/ 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires:  python, wxPython >= 2.6.0
BuildRequires: python-devel

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
%__mkdir -p %{buildroot}/%{_menudir}
%__mkdir -p %{buildroot}/{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
%__python setup.py install --skip-build --root=%{buildroot}

%__cat << EOF > %{buildroot}/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/winpdb" icon="%{name}.png" \
needs="X11" section="More Applications/Development/Tools" title="%{name}" \
longtitle="An advanced Python debugger" \
xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc PKG-INFO README.txt
%{_bindir}/*
%{python_sitelib}/*
%{_datadir}/applications/*.desktop
%{_menudir}/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


