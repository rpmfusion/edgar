%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           edgar
Version:        1.12
Release:        1%{?dist}
Summary:        A platform game

# edgar now contains sounds licensed under a "good" Fedora license:
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=653813#80
License:        GPLv2+ and CC-BY and CC-BY-SA and CC0 and GPLv3
URL:            http://www.parallelrealities.co.uk/p/legend-of-edgar.html
Source0:        http://downloads.sourceforge.net/legendofedgar/%{name}/%{name}-%{version}-1.tar.gz

BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_ttf-devel
BuildRequires: zlib-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
Requires:      hicolor-icon-theme


%description
When his father fails to return home after venturing out one dark and stormy 
night, Edgar fears the worst: he has been captured by the evil sorcerer who 
lives in a fortress beyond the forbidden swamp.

Donning his armor, Edgar sets off to rescue him, but his quest will not be 
easy...


%prep
%setup -q

# Fix Makefile
sed -i 's:$(PREFIX)/share/games/edgar/:$(PREFIX)/share/edgar/:' \
  makefile

# Use standard Fedora CFLAGS to compile
sed -i 's/^CFLAGS = -Wall -pedantic/CFLAGS +=/' makefile

# Fix end-of-line encoding
for txtfile in src/graphics/font.h src/system/random.h
do
  sed -i 's/\r//' $txtfile
done

# Fix premissions
for txtfile in src/graphics/font.h src/graphics/font.c src/system/random.h \
  src/system/random.c
do
  chmod 644 $txtfile
done


%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} 


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} \
  BIN_DIR=%{buildroot}%{_bindir}/ \
  DATA_DIR=%{buildroot}%{_datadir}/%{name}/ \
  DOC_DIR=%{buildroot}%{_pkgdocdir}

desktop-file-install \
  --delete-original \
  --remove-key Encoding \
  --add-category=ActionGame \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%doc %{_pkgdocdir}


%changelog
* Sun Aug 25 2013 Andrea Musuruane <musuruan@gmail.com> - 1.12-1
- Updated to upstream 1.12-1
- Used unversioned docdir
- Sounds are now licensed under a "good" Fedora license

* Wed Jun 19 2013 Andrea Musuruane <musuruan@gmail.com> - 1.09-1
- Updated to upstream 1.09-1

* Thu Apr 04 2013 Andrea Musuruane <musuruan@gmail.com> - 1.08-1
- Updated to upstream 1.08-1

* Sun Mar 03 2013 Andrea Musuruane <musuruan@gmail.com> - 1.07-1
- Updated to upstream 1.07-1

* Fri Feb 08 2013 Andrea Musuruane <musuruan@gmail.com> - 1.06-2
- Updated to upstream 1.06-2

* Sat Jan 26 2013 Andrea Musuruane <musuruan@gmail.com> - 1.06-1
- Updated to upstream 1.06-1

* Thu Dec 06 2012 Andrea Musuruane <musuruan@gmail.com> - 1.05-1
- Updated to upstream 1.05-1

* Sun Oct 28 2012 Andrea Musuruane <musuruan@gmail.com> - 1.04-2
- Fixed license (BZ #2378)

* Sat Sep 22 2012 Andrea Musuruane <musuruan@gmail.com> - 1.04-1
- Updated to upstream 1.04-1

* Wed Aug 08 2012 Andrea Musuruane <musuruan@gmail.com> - 1.03-1
- Updated to upstream 1.03-1

* Sat Jun 23 2012 Andrea Musuruane <musuruan@gmail.com> - 1.02-2
- Updated to upstream 1.02-2

* Sun Jun 17 2012 Andrea Musuruane <musuruan@gmail.com> - 1.02-1
- Updated to upstream 1.02-1

* Wed May 16 2012 Andrea Musuruane <musuruan@gmail.com> - 1.01-1
- Updated to upstream 1.01-2

* Thu Apr 26 2012 Andrea Musuruane <musuruan@gmail.com> - 1.00-1
- First release

