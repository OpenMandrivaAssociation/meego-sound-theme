Name: meego-sound-theme
Summary: MeeGo sound theme
Version: 0.5
Release: %mkrel 1
Group: System/Desktop
License: GPLv2
URL: http://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.bz2
BuildRequires: intltool
BuildRequires: gettext
Obsoletes: moblin-sound-theme < 0.5

%description
Description: %{summary}

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root,-)
%doc README
%dir %{_datadir}/sounds/meego
%dir %{_datadir}/sounds/meego/stereo
%{_datadir}/sounds/meego/index.theme
%{_datadir}/sounds/meego/stereo/*.ogg
%{_datadir}/sounds/meego/stereo/*.wav

