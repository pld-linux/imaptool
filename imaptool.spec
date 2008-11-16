Summary:	An utility for creating client-side HTML image maps
Summary(pl.UTF-8):	Narzędzie do tworzenia map HTML obrazów
Name:		imaptool
Version:	0.9
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://www.sspitzer.org/imaptool/%{name}-%{version}.tar.gz
# Source0-md5:	b1cda4124bf2756efadc372adfa19d11
URL:		http://www.sspitzer.org/imaptool/
Patch0:		%{name}-Makefile.patch
BuildRequires:	libjpeg-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imaptool helps in the creation of client-side HTML image maps. For
more information read about HTML AREA and MAP tags. Both GIF and JPEG
formats are supported.

%description -l pl.UTF-8
imaptool pomaga w tworzeniu map HTML obrazów. Więcej na ten temat
można znaleźć w opisie znaczników AREA i MAP w specyfikacji HTML.
Program obsługuje formaty GIF i JPEG.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install imaptool $RPM_BUILD_ROOT%{_bindir}
install imaptool.man $RPM_BUILD_ROOT%{_mandir}/man1/imaptool.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imaptool
%{_mandir}/man1/imaptool.1*
