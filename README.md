<!-- Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0F2027,100:2C5364&section=header&text=MAC%20Address%20Changer&fontSize=50&fontColor=ffffff&desc=Python%20Networking%20Tool&descSize=22&descAlignY=65" alt="header" />
</p>

<p align="center">
  <b>🔧 MAC Address Changer (Python)</b><br>
  <i>A simple Python script to change the MAC address of a network interface on Linux systems.</i>
</p>

---

<h2>📌 Features</h2>

<ul>
  <li>Change MAC address using command-line arguments</li>
  <li>Supports both short and long options</li>
  <li>Verifies whether the MAC address change was successful</li>
</ul>

---

<h2>⚙️ Requirements</h2>

<ul>
  <li>Python 3 (or Python 2 if still installed)</li>
  <li>Linux-based OS (uses ifconfig)</li>
  <li>Root/sudo privileges</li>
</ul>

---

<h2>📥 Installation</h2>

<p>Clone the repository:</p>

<pre>
git clone https://github.com/your-username/mac-changer.git
cd mac-changer
</pre>

---

<h2>🚀 Usage</h2>

<p>⚠️ You must run this script with sudo/root privileges</p>

<h3>Using Python 3</h3>

<pre>
sudo python3 mac_changer.py -i &lt;interface&gt; -m &lt;MAC_Address&gt;

or

sudo python3 mac_changer.py --interface &lt;interface&gt; --mac &lt;MAC_Address&gt;
</pre>

<h3>Using Python (default)</h3>

<pre>
sudo python mac_changer.py -i &lt;interface&gt; -m &lt;MAC_Address&gt;

or

sudo python mac_changer.py --interface &lt;interface&gt; --mac &lt;MAC_Address&gt;
</pre>

---

<h2>🧪 Example</h2>

<pre>
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
</pre>

---

<h2>🧠 How It Works</h2>

<ul>
  <li>Takes user input for:
    <ul>
      <li>Network interface (-i or --interface)</li>
      <li>New MAC address (-m or --mac)</li>
    </ul>
  </li>
  <li>Disables the interface</li>
  <li>Changes the MAC address</li>
  <li>Re-enables the interface</li>
  <li>Verifies the change using regex</li>
</ul>

---

<h2>📄 Script Overview</h2>

<ul>
  <li><code>get_user_input()</code> → Parses CLI arguments</li>
  <li><code>mac_address_changer()</code> → Changes MAC address</li>
  <li><code>control_new_mac()</code> → Confirms MAC address update</li>
</ul>

---

<h2>⚠️ Important Notes</h2>

<ul>
  <li>Works best on systems with ifconfig installed</li>
  <li>May not work on modern systems using only ip command</li>
  <li>Ensure the interface name is correct (eth0, wlan0, etc.)</li>
</ul>

---

<h2>🛑 Disclaimer</h2>

<p>
This tool is for educational and ethical use only.<br>
Do not use it on networks or systems without proper authorization.
</p>

---

<h2>📬 Contributing</h2>

<p>
Feel free to fork this repo and submit pull requests to improve functionality.
</p>

---

<h2>📜 License</h2>

<p>
This project is licensed under the MIT License.<br>
@Pro-Mousa<br>
© 2026
</p>

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:0F2027,100:2C5364&section=footer" alt="footer" />
</p>
