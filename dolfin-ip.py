#!/usr/bin/env python3

import os
import sys
import time
import json
import socket
import subprocess
from datetime import datetime
import ipaddress

# Spinner Animation
def loading_animation(message, duration=3):
    chars = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{message} {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    print('\r' + ' ' * (len(message) + 2), end='\r')

# Auto-install required modules
required_modules = ["requests", "geopy", "ipwhois", "termcolor"]

def install_module(module):
    subprocess.run([sys.executable, "-m", "pip", "install", module, "--quiet"])

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"🔧 Installing {module}...")
        install_module(module)

from requests import get
from geopy.geocoders import Nominatim
from ipwhois import IPWhois
from termcolor import colored

# IP Format Validation
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Show ASCII Banner
def show_banner():
    banner = r"""
     ____        _  __ _
    |  _ \  ___ | |/ _(_)|\   |
    | | | |/ _ \| | |_| || \  |
    | |_| | (_) | |  _| ||  \ |- ip
    |____/ \___/|_|_| |_||   \|
         Developed by @ethicalphoenix
    """
    print(colored(banner, "cyan"))

# Save log to file
def save_log(ip, location_info, whois_data, reverse_dns_info):
    os.makedirs("logs", exist_ok=True)
    existing_files = os.listdir("logs")
    log_number = len(existing_files) + 1
    filename = f"logs/{log_number}.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as f:
        f.write(f"🕒 Time: {timestamp}\n")
        f.write("🔹 IP: " + ip + "\n\n")
        f.write("🌍 Location Info\n" + location_info + "\n")
        f.write("🔄 Reverse DNS\n" + reverse_dns_info + "\n\n")
        f.write("📄 WHOIS Info\n" + whois_data + "\n")

    print(colored(f"\n📝 Saved report to {filename}", "green"))

# IP Geolocation Lookup
def get_ip_info(ip):
    try:
        loading_animation("📡 Gathering IP info", 3)
        response = get(f"https://ipinfo.io/{ip}/json", timeout=5).json()
        loc = response.get("loc", "").split(",")
        latitude = loc[0] if len(loc) > 1 else "N/A"
        longitude = loc[1] if len(loc) > 1 else "N/A"
        city = response.get("city", "N/A")
        region = response.get("region", "N/A")
        country = response.get("country", "N/A")
        postal = response.get("postal", "N/A")
        org = response.get("org", "N/A")
        timezone = response.get("timezone", "N/A")

        info = (
            f"City: {city}\n"
            f"Region: {region}\n"
            f"Country: {country}\n"
            f"Postal Code: {postal}\n"
            f"Coordinates: {latitude}, {longitude}\n"
            f"ISP/Org: {org}\n"
            f"Timezone: {timezone}\n"
            f"Google Maps: https://www.google.com/maps?q={latitude},{longitude}"
        )

        print(colored("\n🌍 Location Info", "green"))
        print(info)
        return info

    except Exception as e:
        err = f"❌ Error fetching IP info: {e}"
        print(colored(err, "red"))
        return err

# WHOIS Lookup
def get_whois(ip):
    try:
        loading_animation("🔍 Running WHOIS", 2)
        obj = IPWhois(ip)
        result = obj.lookup_rdap()
        whois_json = json.dumps(result["network"], indent=2)
        print(colored("\n📄 WHOIS Info", "yellow"))
        print(whois_json)
        return whois_json
    except Exception as e:
        err = f"❌ WHOIS error: {e}"
        print(colored(err, "red"))
        return err

# Reverse DNS Lookup
def reverse_dns(ip):
    try:
        host = socket.gethostbyaddr(ip)[0]
        result = f"Reverse DNS: {host}"
    except Exception:
        result = "Reverse DNS: Not available"
    print(colored("\n🔄 Reverse DNS", "magenta"))
    print(result)
    return result

# Main Function
def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_banner()
    ip = input(colored("🔸 Enter an IP address: ", "blue")).strip()
    if not ip:
        print(colored("⚠️ No IP entered. Exiting.", "red"))
        return

    if not is_valid_ip(ip):
        print(colored("⚠️ Invalid IP format. Please enter a valid IP address.", "red"))
        return

    loc_info = get_ip_info(ip)
    dns_info = reverse_dns(ip)
    whois_info = get_whois(ip)
    save_log(ip, loc_info, whois_info, dns_info)

if __name__ == "__main__":
    main()