Summary:	Dial Up Timer
Summary(pl):	Dial Up Timer
Name:		dutimer
Version: 	0.4.1
Release: 	2d
Copyright:	GPL
Source: 	%{name}-v%{version}-linux.tar.gz
Group:		Networking
Group(pl):	Sieciowe
URL: 		http://dutimer.viii-lo.krakow.pl
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Dial Up Timer shows modem connection time and cost.

%description -l pl
Dial Up Timer wy¶wietla czas oraz koszt po³±czenia modemowego.

%prep
%setup -q

%build
make pl

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -s dutimer $RPM_BUILD_ROOT%{_sbindir}/dutimer

bzip2 -9 doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*

%attr(755,root,root) %{_sbindir}/*

%changelog
* Thu Feb 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.4.1-2d]
- added Group(pl),
- compresswd documentation,
- changed %buildroot.

* Sun Feb 14 1999 Piotr Grochowski <pager@dione.ids.pl>
  [0.4.1-1d]
- Updated to 0.4.1

* Mon Oct 19 1998 Piotr Grochowski <pager@dione.ids.pl>
  [0.3.0-1d]
- Updated to 0.3.0

* Thu Sep 24 1998 Piotr Grochowski <pager@dione.ids.pl>
  [0.2.1-1d]
- Updated to 0.2.1

* Tue Sep 22 1998 Piotr Grochowski <pager@dione.ids.pl>
  [0.2.0-1d]
- Updated to 0.2.0

* Mon Sep 21 1998 Piotr Grochowski <pager@dione.ids.pl>
  [0.1.1-1d]
- Updated to 0.1.1

* Sun Sep 13 1998 Marek Obuchowicz <elephant@shadow.eu.org>
  [0.1.0-1d]
- Updated to 0.1.0

* Thu Sep 10 1998 Marek Obuchowicz <elephant@shadow.eu.org>
  [0.07-1d]
- first try RPM.
