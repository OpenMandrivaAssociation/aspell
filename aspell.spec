%define major 15
%define libname %mklibname %{name} %{major}
%define libpspell %mklibname pspell %{major}
%define devname %mklibname %{name} -d

%define beta %{nil}

Summary:	A Free and Open Source interactive spelling checker program
Name:		aspell
Version:	0.60.8.1
%if "%{beta}" != ""
Release:	0.%{beta}.1
Source0:	ftp://alpha.gnu.org/gnu/aspell/%{name}-%{version}-%{beta}.tar.gz
%else
Release:	1
Source0:	ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
%endif
Group:		Text tools
License:	LGPL
Url:		https://aspell.net/
Suggests:	aspell-dictionary
BuildRequires:	slibtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make

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

%package -n %{libname}
Summary:	Shared library files for aspell
Group:		Text tools

%description -n %{libname}
Shared library files for the aspell package.

%package -n %{libpspell}
Summary:	Shared library files for aspell
Group:		Text tools
Conflicts:	%{libname} < 0.60.6.1-3

%description -n %{libpspell}
Shared library files for the aspell package.

%package -n %{devname}
Summary:	Development files for aspell
Group:		Development/Other
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{libpspell} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development headers, and files for development from the aspell package.

%package manual
Summary:	Manual for aspell
Group:		Text tools

%description manual
This package contains a manual for aspell.

GNU Aspell is a Free and Open Source spell checker designed to eventually 
replace Ispell. It can either be used as a library or as an independent 
spell checker. 

%prep
%if "%{beta}" != ""
%autosetup -n %{name}-%{version}-%{beta} -p1
%else
%autosetup -p1
%endif

%build
%configure \
	--disable-rpath

%make_build LIBTOOL=slibtool-shared

%install
%make_install LIBTOOL=slibtool-shared

# Provides symlink for configures that mean to match aspell on %%_libdir/aspell
ln -sf aspell-0.60 %{buildroot}%{_libdir}/aspell

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

%files manual
%doc manual/*
