%define name		gfontsampler
%define version 	0.4
%define release %mkrel 10

Name:			%{name}
Version:		%{version}
Release:		%{release}
License:		GPL
Source0:		http://linuxadvocate.org/projects/gfontsampler/downloads/%name-%version.tar.bz2
Patch: gfontsampler-0.4-xdg.patch
Group:			Graphical desktop/GNOME
URL:			http://linuxadvocate.org/projects/gfontsampler/
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
Summary:		Gnome Font Sampler
BuildRequires:		libgnomeui2-devel
BuildRequires:		libglade2.0-devel
BuildRequires:		bison
BuildRequires:		imagemagick

%description
Gnome Font Sampler
The easiest way to pick the right font for the job.

Features:
* View all yours fonts at once
* Choose text and background colors
* Choose bold, italics, underline, font size, and example text used
* It's Free Software released under the GPL 

%prep
%setup -q
%patch -p1 -b .xdg

%build
%configure2_5x
%make LDFLAGS="-rdynamic -lpangoxft-1.0"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/%_prefix/doc
rm -fr $RPM_BUILD_ROOT/%_includedir
mv %buildroot%{_datadir}/gnome/apps/Utilities/ %buildroot%{_datadir}/applications
#menu

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/%name-icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/%name-icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/%name-icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-, root, root)
%doc AUTHORS
%{_bindir}/*
#%{_includedir}/%{name}
%_datadir/applications/%name.desktop
%{_datadir}/pixmaps/%{name}/%{name}-icon.png
%{_datadir}/%{name}
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png


