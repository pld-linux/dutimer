Summary:	Dial Up Timer
Summary(pl):	Dial Up Timer
Name:		dutimer
Version:	0.4.1
Release:	3
License:	GPL
Group:		Networking
Source0:	ftp://viii-lo.krakow.pl/pub/linux/dutimer/%{name}-v%{version}-linux.tar.gz
URL:		http://dutimer.viii-lo.krakow.pl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dial Up Timer shows modem connection time and cost.

%description -l pl
Dial Up Timer wyświetla czas oraz koszt połączenia modemowego.

%prep
%setup -q

%build
%{__make} pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install dutimer $RPM_BUILD_ROOT%{_sbindir}/dutimer

gzip -9nf doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_sbindir}/*
