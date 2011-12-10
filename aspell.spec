%define major 15
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A Free and Open Source interactive spelling checker program
Name:		aspell
Version:	0.60.6.1
Release:	2
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

%package -n %{libname}
Summary:	Shared library files for aspell
Group:		Text tools

%description -n %{libname}
Shared library files for the aspell package.

%package -n %{develname}
Summary:	Development files for aspell
Group:		Development/Other
Requires:	%{name} >= %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}
Provides:	libaspell-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < %{version}-%{release}
Conflicts:	libpspell4-devel

%description -n %{develname}
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
%setup -q

%build
%configure2_5x \
	--disable-rpath

%make

%install
rm -rf %{buildroot}

%makeinstall_std
#make DESTDIR=%buildroot install

# Provides symlink for configures that mean to match aspell on %%_libdir/aspell
pushd %{buildroot}%{_libdir}
    ln -sf aspell-0.60 aspell
popd

# multiarch policy
%multiarch_binaries %{buildroot}%{_bindir}/pspell-config

%find_lang %{name}

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

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
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_bindir}/pspell-config
%{_includedir}/*
%{_libdir}/libaspell.so
%{_libdir}/libpspell.so
%{multiarch_bindir}/pspell-config

%files manual
%doc manual/*
