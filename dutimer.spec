Summary:     Dial Up Timer
Summary(pl): Dial Up Timer
Name:        dutimer
Version:     0.3.0
Release:     1
Copyright:   GPL
Source:      %{name}-v%{version}-linux.tar.gz
Group:       Applications/Networking
Group(pl):   Aplikacje/Sieciowe
URL:         http://dutimer.viii-lo.krakow.pl
BuildRoot:   /tmp/buildroot-%{name}-%{version}

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
install -d $RPM_BUILD_ROOT/usr/sbin

install -s dutimer $RPM_BUILD_ROOT/usr/sbin/dutimer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc doc/*
%attr(755, root, root) /usr/sbin/*

%changelog
* Thu Sep 10 1998 Marek Obuchowicz <elephant@shadow.eu.org>
  [0.07-1]
- first try RPM
