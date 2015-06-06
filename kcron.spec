Summary:	Graphical editor for the cron command scheduler
Name:		kcron
Version:	15.04.2
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)

%description
Kcron is a graphical frontend to the cron system, used to schedule regular
tasks on a Unix system.

%files
%{_kde_services}/kcm_cron.desktop
%{_kde_libdir}/kde4/kcm_cron.so
%{_kde_docdir}/*/*/kcron

#------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install_std -C build
