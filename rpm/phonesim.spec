# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       phonesim

# >> macros
# << macros

Summary:    Phone simulator.
Version:    1.19.0
Release:    1
Group:      Applications/System
License:    LGPL v2.1
URL:        http://github.com/mer-qa/phonesim
Source0:    %{name}-%{version}.tar.bz2
Source1:    phonesim.conf
Source2:    phonesim.desktop
Source3:    nemomobile.xml
Source4:    phonesim.service
Source5:    ofono-phonesim.conf
Source6:    exec_phonesim
Source100:  phonesim.yaml
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  desktop-file-utils

%description
%{summary}.

%package configs-mer
Summary:    Package to provide default configs for connman
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-configs

%description configs-mer
This package provides default configs for connman, such as
FallbackTimeservers.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install
mkdir -p %{buildroot}%{_sysconfdir}/ofono/
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/ofono/
mkdir -p %{buildroot}%{_datadir}/applications/
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/phonesim/
cp -a %{SOURCE3} %{buildroot}%{_datadir}/phonesim/
mkdir -p %{buildroot}%{_libdir}/systemd/user/
cp -a %{SOURCE4} %{buildroot}%{_libdir}/systemd/user/
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d/
cp -a %{SOURCE5} %{buildroot}%{_sysconfdir}/dbus-1/system.d/
mkdir -p %{buildroot}%{_datadir}/phonesim/
cp -a %{SOURCE6} %{buildroot}%{_datadir}/phonesim/


# >> install post
chmod 755 %{buildroot}%{_datadir}/phonesim/exec_phonesim
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/phonesim
%{_datadir}/phonesim/default.xml
%{_datadir}/phonesim/exec_phonesim
%config(noreplace) %{_sysconfdir}/ofono/phonesim.conf
%{_datadir}/applications/phonesim.desktop
# >> files
# << files

%files configs-mer
%defattr(-,root,root,-)
%{_datadir}/phonesim/nemomobile.xml
%{_sysconfdir}/ofono/phonesim.conf
%{_libdir}/systemd/user/phonesim.service
%{_sysconfdir}/dbus-1/system.d/ofono-phonesim.conf
# >> files configs-mer
# << files configs-mer