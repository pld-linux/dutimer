Summary:	Dial Up Timer
Summary(pl):	Dial Up Timer
Name:		dutimer
Version:	0.4.1
Release:	3
License:	GPL
Group:		Networking
Source0:	ftp://viii-lo.krakow.pl/pub/linux/dutimer/%{name}-v%{version}-linux.tar.gz
# Source0-md5:	77747b471458ab769cfe7a198b2ac26c
URL:		http://dutimer.viii-lo.krakow.pl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dial Up Timer shows modem connection time and cost.

%description -l pl
Dial Up Timer wy¶wietla czas oraz koszt po³±czenia modemowego.

%prep
%setup -q

%build
%{__make} pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install dutimer $RPM_BUILD_ROOT%{_sbindir}/dutimer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_sbindir}/*
