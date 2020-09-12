Name:      g810-led
Summary:   Linux led controller for Logitech Keyboards
Version:   0.4.2
Release:   2%{?dist}
License:   GPLv3
URL:       https://github.com/MatMoul/g810-led
Source0:   https://github.com/MatMoul/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 bin/%{name} %{buildroot}%{_bindir}
ln -s %{name} %{buildroot}%{_bindir}/g213-led
ln -s %{name} %{buildroot}%{_bindir}/g410-led
ln -s %{name} %{buildroot}%{_bindir}/g413-led
ln -s %{name} %{buildroot}%{_bindir}/g512-led
ln -s %{name} %{buildroot}%{_bindir}/g513-led
ln -s %{name} %{buildroot}%{_bindir}/g610-led
ln -s %{name} %{buildroot}%{_bindir}/g910-led
ln -s %{name} %{buildroot}%{_bindir}/gpro-led

install -m 0755 -d %{buildroot}%{_udevrulesdir}
install -m 0644 udev/%{name}.rules %{buildroot}%{_udevrulesdir}/95-%{name}.rules

install -m 0755 -d %{buildroot}%{_unitdir}
install -m 0644 systemd/%{name}.service %{buildroot}%{_unitdir}
install -m 0644 systemd/%{name}-reboot.service %{buildroot}%{_unitdir}

install -m 0755 -d %{buildroot}%{_docdir}/%{name}/sample_profiles
install -m 0644 sample_profiles/* %{buildroot}%{_docdir}/%{name}/sample_profiles

install -m 0755 -d %{buildroot}%{_docdir}/%{name}/examples
install -m 0644 sample_effects/bash/k2000 %{buildroot}%{_docdir}/%{name}/examples/k2000.bash
install -m 0644 sample_effects/python/k2000 %{buildroot}%{_docdir}/%{name}/examples/k2000.py

install -m 0755 -d %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 sample_profiles/group_keys %{buildroot}%{_sysconfdir}/%{name}/profile
install -m 0644 sample_profiles/all_blue   %{buildroot}%{_sysconfdir}/%{name}/reboot


%post
%systemd_post %{name}-reboot.service
%systemd_post %{name}.service

%preun
%systemd_preun %{name}-reboot.service
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}-reboot.service
%systemd_postun %{name}.service


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md LICENSE INSTALL.md PROFILES.md CONTRIBUTING.md CONTRIBUTORS.md
%doc %{_docdir}/%{name}/sample_profiles
%doc %{_docdir}/%{name}/examples
%{_bindir}/g810-led
%{_bindir}/g213-led
%{_bindir}/g410-led
%{_bindir}/g413-led
%{_bindir}/g512-led
%{_bindir}/g513-led
%{_bindir}/g610-led
%{_bindir}/g910-led
%{_bindir}/gpro-led
%{_udevrulesdir}/95-%{name}.rules
%{_unitdir}/%{name}-reboot.service
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Sat Sep 12 2020 João Carlos Mendes Luís <dioni21@github.com> - 0.4.2-2
- LSBize distro files
- Add g810-led.service

* Thu May 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.4.2-1
- Update to 0.4.2

* Thu May 07 2020 Lars Kiesow <lkiesow@uos.de> - 0.4.1-1
- Update to 0.4.1

* Wed Apr 29 2020 Lars Kiesow <lkiesow@uos.de> - 0.4.0-1
- Update to 0.4.0

* Sun Sep 22 2019 Lars Kiesow <lkiesow@uos.de> - 0.3.9-1
- Update to 0.3.9

* Thu Aug 29 2019 Lars Kiesow <lkiesow@uos.de> - 0.3.8-1
- Update to 0.3.8

* Wed Aug 21 2019 Lars Kiesow <lkiesow@uos.de> - 0.3.7-1
- Update to 0.3.7

* Wed Oct 31 2018 Lars Kiesow <lkiesow@uos.de> - 0.2.8-1
- Initial packaging
