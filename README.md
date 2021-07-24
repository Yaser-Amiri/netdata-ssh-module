# Netdata SSH Module

----
This is a simple module for [Netdata](https://github.com/firehol/netdata) to add a chart to show failed authentication's count of SSH.

*I used and tested it on Debian based systems but I think it would work on CentOS if you change "path" field in SSH.conf to "/var/log/secure" and change owner of this file to netdata.*

----
## Usage
1. Clone repo

2. Run update.sh to install or update the module (needs root permission)

3. Make sure the `/var/log/auth.log` is readable for the netdata (Add `netdata` user to `adm` group by `usermod -aG adm netdata`)

4. Restart netdata

---
![screenshot](https://github.com/Yaser-Amiri/netdata-ssh-module/blob/master/screenshot.png "Screenshot")
