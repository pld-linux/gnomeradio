Summary:	A FM-Tuner program for GNOME
Summary(pl):	Tuner FM dla GNOME
Name:		gnomeradio
Version:	1.4
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://mfcn.ilo.de/gnomeradio/%{name}-%{version}.tar.gz
# Source0-md5:	799efdfeb7c44f82cbb4b3c8f727f7f5
Patch0:		%{name}-schema.patch
Patch1:		%{name}-warnings.patch
Patch2:		%{name}-do_not_popup_without_lirc.patch
URL:		http://mfcn.ilo.de/gnomeradio/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2 >= 2.1.5
BuildRequires:	libtool
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A FM-Tuner program for GNOME.

%description -l pl
Tuner FM dla GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
