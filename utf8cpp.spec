Summary:	UTF-8 with C++ in a Portable Way
Summary(pl.UTF-8):	UTF-8 z C++ w przenośny sposób
Name:		utf8cpp
Version:	4.0.5
Release:	1
License:	Boost
Group:		Libraries
#Source0Download: https://github.com/nemtrif/utfcpp/releases
Source0:	https://github.com/nemtrif/utfcpp/archive/v%{version}/utfcpp-%{version}.tar.gz
# Source0-md5:	8e0fe13266a7fa02f61340bf399986c3
URL:		https://github.com/nemtrif/utfcpp
BuildRequires:	cmake >= 3.14
BuildRequires:	rpmbuild(macros) >= 1.605
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small, C++98 compatible generic library to handle UTF-8 encoded
strings. For anybody used to work with STL algorithms and iterators,
it should be easy and natural to use.

%description -l pl.UTF-8
Mała, ogólna, zgodna z C++98 biblioteka do obsług łańcuchów kodowanych
UTF-8. Powinna być łatwa i naturalna w użyciu dla każdego pracującego
z algorytmami i iteratorami STL.

%package devel
Summary:	UTF-8 with C++ in a Portable Way
Summary(pl.UTF-8):	UTF-8 z C++ w przenośny sposób
Group:		Development/Libraries

%description devel
Small, C++98 compatible generic library to handle UTF-8 encoded
strings. For anybody used to work with STL algorithms and iterators,
it should be easy and natural to use.

%description devel -l pl.UTF-8
Mała, ogólna, zgodna z C++98 biblioteka do obsług łańcuchów kodowanych
UTF-8. Powinna być łatwa i naturalna w użyciu dla każdego pracującego
z algorytmami i iteratorami STL.

%prep
%setup -q -n utfcpp-%{version}

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/utf8cpp
%dir %{_datadir}/utf8cpp
%{_datadir}/utf8cpp/cmake
