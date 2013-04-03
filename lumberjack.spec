Summary:	Cuts logs in preparation for processing elsewhere
Name:		lumberjack
Version:	0.0.8
Release:	1
License:	Apache v2.0
Group:		Daemons
Source0:	https://github.com/jordansissel/lumberjack/archive/v%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	2da12b7b483c68063b10d3d553fccfd5
Source1:	https://raw.github.com/jordansissel/experiments/master/c/better-assert/insist.h
# Source1-md5:	2b91bd982185a96d7e70a3b8ebfb0b0c
URL:		https://github.com/jordansissel/lumberjack
BuildRequires:	jemalloc-devel
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	zeromq-devel < 3.0
BuildRequires:	zeromq-devel >= 2.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to collect logs locally in preparation for processing
elsewhere!

Problem: logstash jar releases are too fat for constrained systems.

%prep
%setup -q
install -d build/include
cp -p %{SOURCE1} build/include/insist.h

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	VENDOR=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p build/bin/* $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md PROTOCOL.md
%attr(755,root,root) %{_sbindir}/lumberjack
%attr(755,root,root) %{_sbindir}/lumberjack.sh
