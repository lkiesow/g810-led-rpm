Name:      g810-led
Summary:   Linux led controller for Logitech Keyboards
Version:   0.3.8
Release:   1%{?dist}
License:   GPLv3
URL:       https://github.com/MatMoul/g810-led
Source0:   https://github.com/MatMoul/%{name}/archive/v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%{?systemd_requires}
BuildRequires: systemd
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: hidapi-devel


%description
Linux led controller for Logitech G213, G410, G413, G512, G513, G610, G810, G910
and GPRO Keyboards.


%prep
%setup -q


%build
make debug


%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d \
  %{buildroot}%{_bindir} \
  %{buildroot}%{_sysconfdir}/%{name}/samples \
  %{buildroot}%{_udevrulesdir} \
  %{buildroot}%{_unitdir}
install -p -m 755 bin/%{name} %{buildroot}%{_bindir}
for alias in 213 410 413 512 513 610 910 pro; do
  ln -s %{name} "%{buildroot}%{_bindir}/g${alias}-led"
done
install -p -m 644 sample_profiles/* %{buildroot}%{_sysconfdir}/%{name}/samples
install -p -m 644 udev/%{name}.rules %{buildroot}%{_udevrulesdir}
install -p -D -m 0644 systemd/%{name}-reboot.service %{buildroot}%{_unitdir}


%post
%systemd_post %{name}-reboot.service

%preun
%systemd_preun %{name}-reboot.service

%postun
%systemd_postun %{name}-reboot.service


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md LICENSE INSTALL.md
%{_bindir}/g???-led
%{_udevrulesdir}/%{name}.rules
%{_unitdir}/%{name}-reboot.service
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Thu Aug 29 2019 Lars Kiesow <lkiesow@uos.de> - 0.3.8-1
- Update to 0.3.8

* Wed Aug 21 2019 Lars Kiesow <lkiesow@uos.de> - 0.3.7-1
- Update to 0.3.7

* Wed Oct 31 2018 Lars Kiesow <lkiesow@uos.de> - 0.2.8-1
- Initial packaging
