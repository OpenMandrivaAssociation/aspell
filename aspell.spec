%define major	15
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name: aspell
Version: 0.60.6
Release: %mkrel 7
Summary: A Free and Open Source interactive spelling checker program
Group: Text tools
Source0: ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
URL: http://aspell.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
License: LGPL
Requires: aspell-dictionary

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

%pre
if [ -d %_libdir/aspell ]; then 
    rm -rf %_libdir/aspell
fi

%files -f %{name}.lang
%defattr(-,root,root)
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

#----------------------------------------------------------------------

%package -n %{libname}
Group: Text tools
Summary: Shared library files for aspell

%description -n %{libname}
Shared library files for the aspell package.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib*.so.%{major}*

#----------------------------------------------------------------------

%package -n %{develname}
Group: Development/Other
Summary: Development files for aspell
Requires: %{name} = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Provides: libaspell-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{libname}-devel
Conflicts: libpspell4-devel

%description -n %{develname}
Development headers, and files for development from the aspell package.

%files -n %{develname}
%defattr(-, root, root)
%{_bindir}/pspell-config
%_includedir/*
%_libdir/libaspell.so
%_libdir/libpspell.so
%_libdir/lib*.la
%multiarch %{multiarch_bindir}/pspell-config

#----------------------------------------------------------------------

%package manual
Group: Text tools
Summary: Manual for aspell

%description manual
This package contains a manual for aspell.

GNU Aspell is a Free and Open Source spell checker designed to eventually 
replace Ispell. It can either be used as a library or as an independent 
spell checker. 

%files manual
%defattr(-, root, root)
%doc manual/*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x 

%make

%install
rm -rf %buildroot

make DESTDIR=%buildroot install

# Provides symlink for configures that mean to match aspell on %%_libdir/aspell
pushd %buildroot%_libdir
    ln -sf aspell-0.60 aspell
popd

# multiarch policy
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/pspell-config

%find_lang %{name}



%clean
rm -rf %buildroot


