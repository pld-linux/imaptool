Summary:	An utility for creating client-side HTML image maps
Summary(pl):	Narz�dzie do tworzenia map HTML obraz�w
Name:		imaptool
Version:	0.9
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.sspitzer.org/imaptool/%{name}-%{version}.tar.gz
# Source0-md5:	b1cda4124bf2756efadc372adfa19d11
URL:		http://www.sspitzer.org/imaptool/
Patch0:		%{name}-Makefile.patch
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imaptool helps in the creation of client-side HTML image maps. For
more information read about HTML AREA and MAP tags. Both GIF and JPEG
formats are supported.

%description -l pl
imaptool pomaga w tworzeniu map HTML obraz�w. Wi�cej na ten temat
dowiesz si�, gdy poczytasz o tagach AREA i MAP w specyfikacji HTML.
Program obs�uguje formaty GIF i JPEG.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	LIBDIR="-L%{_prefix}/X11R6/%{_lib}"

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
