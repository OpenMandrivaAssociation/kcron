Summary:	Graphical editor for the cron command scheduler
Name:		kcron
Version:	4.14.1
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
* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- Split from kdeadmin4 package as upstream did
- New version 4.11.0
