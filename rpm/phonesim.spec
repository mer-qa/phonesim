Name:       phonesim
Summary:    Phone simulator.
Version:    1.20.0
Release:    1
License:    GPLv2
URL:        http://github.com/mer-qa/phonesim
Source0:    %{name}-%{version}.tar.bz2
Source1:    phonesim.conf
Source2:    phonesim.desktop
Source4:    phonesim.service
Source6:    exec_phonesim
Requires:   blts-tools
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  desktop-file-utils

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
%make_build

%install
%qmake5_install
mkdir -p %{buildroot}%{_sysconfdir}/ofono/
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/ofono/
mkdir -p %{buildroot}%{_datadir}/applications/
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_userunitdir}
cp -a %{SOURCE4} %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_datadir}/phonesim/
cp -a %{SOURCE6} %{buildroot}%{_datadir}/phonesim/

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%{_bindir}/phonesim
%dir %{_datadir}/phonesim
%{_datadir}/phonesim/default.xml
%{_datadir}/phonesim/GSMSpecification.xml
%attr(755, root, root) %{_datadir}/phonesim/exec_phonesim
%{_datadir}/applications/phonesim.desktop
%{_userunitdir}/phonesim.service
%{_sysconfdir}/ofono/phonesim.conf
