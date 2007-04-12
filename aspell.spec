%define lib_name %mklibname %{name} %{lib_major}
%define lib_major 15
%define ver_major 0.60

Summary:       A Free and Open Source interactive spelling checker program
Name:          aspell
Version:       0.60.5
Release:       %mkrel 2
Group:         Text tools
Source0:       ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.bz2
Patch0:        aspell-0.60.4-fix-build.patch 
URL:           http://aspell.net/
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
License:       LGPL
BuildRequires: automake1.8

# Mandrake Stuff.
Requires:      aspell-dictionary
Requires:      %{lib_name} = %{version}-%{release}

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


%package -n %{lib_name}
Group:          Text tools
Summary:        Shared library files for aspell

%description -n %{lib_name}
Shared library files for the aspell package.

%package -n %{lib_name}-devel
Group:          Development/Other
Summary:        Development files for aspell
Requires:       %{name} = %{version}-%{release}
Requires:		%{lib_name} = %{version}-%{release}
Provides:       libaspell-devel = %{version}-%{release}
Provides:		aspell-devel = %{version}-%{release}
Obsoletes:      aspell-devel
Conflicts:		libpspell4-devel

%description -n %{lib_name}-devel
Development headers, and files for development from the aspell package.

%package manual
Group:         Text tools
Summary:       Manual for aspell

%description manual
This package contains a manual for aspell.

GNU Aspell is a Free and Open Source spell checker designed to eventually 
replace Ispell. It can either be used as a library or as an independent 
spell checker. 

%prep
%setup -q
#%patch0 -p0 -b .extra_qualificaton
#update build environment for x86-64
#aclocal-1.8   # running aclocal fails; maybe some missing files? (pablo)
#autoconf

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# multiarch policy
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/pspell-config

%find_lang %{name}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_libdir}/aspell-%{ver_major}
%doc %{_datadir}/info/aspell*
%doc %{_mandir}/man1/*.1*

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%{_bindir}/pspell-config
%multiarch %{multiarch_bindir}/pspell-config
%{_includedir}/*
%{_libdir}/libaspell.so
%{_libdir}/libpspell.so
%{_libdir}/lib*.la

%files manual
%defattr(-, root, root)
%doc manual/*


