#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	qterminal
Name:		qterminal
Version:	0.7.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/qterminal/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	566ba64cbec739b94b0ba2bc9cca2880
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.11
BuildRequires:	glib2-devel
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	qtermwidget-devel >= 0.7.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qterminal

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qterminal
%{_desktopdir}/qterminal.desktop
%{_desktopdir}/qterminal_drop.desktop
%{_datadir}/appdata/qterminal.appdata.xml
%{_iconsdir}/hicolor/64x64/apps/qterminal.png
