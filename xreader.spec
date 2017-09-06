%define oname Xreader
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define api	3.0
%define major	3
%define devname %mklibname %{name} -d
%define girname %mklibname %{name}-gir %{api}
%define libname_document %mklibname %{name}document %{major}
%define libname_view %mklibname %{name}view %{major}

Summary:	A generic Document Reader 
Name:		%{lname}
Version:	1.4.4
Release:	1
License:	GPLv2 and LGPLv2
Group:		Publishing
Url:		https://github.com/linuxmint/xreader
Source:		https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.4.4-fix-undeclared-function.patch

BuildRequires:	mate-common
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk+-doc)
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(kpathsea)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libgxps)
BuildRequires:	pkgconfig(libnemo-extension)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	yelp-tools

Requires:	%{name}-backends = %{version}-%{release}

%description
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/%{name}-previewer
%{_bindir}/%{name}-thumbnailer
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{major}/
%{_libexecdir}/%{name}d
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.x.reader.Daemon.service
%{_datadir}/glib-2.0/schemas/org.x.reader.gschema.xml
%{_datadir}/thumbnailers/%{name}.thumbnailer
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.*
%{_mandir}/man1//%{name}-previewer.*
%{_mandir}/man1/%{name}-thumbnailer.*
%doc README
%doc AUTHORS
%doc COPYING

#---------------------------------------------------------------------------

%package -n %{libname_document}
Summary:	A generic Document Reader -- System Library
Group:		System/Libraries

%description -n %{libname_document}
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains the %{name} shared library used for reading documents.

%files -n %{libname_document}
%{_libdir}/lib%{name}document.so.%{major}*
%doc COPYING

#---------------------------------------------------------------------------

%package -n %{libname_view}
Summary:	A generic Document Reader -- System Library
Group:		System/Libraries

%description -n %{libname_view}
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains the %{name} shared library used for viewing documents.

%files -n %{libname_view}
%{_libdir}/lib%{name}view.so.%{major}*
%doc COPYING

#---------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains GObject Introspection interface libraries for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/XreaderDocument-1.5.0.typelib
%{_libdir}/girepository-1.0/XreaderView-1.5.0.typelib
%doc COPYING

#---------------------------------------------------------------------------

%package backends
Summary:	A generic Document Reader (View and Document)
Group:		System/Libraries

%description backends
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains backends for %{name}.

%files backends
%dir %{_libdir}/%{name}/%{major}/backends/
%{_libdir}/%{name}/%{major}/backends/*
%doc COPYING

#---------------------------------------------------------------------------

%package -n nemo-extension-%{name}
Summary:	X-Apps Document Reader file manager extension
Group:		Publishing
Requires:	%{name} = %{version}-%{release}
Requires:	nemo
Recommends:	nemo-extension-sendto

%description -n nemo-extension-%{name}
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains the %{name} extension for the Nemo file manager.

%files -n nemo-extension-%{name}
%{_libdir}/nemo/
%{_datadir}/nemo/extensions/lib%{name}-properties-page.nemo-extension
%doc COPYING

#---------------------------------------------------------------------------

%package -n caja-extension-%{name}
Summary:	X-Apps Document Reader file manager extension
Group:		Publishing
Requires:	%{name} = %{version}-%{release}
Requires:	caja
Recommends:	caja-extension-sendto

%description -n caja-extension-%{name}
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains the %{name} extension for the Caja file manager.

%files -n caja-extension-%{name}
%{_libdir}/caja/
%{_datadir}/caja/extensions/lib%{name}-properties-page.caja-extension
%doc COPYING

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers, libraries and docs for the %{oname}
Group:		Development/C
Requires:	%{name}-backends = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
%{oname} is a document viewer capable of displaying multiple and single page
document formats like PostScript (PS), Encapsulated PostScript (EPS), DJVU,
DVI, XPS and Portable Document Format (PDF) files, as well as comic book
archive files. When supported by the document, it also allows searching for
text, copying text to the clipboard, hypertext navigation and
table-of-contents bookmarks.

This package contains header files and development libraries needed to
develop programs using %{oname}.

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/
%doc README
%doc AUTHORS
%doc COPYING

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-introspection \
	--enable-gtk-doc \
	--enable-pixbuf \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

