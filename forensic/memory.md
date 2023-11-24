# Memory labyrynthe

I launched a strins command analysis
```bash
strings /path/to/labyrynthe | grep "tracker-extract"
```
## Tries
```
1387 --> 8caef7cfd1f24143d5b7f7048b4c1301a29ec767
1470 --> 2e8d241fa2ca9957d1b8fab2a3d479f07a2c963b
4137 --> 4b0601b3a1742659849c735f6f88c746b968705a
1395 --> 64bed117196c2624f38bb8da114684eeb96ff68a
5860 --> c2f5a18013ad18036c4e98811bfafd1624acd6e6  [correct !]
    uid=1000 pid=5860 comm="/usr/libexec/tracker-extract-3 " label="unconfined"
        tracker-extract

```

The output is as follows
```
libtracker-extract.so
/usr/lib/systemd/user/tracker-extract-3.service
.#invocation:tracker-extract-3.serviceb0317db1f1dc64d4
invocation:tracker-extract-3.service
tracker-extract-3-files.1000
[01;34mtracker-extract-3-files.1000
[01;34mtracker-extract-3-files.127
tracker-extract-3.service
tracker-extract-3.service
tracker-extract
tracker-extract-3.service
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
tracker-extract-3-files.127
/tmp/tracker-extract-3-files.1000/96e16e3e5b981df8a3ef4a3d11827a71
/tmp/tracker-extract-3-files.1000/9f325de977ae85fc2969c2e651449381
[01;34mtracker-extract-3-files.1000
[01;34mtracker-extract-3-files.127
Package: tracker-extract
Depends: libc6 (>= 2.34), libglib2.0-0 (>= 2.70.0), libtracker-sparql-3.0-0 (>= 3.3.0~beta), libupower-glib3 (>= 0.99.0), tracker-extract (= 3.3.0-1), init-system-helpers (>= 1.52), tracker (>= 3.3.0~), procps
/tmp/tracker-extract-3-files.1000/598f00fb1b50a8fe2d66f8070623db96
/tmp/tracker-extract-3-files.1000/e62bb2e0904db64f4a821cf8e863c63a
/tmp/tracker-extract-3-files.1000/e36ed2a6de69006e31d3b66b716e5f59
tracker-extract:amd64
libtracker-extract.so
$ORIGIN/../libtracker-extract
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/48d110bf430c3396707b1b90fdc04805
/tmp/tracker-extract-3-files.1000/d1f5c0d16eaec658bf991b8cf1c585f8
/tmp/tracker-extract-3-files.1000/b99b6282503e9f75ce5f18402edcb045
libtracker-extract.so
$ORIGIN/../libtracker-extract
/tmp/tracker-extract-3-files.1000/df430099622b3ac3837246278eee8bad
]: Started Tracker metadata extractor.cessfully activated service 'org.freedesktop.Tracker3.Miner.Extract'tract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")() vfuncs.ve() vfuncs./usr/lib/firefox/firefox " label="snap.firefox.firefox (enforce)") interface="org.freedesktop.FileManager1" member="ShowItems" error name="(unset)" requested_reply="0" destination=":1.126" (uid=1000 pid=4137 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")pparmor/profiles/snap.snap-store.ubuntu-software /var/lib/snapd/apparmor/profiles/snap.snap-store.ubuntu-software-local-file /var/lib/snapd/apparmor/profiles/snap.snapd-desktop-integration.hook.configure /var/lib/snapd/apparmor/profiles/snap.snapd-desktop-integration.snapd-desktop-integration]
/tmp/tracker-extract-3-files.1000/a93f7ed8df1f42122af8602e676e3fc8
/tmp/tracker-extract-3-files.1000/ef001b18511d2063ce65f498af4f431a
sion uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
ervice name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.3' (uid=127 pid=977 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Sep 20 10:44:46 ubuntu-2204 dbus-daemon[1395]: [session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
:46 dbus-daemon[1395]: [session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
libtracker-extract.so
$ORIGIN/../libtracker-extract
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/5d3e6dbf6f0abaf480daed440e1488c8
/tmp/tracker-extract-3-files.1000/433de97fe2917d7dd8fe83efaa8e7c9f
/tmp/tracker-extract-3-files.1000/b9825a2c2e1accb41678310d5f9fed06
/tmp/tracker-extract-3-files.1000/d580932e663badcf83e02b61499b6071
/tmp/tracker-extract-3-files.1000/495654ce16f66389f0f768a81388845d
/tmp/tracker-extract-3-files.1000/87e0c1495e6ba29beae0e396b7a564ad
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/70e9a5e584879cfa622397036218d318
/tmp/tracker-extract-3-files.1000/439800d8b9b074aa6cd2f60e6840508f
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/141f86d3021ac078106643ce95be29bf
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/7b3b6333f64e75758af59ec92b203745
/tmp/tracker-extract-3-files.1000/75459d3c7b4d41964ae20ecbd08e86ff
libtracker-extract.so
$ORIGIN/../libtracker-extract
/tmp/tracker-extract-3-files.1000/7a0f6afbbb3721d3bdafe63ff7d863dd
/tmp/tracker-extract-3-files.1000/2f7943719dfd33446bccbddae3f0ab68
/tmp/tracker-extract-3-files.1000/4158db6b73a3beeaad18385eedb0c9d7
/tmp/tracker-extract-3-files.1000/fbd78700ad0dc3655025733a3f87e41a
/tmp/tracker-extract-3-files.1000/65256d123078316c9f1cf454ce1e4b1a
dwz/x86_64-linux-gnu/tracker-extract.debug
dwz/x86_64-linux-gnu/tracker-extract.debug
dwz/x86_64-linux-gnu/tracker-extract.debug
dwz/x86_64-linux-gnu/tracker-extract.debug
ZP0 pid=1395] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
1395]: [session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
/tmp/tracker-extract-3-files.1000/bba7bb9c844b476347a7288347b8c44f
/tmp/tracker-extract-3-files.1000/98f1f63564ae1156525c386217b94c84
/tmp/tracker-extract-3-files.1000/98f1f63564ae1156525c386217b94c84
/tmp/tracker-extract-3-files.1000/98f1f63564ae1156525c386217b94c84
/tmp/tracker-extract-3-files.1000/98f1f63564ae1156525c386217b94c84
/tmp/tracker-extract-3-files.1000/98f1f63564ae1156525c386217b94c84
tracker-extract-3.service
uid=1000 pid=5860 comm="/usr/libexec/tracker-extract-3 " label="unconfined"
tracker-extract
libtracker-extract.so
$ORIGIN/../libtracker-extract
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/b75c565883cddaeff5a05a000da4ab26
/tmp/tracker-extract-3-files.1000/482841c49614c62d64746014a31f9ac7
Depends: bubblewrap, desktop-file-utils (>= 0.7), gsettings-desktop-schemas (>= 3.8.0), gvfs (>= 1.3.2), libglib2.0-data, libnautilus-extension1a (= 1:42.6-0ubuntu1), nautilus-data (= 1:42.6-0ubuntu1), shared-mime-info (>= 0.50), tracker (>= 3), tracker-miner-fs (>= 3), tracker-extract (>= 3), libatk1.0-0 (>= 1.32.0), libc6 (>= 2.34), libcairo-gobject2 (>= 1.10.0), libcairo2 (>= 1.14.0), libdbusmenu-glib4 (>= 0.4.2), libgdk-pixbuf-2.0-0 (>= 2.25.2), libgexiv2-2 (>= 0.14.0), libglib2.0-0 (>= 2.70.0), libgnome-autoar-0-0 (>= 0.4.0), libgnome-desktop-3-19 (>= 3.17.92), libgstreamer-plugins-base1.0-0 (>= 1.0.0), libgstreamer1.0-0 (>= 1.0.0), libgtk-3-0 (>= 3.23.1), libhandy-1-0 (>= 1.5.0), libpango-1.0-0 (>= 1.44.6), libselinux1 (>= 3.1~), libtracker-sparql-3.0-0 (>= 3.1.1), libunity9 (>= 3.4.6)
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/7b3b6333f64e75758af59ec92b203745
/tmp/tracker-extract-3-files.1000/75459d3c7b4d41964ae20ecbd08e86ff
/tmp/tracker-extract-3-files.1000/ba41d25f7f31b7d3f0cee8fd25045215
/tmp/tracker-extract-3-files.1000/2ae40a651becd869f6fe54179ef7b4e8
/tmp/tracker-extract-3-files.1000/952a184eaf90d8a8ba9ec0b20967369d
/tmp/tracker-extract-3-files.1000/d8fcd19e6058f47e9d911df7e111df9e
/tmp/tracker-extract-3-files.1000/c098a7030e88647e401b24d0d35e4785
/tmp/tracker-extract-3-files.1000/9e0615e63f255a0e2e638650f1d076d6
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000
/tmp/tracker-extract-3-files.1000/141f86d3021ac078106643ce95be29bf
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/ebc5e71d414e87b2fa53d4cdc7f273ea
/tmp/tracker-extract-3-files.1000/f1bfaaf6b7b7997bbe6fc16e72399650
/tmp/tracker-extract-3-files.1000/4681eaf73aee53648f1d6616ddad7d43
/tmp/tracker-extract-3-files.1000/f63bbdd6b7f0511e31c754e59b810f8d
/tmp/tracker-extract-3-files.1000/da52724cff20c77d07535ed43918dc04
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/3a42d7637035ebdbc516ca900a4b565a
/tmp/tracker-extract-3-files.1000/21ff2822f4640c7ab6a43bb4086f2931
/tmp/tracker-extract-3-files.1000/8146d42f856c63887cf04abff3027821
/tmp/tracker-extract-3-files.1000/3c7ba284ab32357e4ca63140c4d7e331
/tmp/tracker-extract-3-files.1000/4d9e6cdc6ea5cf7e0262bd69bb511c05
/tmp/tracker-extract-3-files.1000/6889098f405972035bb315a81085b011
/tmp/tracker-extract-3-files.1000/d04797f462957a4263fcae26be5e69fd
/tmp/tracker-extract-3-files.1000/37228c1338ee084340ccbe04de254cff
/tmp/tracker-extract-3-files.1000/cf14e7d9cc544722d7af8dd040d3b535
USER_UNIT=tracker-extract-3.service
dwz/x86_64-linux-gnu/tracker-extract.debug
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
Exec=/app/libexec/tracker-extract-3 --domain-ontology /usr/share/tracker3/domain-ontologies/org.gnome.Nautilus.domain.rule
/app/libexec/tracker-extract-3 --domain-ontology /usr/share/tracker3/domain-ontologies/org.gnome.Nautilus.domain.rule
Exec=/usr/libexec/tracker-extract-3 
SystemdService=tracker-extract-3.service
/tmp/tracker-extract-3-files.1000/141f86d3021ac078106643ce95be29bf
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/52ab79e410d9d75981bd69acb979a249
/tmp/tracker-extract-3-files.1000/9f036ee1c363a99ff534ea1b4afa75dd
tracker-extract-3
/tmp/tracker-extract-3-files.1000/0cf9aa73df1f19a370b6a47d0bf1908d
/tmp/tracker-extract-3-files.1000/2c78a1ff0aacaccb3373406148003b69
/tmp/tracker-extract-3-files.1000/66e99cb7fe06a25f17cb2ca4ccf6b9fa
/tmp/tracker-extract-3-files.1000/9f8275bb876e99ba26a7e1038823b033
/usr/lib/x86_64-linux-gnu/tracker-miners-3.0/libtracker-extract.so
libtracker-extract.so
libtracker-extract.so
IDENTIFIER=tracker-extract-3
/tmp/tracker-extract-3-files.1000/ba1b5fbf3b62b4f3c06b27c61804be5d
/tmp/tracker-extract-3-files.1000/4b750007a29ce912ef9d50145652b8ea
Sep 20 10:40:09 ubuntu-2204 dbus-daemon[1395]: [session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
/tmp/tracker-extract-3-files.1000/a2a478bba3f5b3cae5fc096490abded4
/tmp/tracker-extract-3-files.1000/de9765cd7566e605ce8ffe5c53c326fe
/tmp/tracker-extract-3-files.1000/55f1aaeb9858ce3b034209914eaa9459
tracker-extract-3
/tmp/tracker-extract-3-files.1000/ec07b2942430757dbe531cf4aa6b0903
tracker-extract
/tmp/tracker-extract-3-files.1000/578f08c3b30e3b0b0575b2c9e15594ee
/tmp/tracker-extract-3-files.1000/c5c3b03e0258be7022f8ec00211aa442
ser.slice/user-1000.slice/user@1000.service/background.slice/tracker-extract-3.service/cpu.stat
/tmp/tracker-extract-3-files.1000/1c9e1a4e058f6fef1f9c614bbee65aae
tracker-extract
/tmp/tracker-extract-3-files.1000/42a6b110dc672e274e59d8eb9e6d2132
/tmp/tracker-extract-3-files.1000/a20b50fd3e8cbe0dfe4ca465f5f87348
/tmp/tracker-extract-3-files.1000/61798c29183b10f2424fe3421478bd2b
/tmp/tracker-extract-3-files.1000/caef44ccd570f5ace72acb02e545274b
/usr/libexec/tracker-extract-3
tracker-extract-3.service
tracker-extract-3.service
libtracker-extract.so
$ORIGIN/../libtracker-extract
/tmp/tracker-extract-3-files.1000/5c72f94cd560234ce9b34e4a920ff0d9
/tmp/tracker-extract-3-files.1000/2eabb6135c7e0d1e7e82a6eaeab4f90c
 uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
/usr/lib/systemd/user/tracker-extract-3.service
untu/tmp/tracker-extract-3-files.1000/5bff65b5017cfa1a1d395ea4f00f1dbf
/tracker-extract-3-files.1000/4158db6b73a3beeaad18385eedb0c9d7
/tracker-extract-3-files.1000/fbd78700ad0dc3655025733a3f87e41a
/tracker-extract-3-files.1000/19b02f93f09a84a1274ce2b3ce21a841
/tracker-extract-3-files.1000/433de97fe2917d7dd8fe83efaa8e7c9f
/tracker-extract-3-files.1000/14235e3aabf2775aa83750a10f9598c8
/tracker-extract-3-files.1000/27a9569c1decfd20be88523c0c9343cb
/tracker-extract-3-files.1000/495654ce16f66389f0f768a81388845d
/tmp/tracker-extract-3-files.1000/ba1b5fbf3b62b4f3c06b27c61804be5d
/tmp/tracker-extract-3-files.1000/4b750007a29ce912ef9d50145652b8ea
/tmp/tracker-extract-3-files.1000/19b02f93f09a84a1274ce2b3ce21a841
/tmp/tracker-extract-3-files.1000/214aa1220b2a89ad3a149622089fa137
T=tracker-extract-3.service
ser.slice/user-1000.slice/user@1000.service/background.slice/tracker-extract-3.service/cgroup.events
[01;34mtracker-extract-3-files.1000
[01;34mtracker-extract-3-files.127
/tmp/tracker-extract-3-files.1000/ba10c996314868d0eafe208d58279b9d
/tmp/tracker-extract-3-files.1000/bb4825bbd808f549eb243f03287a3105
 uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
/usr/libexec/tracker-extract-3
tracker-extract-3.service
/usr/lib/systemd/user/tracker-extract-3.service
/tmp/tracker-extract-3-files.1000/42a6b110dc672e274e59d8eb9e6d2132
/tmp/tracker-extract-3-files.1000/a20b50fd3e8cbe0dfe4ca465f5f87348
/tmp/tracker-extract-3-files.1000/61798c29183b10f2424fe3421478bd2b
/tmp/tracker-extract-3-files.1000/caef44ccd570f5ace72acb02e545274b
/tmp/tracker-extract-3-files.1000/69efaaa0077aa7a992190f74f40782dd
/tmp/tracker-extract-3-files.1000/af4ef7764e51c29268768fd8c116cc7c
/usr/lib/systemd/user/tracker-extract-3.service
tracker-extract-3.service
/tmp/tracker-extract-3-files.1000/b26ed01e675627b10cdb960673dbb2c0
/tmp/tracker-extract-3-files.1000/56dbba1bf0cae6286e6e958ac6db014a
/usr/lib/systemd/user/tracker-extract-3.service
MESSAGE=[session uid=1000 pid=1395] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
USER_UNIT=tracker-extract-3.service
MESSAGE=[session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
untu/tmp/tracker-extract-3-files.1000/3c7ba284ab32357e4ca63140c4d7e331
untu/tmp/tracker-extract-3-files.1000/a2cbce7b2cdfea57f07e7c86a0716852
ZP0 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
/tmp/tracker-extract-3-files.1000/05ce9f3c061e07c7cae33f66496e9330
/tracker-extract-3-files.1000/d04797f462957a4263fcae26be5e69fd
tracker-extract-3
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/4af036905d140744b625abfed3589ebe
/tmp/tracker-extract-3-files.1000/e3064a28d2562b95f234eb80a9b0cd82
MESSAGE=[session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
/tmp/tracker-extract-3-files.1000/d6108e756851b2a71c47ce77b6844842
/tmp/tracker-extract-3-files.1000/4b47d9b416c64c37a528dfd49dc8efad
/tmp/tracker-extract-3-files.1000/ee7b50f8c5c73e834c4132067377a705
/tmp/tracker-extract-3-files.1000/b0ff1ec179c560ecf3cafe7ef17b417e
/tmp/tracker-extract-3-files.1000/16b2f4ec094757abbe32fe9f35a01af2
/tmp/tracker-extract-3-files.1000/a7a8ebda64308ef871d09e0314d458d0
/tmp/tracker-extract-3-files.1000/180c1e0d9e8e0b3f43a59684388b5802
/tmp/tracker-extract-3-files.1000/f87ae70b5f6befc0740fa7f511e9a4b4
/tmp/tracker-extract-3-files.1000/bba7bb9c844b476347a7288347b8c44f
tracker-extract-3
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/e2b3ce92865dee3614cf458f5c172990
/tmp/tracker-extract-3-files.1000/bb60c0b8003d9d54f515ff582329de36
/tmp/tracker-extract-3-files.1000/9024e524ef52a221290c35c2ceeb409d
/tmp/tracker-extract-3-files.1000/aa124a123c56d3ee1eb54f5d9b756793
/tmp/tracker-extract-3-files.1000/bba7bb9c844b476347a7288347b8c44f
/tracker-extract-3-files.1000/4158db6b73a3beeaad18385eedb0c9d7
/tracker-extract-3-files.1000/fbd78700ad0dc3655025733a3f87e41a
/tracker-extract-3-files.1000/19b02f93f09a84a1274ce2b3ce21a841
/tracker-extract-3-files.1000/433de97fe2917d7dd8fe83efaa8e7c9f
/tracker-extract-3-files.1000/14235e3aabf2775aa83750a10f9598c8
/tracker-extract-3-files.1000/27a9569c1decfd20be88523c0c9343cb
/tracker-extract-3-files.1000/495654ce16f66389f0f768a81388845d
/tracker-extract-3-files.1000/4d9e6cdc6ea5cf7e0262bd69bb511c05
64-linux-gnu/tracker-extract.debug
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
IDENTIFIER=tracker-extract-3
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/usr/libexec/tracker-extract-3
/usr/libexec/tracker-extract-3
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/bba7bb9c844b476347a7288347b8c44f
/usr/lib/systemd/user/tracker-extract-3.service
MESSAGE=[session uid=1000 pid=1395] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
/tmp/tracker-extract-3-files.1000/16eb85f88318021338c064162289a598
/tmp/tracker-extract-3-files.1000/97c4704ce3c5489de0eeb4ae32d82009
/tmp/tracker-extract-3-files.1000/be0dc4bdff409b3a70632b95f2a3c758
Sep 20 10:44:46 ubuntu-2204 dbus-daemon[1395]: [session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
tracker-extract-3
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
MESSAGE=[session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
/usr/libexec/tracker-extract-3
/tmp/tracker-extract-3-files.1000/4e6b9a2a19cb6377de6424ab658c96e1
/tmp/tracker-extract-3-files.1000/99760083ebfbdd79cfe221bde9e8e029
/tmp/tracker-extract-3-files.1000/ade9fad7ce5e5f837880cbd31fffc054
/tmp/tracker-extract-3-files.1000/914b6e98daa9b41bc91eafc13a7e57c3
64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/c0bcd28496a8d200b060e681221cb0ef
/tmp/tracker-extract-3-files.1000/d2b2c01d9d7db05171fbd9bf5129b619
/tmp/tracker-extract-3-files.1000/d27ae53be40a5d884fc205a324269357
/tmp/tracker-extract-3-files.1000/98f1f63564ae1156525c386217b94c84
/tmp/tracker-extract-3-files.1000/a2cbce7b2cdfea57f07e7c86a0716852
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/05ce9f3c061e07c7cae33f66496e9330
/tmp/tracker-extract-3-files.1000/7937fa0b3f076331fa0b3a8b8e924564
T=tracker-extract-3.service
ser.slice/user-1000.slice/user@1000.service/background.slice/tracker-extract-3.service/cgroup.events
[01;34mtracker-extract-3-files.1000
[01;34mtracker-extract-3-files.127
/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/background.slice/tracker-extract-3.service
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/543ca2b99cdeb927463a2fa0077c011a
/tmp/tracker-extract-3-files.1000/3d667dec38d8d163c015808d05f43a94
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
Setting up watch on tracker-extract at %s (autostart: %s)
tracker-extract vanished, maybe restarting.
/tmp/tracker-extract-3-files.1000/4be22b68ea164741c036e41932a1229a
/tmp/tracker-extract-3-files.1000/9ce62ae527123dd06afae6786bf3d2d8
/tmp/tracker-extract-3-files.1000/f500cd590095ab702742799783b017a1
dwz/x86_64-linux-gnu/tracker-extract.debug
untu/tmp/tracker-extract-3-files.1000/3c7ba284ab32357e4ca63140c4d7e331
/tmp/tracker-extract-3-files.1000/bdd3c1fbcc35995018ea334bdf0cdbdf
/tmp/tracker-extract-3-files.1000/c0875397b46b51ecfc6d06dbfdb79d== NULL
/tmp/tracker-extract-3-files.1000/4e6b9a2a19cb6377de6424ab658c96e1
/tmp/tracker-extract-3-files.1000/6a181efdd680a0db809132b87a8d6185
/tmp/tracker-extract-3-files.1000/6ff4505f642d40d21a6e9aa837473d3e
/tmp/tracker-extract-3-files.1000/cf077e33f120996270da44730256d6ad
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/c18c45749394b468b7b6e83175c44e43
dwz/x86_64-linux-gnu/tracker-extract.debug
/user.slice/user-1000.slice/user@1000.service/background.slice/tracker-extract-3.service
/tmp/tracker-extract-3-files.1000/c8f5d49a096e7438e3e3e09149b608a8
dwz/x86_64-linux-gnu/tracker-extract.debug
/usr/lib/debug/.dwz/x86_64-linux-gnu/tracker-extract.debug
/usr/libexec/tracker-extract-3
/tmp/tracker-extract-3-files.1000/944ab1922a198473669ef62aa3eead2c
/tmp/tracker-extract-3-files.1000/141f86d3021ac078106643ce95be29bf
/tmp/tracker-extract-3-files.1000/e3cab445f9ca15169e7900d7e893167c
/tmp/tracker-extract-3-files.1000/e5fa93d5df238aa7c83c1594ff3654db
untu/tmp/tracker-extract-3-files.1000/a20b50fd3e8cbe0dfe4ca465f5f87348
tracker-extract-3-files.1000/
tracker-extract-3-files.127/
MESSAGE=[session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=1000 pid=1470 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
-gnu/tracker-extract.debug
dwz/x86_64-linux-gnu/tracker-extract.debug
/tmp/tracker-extract-3-files.1000/ccbb68fba407d265aa8ef12b0c6447b2
dwz/x86_64-linux-gnu/tracker-extract.debug
tracker-extract-3.service
/usr/libexec/tracker-extract-3 
/tmp/tracker-extract-3-files.1000/4384d517198b2f3f5869a2875df83f38
/tmp/tracker-extract-3-files.1000/c9be787ff5720e556481621550784b61
dwz/x86_64-linux-gnu/tracker-extract.debug
tracker-extract-3.service
/tmp/tracker-extract-3-files.1000/3efc7b164417fd8e7738c551510b5ce8
/tmp/tracker-extract-3-files.1000/22e6dba0310ade2f16433025a57a8d1c
/tmp/tracker-extract-3-files.1000/0ae9d0b2b1b453e091a602730b9e2255
/tmp/tracker-extract-3-files.1000/d8c706686daa8074737aecf213172be3
ZP:35 dbus-daemon[1395]: [session uid=1000 pid=1395] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.1' (uid=1000 pid=1387 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
```