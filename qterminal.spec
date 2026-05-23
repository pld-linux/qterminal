#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Advanced Qt6-based terminal emulator
Summary(pl.UTF-8):	Zaawansowany, bazujący na Qt6 emulator terminala
Name:		qterminal
Version:	2.4.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/qterminal/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d381d0aad8d9eb44368c5ddcd22dade5
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kp6-layer-shell-qt-devel >= 6.0.0
BuildRequires:	libcanberra-devel
BuildRequires:	lxqt-build-tools >= 2.4.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	qtermwidget-devel >= 2.4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced Qt6-based terminal emulator with many useful bells and
whistles.

%description -l pl.UTF-8
Zaawansowany emulator terminala oparty na Qt6, wyposażony w wiele
przydatnych funkcji.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qterminal
%{_desktopdir}/qterminal.desktop
%{_iconsdir}/hicolor/64x64/apps/qterminal.png
%{_desktopdir}/qterminal-drop.desktop
%{_datadir}/metainfo/qterminal.metainfo.xml
%dir %{_datadir}/qterminal
# required for the lang files
%dir %{_datadir}/qterminal/translations
%{_datadir}/qterminal/qterminal_bookmarks_example.xml
