🔧 MAC Address Changer (Python)

A simple Python script to change the MAC address of a network interface on Linux systems.

📌 Features
Change MAC address using command-line arguments
Supports both short and long options
Verifies whether the MAC address change was successful
⚙️ Requirements
Python 3 (or Python 2 if still installed)
Linux-based OS (uses ifconfig)
Root/sudo privileges
📥 Installation

Clone the repository:

git clone https://github.com/your-username/mac-changer.git
cd mac-changer
🚀 Usage

⚠️ You must run this script with sudo/root privileges

Using Python 3
sudo python3 mac_changer.py -i <interface> -m <MAC_Address>

or

sudo python3 mac_changer.py --interface <interface> --mac <MAC_Address>
Using Python (default)
sudo python mac_changer.py -i <interface> -m <MAC_Address>

or

sudo python mac_changer.py --interface <interface> --mac <MAC_Address>
🧪 Example
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
🧠 How It Works
Takes user input for:
Network interface (-i or --interface)
New MAC address (-m or --mac)
Disables the interface
Changes the MAC address
Re-enables the interface
Verifies the change using regex
📄 Script Overview
get_user_input() → Parses CLI arguments
mac_address_changer() → Changes MAC address
control_new_mac() → Confirms MAC address update
⚠️ Important Notes
Works best on systems with ifconfig installed
May not work on modern systems using only ip command
Ensure the interface name is correct (eth0, wlan0, etc.)
🛑 Disclaimer

This tool is for educational and ethical use only.
Do not use it on networks or systems without proper authorization.

📬 Contributing

Feel free to fork this repo and submit pull requests to improve functionality.

📜 License

This project is licensed under the MIT License.
@Pro-Mousa
© 2026
