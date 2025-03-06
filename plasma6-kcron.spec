#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Graphical editor for the cron command scheduler
Name:		plasma6-kcron
Version:	24.12.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kcron/-/archive/%{gitbranch}/kcron-%{gitbranchd}.tar.bz2#/kcron-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kcron-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(KF6Auth)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  qml(QtNetwork)

%description
Kcron is a graphical frontend to the cron system, used to schedule regular
tasks on a Unix system.

%files -f kcron.lang
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_cron.so
%{_datadir}/qlogging-categories6/kcron.categories
%{_datadir}/metainfo/org.kde.kcron.metainfo.xml
%{_libdir}/libexec/kf6/kauth/kcron_helper
%{_datadir}/dbus-1/system-services/local.kcron.crontab.service
%{_datadir}/dbus-1/system.d/local.kcron.crontab.conf
%{_datadir}/polkit-1/actions/local.kcron.crontab.policy
%{_datadir}/applications/kcm_cron.desktop

#------------------------------------------------------------------------

%prep
%autosetup -p1 -n kcron-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcron --with-html
