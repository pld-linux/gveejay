#
Summary:	Front End for veejay a video mixing/editing Instrument
Summary(pl):	Graficzna nak³adka dla veejay do edycji i miksowania filmów
Name:		gveejay
Version:	0.4.7
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/veejay/%{name}-%{version}.tar.bz2
# Source0-md5:	2c5a7064b894004f17fbac65c378cb73
URL:		http://veejay.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	mjpegtools-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Front End for veejay a video mixing/editing Instrument

%description -l pl
Graficzna nak³adka dla veejay do edycji i miksowania filmów

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C man install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/*
#{_datadir}/%{name}
%{_mandir}/man1/*

#{_mandir}/man1/*
#{_pixmapsdir}/*
#{_mandir}/man1/gveejay.1
# brakuje pixmaps i man do poprawy
