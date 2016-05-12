Summary:	Graphical editor for the cron command scheduler
Name:		kcron
Version:	16.04.1
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5XmlGui)


%description
Kcron is a graphical frontend to the cron system, used to schedule regular
tasks on a Unix system.

%files
%{_datadir}/kservices5/kcm_cron.desktop
%{_libdir}/qt5/plugins/kcm_cron.so
%doc %{_docdir}/*/*/kcron

#------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
