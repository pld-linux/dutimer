Summary:	Dial Up Timer
Summary(pl):	Dial Up Timer
Name:		dutimer
Version:	0.4.1
Release:	3
License:	GPL
Group:		Networking
Group(pl):	Sieciowe
Source0:	%{name}-v%{version}-linux.tar.gz
URL:		http://dutimer.viii-lo.krakow.pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

gzip -9nf doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_sbindir}/*
