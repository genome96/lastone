from kyt import *

from telethon import events, Button
import time
import subprocess

@bot.on(events.CallbackQuery(data=b'update'))
async def update_(event):
    cmd = 'update'
    
    await event.edit("Processing.")
    time.sleep(0.5)
    await event.edit("Processing..")
    time.sleep(0.5)
    await event.edit("Processing...")
    time.sleep(0.5)
    await event.edit("Processing....")
    time.sleep(1)
    await event.edit("`Processing Update Script Server...`")
    time.sleep(1)
    await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 100%\n█████████████████████████ `")
    
    await event.edit("""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ UPDATE SCRIPT SERVER**
**◈ DONE**
━━━━━━━━━━━━━━━━━━━━━━━
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])
    
    subprocess.check_output(cmd, shell=True)

    sender = await event.get_sender()
    a = valid(str(sender.id))
    
    if a == "true":
        await update_(event)
    else:
        await event.answer("Access Denied", alert=True)


from kyt import *

@bot.on(events.NewMessage(pattern=r"(?:/reboot|\.reboot)$"))
@bot.on(events.CallbackQuery(data=b'reboot'))
async def reboot(event):
    async def reboot_(event):
        cmd = 'shutdown -r now'
        await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ REBOOT SERVER**
**◈ REBOOTING NOW...**
━━━━━━━━━━━━━━━━━━━━━━━
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])
        subprocess.check_output(cmd, shell=True)

    sender = await event.get_sender()
    val = valid(str(sender.id))
    if val == "false":
        try:
            await event.answer("Access Denied", alert=True)
        except:
            await event.reply("Access Denied")
    elif val == "true":
        await reboot_(event)


@bot.on(events.NewMessage(pattern=r"(?:/restart|\.restart)$"))
@bot.on(events.CallbackQuery(data=b'resx'))
async def resx(event):
	async def resx_(event):
		cmd = f'systemctl restart xray | systemctl restart nginx | systemctl restart haproxy | systemctl restart server | systemctl restart client'
		await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Restarting Service Done**
━━━━━━━━━━━━━━━━━━━━━━━
**◈ @alawivpn**
━━━━━━━━━━━━━━━━━━━━━━━
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	subprocess.check_output(cmd, shell=True)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await resx_(event)
	else:
		try:
			await event.answer("Akses ditolak",alert=True)
		except:
			await event.reply("Akses ditolak")

@bot.on(events.CallbackQuery(data=b'speedtest'))
async def speedtest(event):
	async def speedtest_(event):
		cmd = 'speedtest-cli --share'.strip()
		time.sleep(0)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		await event.edit(f"""
**
{z}
**
**◈ Succes**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await speedtest_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'backup'))
async def backup(event):
	async def backup_(event):
		cmd = f'printf "%s\n" "3" | m-backup | sleep 6 | exit'
		time.sleep(0)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)		
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		await event.edit(f"""
**◈ Succes**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backup_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'restore'))
async def create_restore(event):
	async def create_restore_(event):
		async with bot.conversation(chat) as pw2:
			await event.respond("**◈ LINK BACKUP :**")
			pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw2 = (await pw2).raw_text
		cmd = f'printf "%s\n" "1" "{pw2}" | m-backup | sleep 15 | exit'
		subprocess.check_output(cmd, shell=True)
		await event.respond(f"""
**◈ SUCCES RESTORE AKUN**
**◈ DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_restore_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'backer'))
async def backers(event):
	async def backers_(event):
		inline = [
[Button.inline(" BACKUP","backup"),
Button.inline(" RESTORE","restore")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
        **PREMIUM MENU SETTING**
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Domain :** `{DOMAIN}`
**◈ ISP:** `{z["isp"]}`
**◈ Country:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━
**◈ @alawivpn**
━━━━━━━━━━━━━━━━━━━━━━━
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backers_(event)
	else:
		await event.answer("Access Denied",alert=True)


async def get_public_ip():
    response = requests.get("http://ipv4.icanhazip.com")
    return response.text.strip()

@bot.on(events.CallbackQuery(data=b'setting'))
async def settings(event):
    async def settings_(event):
        inline = [
            [Button.inline("SPEEDTEST", "speedtest"), Button.inline("UPDATE","update")],
            [Button.inline("BACKUP", "backup"), Button.inline("RESTORE", "restore")],
            [Button.inline("REBOOT", "reboot"), Button.inline("RESTART", "resx")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]
        
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        public_ip = await get_public_ip()
        
        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
 ☘️ **PREMIUM MENU SETTING** ☘️
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Domain :** `{DOMAIN}`
**◈ IP VPS :** `{public_ip}`
**◈ ISP :** `{z["isp"]}`
**◈ Country :** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━
**◈ @alawivpn**
━━━━━━━━━━━━━━━━━━━━━━━
"""
        await event.edit(msg, buttons=inline)
    
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await settings_(event)
    else:
        await event.answer("Access Denied", alert=True)

# Tambahkan handler lain di sini...
