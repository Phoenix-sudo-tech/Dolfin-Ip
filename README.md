

# 🌐 IP Lookup Tool

A powerful and user-friendly Python tool to gather detailed information about any public IP address. It performs IP geolocation, WHOIS lookup, reverse DNS lookup, and logs all results for further analysis.

> 🔧 Developed by [@ethicalphoenix](https://github.com/Phoenix-sudo-tech)

---

## 🚀 Features

- 📍 Get accurate IP geolocation data (city, region, country, coordinates)
- 🛰️ View Google Maps location link
- 📄 Perform WHOIS lookup for detailed network information
- 🔁 Reverse DNS lookup to resolve IP to domain (if available)
- 📂 Auto-logs results with timestamp in a clean format
- 🎨 Colorful terminal output for better readability
- 🛠️ Automatically installs required Python modules

---

## 🖥️ Screenshots

![Terminal Screenshot] ![1000472117](https://github.com/user-attachments/assets/81c8c011-62d0-47b7-847d-789cd3b551a5)
![1000472116](https://github.com/user-attachments/assets/1a83e0b0-e076-4cb5-8a66-ab5b2f1cdc4f)
![1000472115](https://github.com/user-attachments/assets/a6ff842f-520f-4663-b174-97f0f4d65610)

---

## 📦 Requirements

- Python 3.6+
- Internet connection

Required Python packages (auto-installed if missing):
- `requests`
- `geopy`
- `ipwhois`
- `termcolor`

---

## 📥 Installation

### 🔁 Clone the repository
```bash

pip install geopy --break-system-packages    
pip install ipwhois --break-system-packages  
pip install geopy --break-system-packages  


git clone https://github.com/yourusername/ip-lookup-tool.git
cd ip-lookup-tool

▶️ Run the tool

python3 ip_lookup_tool.py


---

✏️ Usage

1. Run the script.


2. Enter a valid public IP address (e.g., 8.8.8.8).


3. The tool will:

Fetch location data

Run a WHOIS query

Perform reverse DNS lookup



4. Save the full report in the logs/ folder.




---

📁 Example Output

🔸 Enter an IP address: 8.8.8.8

🌍 Location Info
City: Mountain View
Region: California
Country: US
Coordinates: 37.4056, -122.0775
ISP/Org: Google LLC
Google Maps: https://www.google.com/maps?q=37.4056,-122.0775

🔄 Reverse DNS
dns.google

📄 WHOIS Info
{
  "name": "GOOGLE",
  "handle": "NET-8-8-8-0-1",
  ...
}

📝 Saved report to logs/1.txt


---

🛡️ Legal Disclaimer

This tool is intended for educational and legitimate network diagnostic purposes only. Unauthorized usage on IPs without permission may violate privacy or cyber laws in your region.


---

👨‍💻 Author

@ethicalphoenix
Instagram / GitHub / LinkedIn: add your handles here


---

⭐ Support

If you found this tool useful:

⭐ Star the repo

🐞 Report issues or suggestions via GitHub Issues



---

📜 License

MIT License – see LICENSE file for details.

---



