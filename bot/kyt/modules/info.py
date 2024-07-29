from kyt import *
from telethon import Button, events
import subprocess
import time

# Fungsi untuk mendapatkan status layanan
def get_service_status(service_name):
    try:
        status_output = subprocess.check_output(f'systemctl is-active {service_name}', shell=True, stderr=subprocess.STDOUT, text=True).strip()
        return "💚" if status_output == "active" else "💔"
    except subprocess.CalledProcessError:
        return "💔"

def get_initd_service_status(service_name):
    try:
        status_output = subprocess.check_output(f'/etc/init.d/{service_name} status', shell=True, stderr=subprocess.STDOUT, text=True).strip()
        if "active" in status_output.lower():
            return "💚"
        else:
            return "💔"
    except subprocess.CalledProcessError:
        return "💔"

# Event handler untuk tombol info
@bot.on(events.CallbackQuery(data=b'info'))
async def info_vps(event):
    async def info_vps_(event):
        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(3)
        await event.edit("`Processing Info Service Server...`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(2)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(3)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(2)
        await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        time.sleep(1)
        await event.edit("`Wait.. Setting up Server Data`")

        # Mendapatkan status dari beberapa layanan
        services_status = {
            "Nginx      ": get_service_status("nginx"),
            "SSHWS      ": get_service_status("ws-stunnel"),
            "OpenVPN    ": get_service_status("openvpn"),
            "Xray TLS   ": get_service_status("xray"),
            "Xray N-TLS ": get_service_status("xray"),
            "VLESS TLS  ": get_service_status("xray"),
            "VLESS N-TLS": get_service_status("xray"),
            "Trojan     ": get_service_status("xray"),
            "Dropbear   ": get_initd_service_status("dropbear"),
            "Stunnel    ": get_initd_service_status("stunnel4"),
            "SSH        ": get_initd_service_status("ssh"),
            "Vnstat     ": get_initd_service_status("vnstat"),
            "Crontab    ": get_initd_service_status("cron"),
            "Fail2ban   ": get_initd_service_status("fail2ban"),
            "WS TLS     ": get_service_status("ws-stunnel.service"),
            "WS OpenVPN ": get_service_status("ws-ovpn"),
            "SSLH       ": get_service_status("sslh"),
            "UDP Custom ": get_service_status("udp-custom"),
            "SDNS Server": get_service_status("server"),
            "SDNS Client": get_service_status("client")
        }

        # Membuat pesan status layanan
        status_message = "\n".join([f"**◈**   `{service_name} :`     **{status}**" for service_name, status in services_status.items()])

        await event.respond(f"""
━━━━━━━━━━━━━━━━━━━━━━━
    **INFO STATUS SERVICE SERVER**
━━━━━━━━━━━━━━━━━━━━━━━
{status_message}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ @alawivpn**
━━━━━━━━━━━━━━━━━━━━━━━
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await info_vps_(event)
    else:
        await event.answer("Access Denied", alert=True)

