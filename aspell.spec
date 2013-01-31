%define	major	15
%define	libname	%mklibname %{name} %{major}
%define	libpspell	%mklibname pspell %{major}
%define	devname	%mklibname %{name} -d

Summary:	A Free and Open Source interactive spelling checker program
Name:		aspell
Version:	0.60.6.1
Release:	4
Group:		Text tools
License:	LGPL
URL:		http://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
Requires:	aspell-dictionary

%description
GNU Aspell is a Free and Open Source spell checker designed to eventually 
replace Ispell. It can either be used as a library or as an independent 
spell checker.
Its main feature is that it does a much better job of coming up with possible 
suggestions than just about any other spell checker out there for the English 
language, including Ispell and Microsoft Word. It also has many other technical
enhancements over Ispell such as using shared memory for dictionaries and 
intelligently handling personal dictionaries when more than one Aspell process 
is open at once.

%package -n	%{libname}
Summary:	Shared library files for aspell
Group:		Text tools

%description -n	%{libname}
Shared library files for the aspell package.

%package -n	%{libpspell}
Summary:	Shared library files for aspell
Group:		Text tools
Conflicts:	%{libname} < 0.60.6.1-3

%description -n	%{libpspell}
Shared library files for the aspell package.

%package -n	%{devname}
Summary:	Development files for aspell
Group:		Development/Other
Requires:	%{name} >= %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{libpspell} >= %{version}-%{release}
Provides:	libaspell-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < %{version}-%{release}
Conflicts:	libpspell4-devel

%description -n	%{devname}
Development headers, and files for development from the aspell package.

%package	manual
Summary:	Manual for aspell
Group:		Text tools

%description	manual
This package contains a manual for aspell.

GNU Aspell is a Free and Open Source spell checker designed to eventually 
replace Ispell. It can either be used as a library or as an independent 
spell checker. 

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--disable-rpath

%make

%install
%makeinstall_std

# Provides symlink for configures that mean to match aspell on %%_libdir/aspell
ln -sf aspell-0.60 %{buildroot}%{_libdir}/aspell

# multiarch policy
%multiarch_binaries %{buildroot}%{_bindir}/pspell-config

%find_lang %{name}

%pre
if [ -d %{_libdir}/aspell ]; then 
    rm -rf %{_libdir}/aspell
fi

%files -f %{name}.lang
%doc README TODO
%{_bindir}/aspell*
%{_bindir}/run-with-aspell
%{_bindir}/word-list-compress
%{_bindir}/precat
%{_bindir}/preunzip
%{_bindir}/prezip
%{_bindir}/prezip-bin
%{_libdir}/aspell-0.60
%{_libdir}/aspell
%doc %{_datadir}/info/aspell*
%doc %{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/libaspell.so.%{major}*

%files -n %{libpspell}
%{_libdir}/libpspell.so.%{major}*

%files -n %{devname}
%{_bindir}/pspell-config
%{_includedir}/*
%{_libdir}/libaspell.so
%{_libdir}/libpspell.so
%{multiarch_bindir}/pspell-config

%files manual
%doc manual/*

%changelog
* Thu Jan 31 2013 Per ÿyvind Karlsen <peroyvind@mandriva.org> 0.60.6.1-4
- cleanups

* Wed Dec 14 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.60.6.1-3
+ Revision: 741383
- fixed pspell name
- split out libpspell
- disabled static build instead of removing

* Sat Dec 10 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.6.1-2
+ Revision: 740064
- delete the libtool *.la files
- various fixes

* Thu Aug 25 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.6.1-1
+ Revision: 697099
- spec file clean
- update to new version 0.60.6.1

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.6-9
+ Revision: 661620
- multiarch fixes

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.6-8mdv2011.0
+ Revision: 603188
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.6-7mdv2010.1
+ Revision: 518902
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.60.6-6mdv2010.0
+ Revision: 413042
- rebuild

* Mon Mar 23 2009 G√∂tz Waschk <waschk@mandriva.org> 0.60.6-5mdv2009.1
+ Revision: 360644
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.60.6-4mdv2009.1
+ Revision: 316457
- rebuild

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 0.60.6-3mdv2009.0
+ Revision: 275998
- apply devel policy
- check major

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.60.6-2mdv2009.0
+ Revision: 264320
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.60.6-1mdv2009.0
+ Revision: 209743
- 0.60.6 (may fix build with gcc43)

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.60.5-7mdv2008.1
+ Revision: 148465
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.5-6mdv2008.0
+ Revision: 89572
- rebuild

* Mon May 21 2007 Helio Chissini de Castro <helio@mandriva.com> 0.60.5-5mdv2008.0
+ Revision: 29447
- Play nice with shell during installs

* Fri May 18 2007 Helio Chissini de Castro <helio@mandriva.com> 0.60.5-4mdv2008.0
+ Revision: 28334
- Back to old libdir 0.60 as pointed by Thierry Vignaud, To keep compat with other apps configures
  that looks in plain aspell directory, keep a symlink to aspell.

* Fri Apr 20 2007 Helio Chissini de Castro <helio@mandriva.com> 0.60.5-3mdv2008.0
+ Revision: 16358
- Install proper aspell files under aspell dir, bit under a versionated dir. Is clear that in 2008 we
  will not have 2 aspell on machines, and having such versionated dir made all packages depending on
  aspell add a patch on their configures to detect, instead of standard aspell. Now things is a little
  bit more sane, as we fix the parent source, not the dependencies.
- Remove unused patch


* Mon Jan 29 2007 Olivier Blin <oblin@mandriva.com> 0.60.5-2mdv2007.0
+ Revision: 115140
- split manual in aspell-manual package

* Thu Jan 18 2007 J√©r√¥me Soyer <saispo@mandriva.org> 0.60.5-1mdv2007.1
+ Revision: 110162
- New release 0.60.5

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 0.60.4-3mdv2007.1
+ Revision: 74494
- Import aspell

* Thu Sep 07 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.60.4-3mdv2007.0
- Add Patch to fix extra qualification

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 0.60.4-2mdk
- rebuild for sparc

* Tue Nov 29 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.60.4-1mdk
- new release

* Thu Aug 11 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.60.3-2mdk
- fix rpmlint errors ( dot ended summary )

* Wed Jun 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.60.3-1mdk
- new release

* Fri Feb 25 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.60.2-2mdk
- multiarch

* Mon Dec 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.60.2-1mdk
- 0.60.2

* Wed Dec 01 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.60.1.1-1mdk
- updated version

* Fri Sep 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.50.5-3mdk
- Enable libtoolize
- Remove patch0, regenerate build environment instead

* Fri Jun 04 2004 Laurent Montel <lmontel@mandrakesoft.com> 0.50.5-2mdk
- Rebuild against new gcc

* Fri May 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.50.5-1mdk
- Release 0.50.5
- Regenreate patch0 (partially merged)

* Fri May 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.50.4.1-2mdk
- Rebuild

* Mon Mar 08 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.50.4.1-1.2mdk
- really fix amd64 build

* Mon Mar 01 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.50.4.1-1.1mdk
- amd64 build fixes

