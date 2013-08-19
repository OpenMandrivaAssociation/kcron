Summary:	Graphical editor for the cron command scheduler
Name:		kcron
Version:	4.11.0
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- Split from kdeadmin4 package as upstream did
- New version 4.11.0
