#!/usr/bin/env python

import subprocess
# subprocess module allows us to spawn new processes, run OS commands,
# connect to their input/output/error pipes, and obtain their return codes.

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
