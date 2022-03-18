Name:       phonesim
Summary:    Phone simulator.
Version:    1.19.0
Release:    1
License:    GPLv2
URL:        http://github.com/mer-qa/phonesim
Source0:    %{name}-%{version}.tar.bz2
Source1:    phonesim.conf
Source2:    phonesim.desktop
Source3:    nemomobile.xml
Source4:    phonesim.service
Source5:    ofono-phonesim.conf
Source6:    exec_phonesim.privileges
Requires:   %{name}-configs
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  desktop-file-utils

%description
%{summary}.

%package configs-mer
Summary:    Package to provide default configs for connman
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-configs

%description configs-mer
This package provides default configs for connman, such as
FallbackTimeservers.


%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 
make %{?_smp_mflags}

%install
%qmake5_install
mkdir -p %{buildroot}%{_sysconfdir}/ofono/
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/ofono/
mkdir -p %{buildroot}%{_datadir}/applications/
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/phonesim/
cp -a %{SOURCE3} %{buildroot}%{_datadir}/phonesim/
mkdir -p %{buildroot}%{_userunitdir}
cp -a %{SOURCE4} %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d/
cp -a %{SOURCE5} %{buildroot}%{_datadir}/dbus-1/system.d/
mkdir -p %{buildroot}%{_datadir}/mapplauncherd/privileges.d/
cp -a %{SOURCE6} %{buildroot}%{_datadir}/mapplauncherd/privileges.d/

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/phonesim
%dir %{_datadir}/phonesim
%{_datadir}/phonesim/default.xml
%{_libexecdir}/exec_phonesim
%{_datadir}/applications/phonesim.desktop
%{_datadir}/mapplauncherd/privileges.d/exec_phonesim.privileges

%files configs-mer
%defattr(-,root,root,-)
%{_datadir}/phonesim/nemomobile.xml
%{_sysconfdir}/ofono/phonesim.conf
%{_userunitdir}/phonesim.service
%{_datadir}/dbus-1/system.d/ofono-phonesim.conf
