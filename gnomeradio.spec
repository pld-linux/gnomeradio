Summary:	A FM-Tuner program for Gnome
Summary(pl):	Tuner FM dla Gnome
Name:		gnomeradio
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://mfcn.ilo.de/gnomeradio/%{name}-%{version}.tar.gz
URL:		http://mfcn.ilo.de/gnomeradio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	libtool
%ifnarch sparc sparcv9 sparc64 alpha
BuildRequires:	lirc-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A FM-Tuner program for Gnome.

%description -l pl
Tuner FM dla Gnome.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
aclocal -I macros
%{__autoconf}
%{__automake}
# CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Multimedia

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*.desktop
