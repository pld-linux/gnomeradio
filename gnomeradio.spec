Summary:	A FM-Tuner program for GNOME
Summary(pl.UTF-8):	Tuner FM dla GNOME
Name:		gnomeradio
Version:	1.6
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.wh-hms.uni-ulm.de/~mfcn/gnomeradio/packages/%{name}-%{version}.tar.gz
# Source0-md5:	07b9d511f79e38f114af51cc7bfc014a
Patch0:		%{name}-schema.patch
Patch1:		%{name}-warnings.patch
Patch2:		%{name}-do_not_popup_without_lirc.patch
Patch3:		%{name}-no_disable_deprecated.patch
Patch4:		%{name}-desktop.patch
URL:		http://www.wh-hms.uni-ulm.de/~mfcn/gnomeradio/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2 >= 2.1.5
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rarian-compat
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A FM-Tuner program for GNOME.

%description -l pl.UTF-8
Tuner FM dla GNOME.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p0
%patch4 -p1

%build
rm -f missing
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-install-schemas \
	--with-gconf-schema-file-dir=%{_sysconfdir}/gconf/schemas

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.lirc example.lircrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
