# Netdata SSH Module

----
This is a simple module for [Netdata](https://github.com/firehol/netdata) to add a chart to show failed authentication's count of SSH.

*Now this module works just on Debian based systems. I'll add supporting of CentOS soon.*

----
## Usage
1. Clone repo and copy SSH.chart.py to /usr/libexec/netdata/python.d/SSH.chart.py and change it's owner to *netdata*
(sudo chown netdata:netdata /usr/libexec/netdata/python.d/SSH.chart)

2. Copy SSH.conf to /etc/netdata/python.d/SSH.conf and change its owner to netdata too.

3. Restart the Netdata service.
