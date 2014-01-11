%define vimver 7.4.86
%define sha512sum 464b1a0859e3ddf5e44e49b4befcf9ab937986c623e3039ae0debec811546edb78e596f563917f4378f866b1daeafe9dec4329d057696f1e3cd04e68cbc5244c

Name: vim74 
Version: 7.4 
License: See vim license
Release: 1
Summary: Vim 7.4 

Group: Applications/Editors
URL: http://www.vim.org/    
Source: ftp://ftp.archlinux.org/other/vim/vim-%{vimver}.tar.xz

BuildRequires: ncurses ncurses-devel gcc 

%description
Vim 7.4


%build
cd %{_sourcedir}
wget ftp://ftp.archlinux.org/other/vim/vim-%{vimver}.tar.xz

if ! sha512sum %{_sourcedir}/vim-%{vimver}.tar.xz | grep %{sha512sum}; then
    echo "SHA512 did not match"
    exit 1
fi

tar xJf %{_sourcedir}/vim-%{vimver}.tar.xz


cd %{_sourcedir}/vim-%{vimver}
./configure \
  --prefix=/usr \
  --localstatedir=/var/lib/vim \
  --with-features=huge \
  --enable-gpm \
  --enable-acl \
  --with-x=no \
  --disable-gui \
  --enable-multibyte \
  --enable-cscope \
  --disable-netbeans \
  --disable-perlinterp \
  --disable-pythoninterp \
  --disable-python3interp \
  --disable-rubyinterp \
  --disable-luainterp
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd %{_sourcedir}/vim-%{vimver}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}


%changelog
