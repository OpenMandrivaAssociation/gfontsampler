%define name		gfontsampler
%define version 	0.4
%define release %mkrel 6

Name:			%{name}
Version:		%{version}
Release:		%{release}
License:		GPL
Source0:		http://linuxadvocate.org/projects/gfontsampler/downloads/%name-%version.tar.bz2
Patch: gfontsampler-0.4-xdg.patch
Group:			Graphical desktop/GNOME
URL:			http://linuxadvocate.org/projects/gfontsampler/
Summary:		Gnome Font Sampler
BuildRequires:		libgnomeui2-devel
BuildRequires:		libglade2.0-devel
BuildRequires:		bison
BuildRequires:		ImageMagick

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
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GFontSampler" longtitle="Font previewer" section="System/Text Tools" xdg="true"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/%name-icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/%name-icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/%name-icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-, root, root)
%doc AUTHORS
%{_bindir}/*
#%{_includedir}/%{name}
%_datadir/applications/%name.desktop
%{_datadir}/pixmaps/%{name}/%{name}-icon.png
%{_datadir}/%{name}
%{_menudir}/%name
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png


