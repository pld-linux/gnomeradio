Summary:	A FM-Tuner program for Gnome
Summary(pl):	Tuner FM dla Gnome
Name:		gnomeradio
Version:	1.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://mfcn.ilo.de/gnomeradio/%{name}-%{version}.tar.gz
Patch0:		%{name}-schema.patch
Patch1:		%{name}-warnings.patch
URL:		http://mfcn.ilo.de/gnomeradio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2 >= 2.1.3-3
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	rpm-build >= 4.1-8.2
Requires:	bonobo-activation >= 2.1.0
%ifnarch sparc sparcv9 sparc64 alpha
BuildRequires:	lirc-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A FM-Tuner program for Gnome.

%description -l pl
Tuner FM dla Gnome.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
    --disable-install-schemas \
    --with-gconf-schema-file-dir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{name} --with-gnome --all-name

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/*.desktop
%{_pixmapsdir}/*
%{_sysconfdir}/*
