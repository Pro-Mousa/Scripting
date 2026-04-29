import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="wifi_interface",help="wifi interface to change!")
parse_object.add_option("-m", "--mac",dest="mac_address",help="MAC Address to change into!")

(user_inputs, arguments) = parse_object.parse_args()

user_interface = user_inputs.wifi_interface
user_mac_address = user_inputs.mac_address

print("MacChanger Started !!")

subprocess.call(["ifconfig", user_interface, "down"])
subprocess.call(["ifconfig",user_interface, "hw", "ether", user_mac_address])
subprocess.call(["ifconfig", user_interface, "up"])

print("MacChanger successfully Executed !!")

