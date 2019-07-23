# Netdata SSH Module

----
This is a simple module for [Netdata](https://github.com/firehol/netdata) to add a chart to show failed authentication's count of SSH.

*Now this module tested on Debian based systems. I'll test it on CentOS soon. But I think it would work on CentOS if you  change "path" field in SSH.conf to "/var/log/secure" and change owner of this file to netdata.*

----
## Usage
1. Clone repo

2. Run update.sh to install or update module to netdata root

3. Make sure the /var/log/auth.log is readable for the user netdata, e.g. by 
   chgrp -G adm netdata

4. Control if the module is working by running as user netdata:

   /usr/{lib,libexec}/netdata/plugins.d/python.d.plugin SSH trace debug

5. Restart the Netdata service.

---
![screenshot](https://github.com/Yaser-Amiri/netdata-ssh-module/blob/master/screenshot.png "Screenshot")
