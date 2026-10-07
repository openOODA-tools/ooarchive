Name:           ooarchive
Version:        0.1.0
Release:        1%{?dist}
Summary:        Deterministic reproducible archive builder guaranteeing byte-for-byte outputs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooarchive
Source0:        ooarchive-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooarchive is a sovereign, capability-bounded ARCHIVE PACKER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooarchive
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooarchive-uninstall

%files
/usr/bin/ooarchive
/usr/bin/ooarchive-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
