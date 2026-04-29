import subprocess
import optparse

## Get User Input
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="wifi_interface",help="wifi interface to change!")
    parse_object.add_option("-m", "--mac",dest="mac_address",help="MAC Address to change into!")

    return parse_object.parse_args()

## MAC Address Changer
def mac_address_changer(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig",user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

## Checking if MAC_Address has been changed
def control_new_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig",user_interface])
    print(ifconfig)


print("MAC_Changer Started !!")
## Calling get_user_input function and passing the tuples to mac_address_changer function
(user_input,arguments) = get_user_input()
mac_address_changer(user_input.wifi_interface,user_input.mac_address)
control_new_mac(user_input.wifi_interface)


print("MAC_Changer successfully Executed !!")
