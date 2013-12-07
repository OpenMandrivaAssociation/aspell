%define	major	15
%define	libname	%mklibname %{name} %{major}
%define	libpspell	%mklibname pspell %{major}
%define	devname	%mklibname %{name} -d

Summary:	A Free and Open Source interactive spelling checker program
Name:		aspell
Version:	0.60.6.1
Release:	11
Group:		Text tools
License:	LGPL
Url:		http://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
Suggests:	aspell-dictionary

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
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{libpspell} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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

