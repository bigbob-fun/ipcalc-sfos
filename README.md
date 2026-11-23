# ipcalc for Sailfish OS

Packaging of [ipcalc](https://gitlab.com/ipcalc/ipcalc) (the IPv4/IPv6
calculator also shipped by Fedora and RHEL) for Sailfish OS, built on the
Sailfish OS OBS for [SailfishOS:Chum](https://github.com/sailfishos-chum/main).

- `upstream/` : git submodule of the upstream project, pinned to the released tag
- `rpm/` : spec file and a pre-generated manual page (ronn is not available on Sailfish OS)

Built without MaxMind GeoIP support (libmaxminddb is not available on Sailfish OS).

## Install

From the SailfishOS:Chum GUI, or on the command line:

    pkcon install ipcalc

## Usage

    ipcalc 192.168.1.0/24
    ipcalc -S 26 10.0.0.0/24
    ipcalc -6 2001:db8::1/64

Packaging issues: please open an issue here. Upstream issues:
https://gitlab.com/ipcalc/ipcalc/-/issues

---
*AI disclosure: this packaging was prepared interactively with Claude Code (Anthropic's AI coding assistant). Every action was requested, reviewed and approved by me; nothing was decided or published autonomously.*
