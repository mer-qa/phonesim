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
Source6:    exec_phonesim
Requires:   %{name}-configs
Requires:   blts-tools
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
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
mkdir -p %{buildroot}%{_datadir}/phonesim/
cp -a %{SOURCE6} %{buildroot}%{_datadir}/phonesim/

chmod 755 %{buildroot}%{_datadir}/phonesim/exec_phonesim

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

# Remove a mistakenly created directory
%pre
if [ "$1" -eq 2 ]
then
    rm -rf %{_datadir}/phonesim/default.xml
fi

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/phonesim
%dir %{_datadir}/phonesim
%{_datadir}/phonesim/default.xml
%{_datadir}/phonesim/GSMSpecification.xml
%{_datadir}/phonesim/exec_phonesim
%{_datadir}/applications/phonesim.desktop

%files configs-mer
%defattr(-,root,root,-)
%{_datadir}/phonesim/nemomobile.xml
%{_sysconfdir}/ofono/phonesim.conf
%{_userunitdir}/phonesim.service
