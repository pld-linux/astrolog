Summary:	Astrology program
Summary(pl):	Program do astrologii
Name:		astrolog
Version:	5.40
Release:	1
License:	Freeware
Group:		X11/Applications
Source0:	http://www.astrolog.org/ftp/ast54unx.shr
# Source0-md5:	3d604e013d8a7e2134bc637f17bb2857
Patch0:		%{name}-libs.patch
URL:		http://www.astrolog.org/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix	/usr/X11R6

%description
Astrolog is a freeware astrology program.

%description -l pl
Astrolog jest darmowym programem do astrologii.

%prep
%setup -q -c -T
/bin/sh %{SOURCE0}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}
install astrolog $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.540
%attr(755,root,root) %{_bindir}/*
