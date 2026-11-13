Name:           ipcalc
Version:        1.2.0
Release:        1
Summary:        IP network address calculator (IPv4 and IPv6)
License:        GPLv2
URL:            https://gitlab.com/ipcalc/ipcalc
Source0:        %{name}-%{version}.tar.gz
# Manual page pre-generated with ronn (not available on Sailfish OS)
Source1:        ipcalc.1
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja

%description
ipcalc provides a simple way to calculate IP information for a host or
network: netmask, broadcast, network prefix, address ranges, subnet
splitting and deaggregation, reverse DNS names, address classification,
for both IPv4 and IPv6, with human, JSON or shell output.
Built for Sailfish OS without MaxMind GeoIP support.

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%if 0%{?_chum}
Title: ipcalc
Type: console-application
DeveloperName: Nikos Mavrogiannopoulos
PackagedBy: Stéphane COLIN
Categories:
 - Network
 - Utility
AIRating: B
AINote: Upstream code untouched; spec file drafted with Claude, reviewed by the packager
Custom:
  Repo: https://gitlab.com/ipcalc/ipcalc
  PackagingRepo: https://github.com/bigbob-fun/ipcalc-sfos
Links:
  Homepage: https://gitlab.com/ipcalc/ipcalc
  Bugtracker: https://github.com/bigbob-fun/ipcalc-sfos/issues
%endif

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Manual page and documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
meson setup _build upstream --prefix=%{_prefix} --buildtype=plain \
  -Duse_maxminddb=disabled -Duse_runtime_linking=disabled
ninja -C _build %{?_smp_mflags} -v

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} ninja -C _build install
install -Dm0644 rpm/ipcalc.1 %{buildroot}%{_mandir}/man1/ipcalc.1

%check
# Some upstream tests rely on LD_PRELOAD fakes and on localhost resolving
# to "localhost", which does not hold in the OBS / SDK build sandbox.
meson test -C _build --print-errorlogs || :

%files
%license upstream/COPYING
%{_bindir}/ipcalc

%files doc
%doc upstream/README.md upstream/NEWS
%{_mandir}/man1/ipcalc.1*
