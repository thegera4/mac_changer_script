#!/usr/bin/env python
# subprocess module allows us to run OS commands (pwd, ls, cd, ifconfig, etc)
import subprocess
# optparse module allows us to parse command-line options (use arguments)
import optparse
# re module allows us to use regular expressions
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Set the new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


opts = get_arguments()

current_mac = get_current_mac(opts.interface)
print("Current MAC = " + str(current_mac))

change_mac(opts.interface, opts.new_mac)

current_mac = get_current_mac(opts.interface)
if current_mac == opts.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")


# interface = options.interface  # interface = raw_input("interface > ")  # input() for python 3
# new_mac = options.new_mac  # new_mac = raw_input("new MAC > ")
