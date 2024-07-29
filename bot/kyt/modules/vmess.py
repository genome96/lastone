from kyt import *

#delete
@bot.on(events.CallbackQuery(data=b'delete7-vmess'))
async def delete_vmess(event):
	async def delete_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#vmg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
** LIST DELETE USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "4" "{user}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#renew
@bot.on(events.CallbackQuery(data=b'renew7-vmess'))
async def renew_vmess(event):
	async def renew_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#vmg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST RENEW USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**◈ Input Your New Expired (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "3" "{user}" "{exp}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)


#limit
@bot.on(events.CallbackQuery(data=b'limit7-vmess'))
async def limit_vmess(event):
	async def limit_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#vmg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ CHANGE LIMIT USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
** Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**◈ Input Your New Limit IP Login :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**◈ Input Your New Quota User :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			cmd = f'printf "%s\n" "7" "{user}" "{exp}" "{pw}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CHANGE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CekConfig
@bot.on(events.CallbackQuery(data=b'akun7-vmess'))
async def akun_vmess(event):
	async def akun_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#vmg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ CEK CONFIG USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "6" "{user}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CEK AKUN**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await akun_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
#restore
@bot.on(events.CallbackQuery(data=b'restore7-vmess'))
async def restore_vmess(event):
	async def restore_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/vmess/akundelete | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST AKUN RESTORE **
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**◈ Input Your Expired (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**◈ Input Your New Limit IP Login :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**◈ Input Your New Quota User:**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "11" "{user}" "{exp}" "{pw}" "{pw2}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CHANGE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await restore_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)


#MultiLogin Login
@bot.on(events.CallbackQuery(data=b'loginip7-vmess'))
async def loginip_vmess(event):
	async def loginip_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/vmess/listlock | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST MULTI LOGIN IP USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "9" "{user}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES UNLOCK**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await loginip_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#MultiLogin Quota
@bot.on(events.CallbackQuery(data=b'logingb7-vmess'))
async def logingb_vmess(event):
	async def logingb_vmess_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/vmess/userQuota | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST LOGIN QUOTA USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Number :**
➥ /cancel kembali ke MENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "10" "{user}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES UNLOCK**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await logingb_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CRATE VMESS
@bot.on(events.CallbackQuery(data=b'create7-vmess'))
async def create_vmess(event):
	async def create_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
     **CREATE ACCOUNT PREMIUM**
━━━━━━━━━━━━━━━━━━━━━━━
**➥ Boleh campur**
**➥ Huruf, angka, dan kapital**
**➥ Tanpa spasi**
**➥ Tdk sama dgn user lain**

**➥ /cancel kembali ke MENU**
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input your username :**
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**◈ Input Your Expired (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**◈ Input Your Limit IP Login :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**◈ Input Your Quota User :**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "1" "{user}" "{exp}" "{pw}" "{pw2}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CREATE**
**◈ DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# TRIAL VMESS
@bot.on(events.CallbackQuery(data=b'trial7-vmess'))
async def trial_vmess(event):
	async def trial_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
      **TRIAL VMESS PREMIUM**
━━━━━━━━━━━━━━━━━━━━━━━
**➥ Isikan menit saja

━━━━━━━━━━━━━━━━━━━━━━━
**◈ Input Your Timer (Minutes) :**
➥ /cancel kembali ke MENU
""")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		per = "/cancel"
		if exp == per:
			await event.respond(f"""
**◈ CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" {2} "{exp}" | m-vmess | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True).decode("utf-8")
			await event.respond(f"""
**◈ SUCCES CREATE**
**◈ DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CEK
@bot.on(events.CallbackQuery(data=b'cek7-vmess'))
async def cek_vmess(event):
	async def cek_vmess_(event):
		time.sleep(0)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		cmd = 'bot-cek-ws'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
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
━━━━━━━━━━━━━━━━━━━━━━━
**◈ VMESS USER ONLINE**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'login7-vmess'))
async def vmess(event):
	async def vmess_(event):
		inline = [
[Button.inline(" UNLOCK LOGIN ","loginip7-vmess"),
Button.inline(" UNLOCK QUOTA ","logingb7-vmess")],
[Button.inline("‹ Back ›","vmess")]]
		await event.edit(buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

from kyt import *

@bot.on(events.NewMessage(pattern=r"(?:/vmess|.vmess)$"))
@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
    inline = [
        [Button.inline(" Trial ", "trial7-vmess"),
         Button.inline(" Create ", "create7-vmess"),
         Button.inline(" Login ", "cek7-vmess")],
        [Button.inline(" Delete ", "delete7-vmess"),
         Button.inline(" Unlock ", "login7-vmess"),
         Button.inline(" Limit ", "limit7-vmess")],
        [Button.inline(" Renew", "renew7-vmess"),
         Button.inline(" Restore ", "restore7-vmess"),
         Button.inline(" Akun ", "akun7-vmess")],
        [Button.inline("🔙", "menu")]
    ]
    sender = await event.get_sender()
    val = valid(str(sender.id))
    if val == "false":
        try:
            await event.answer("Akses Ditolak", alert=True)
        except:
            await event.reply("Akses Ditolak")
    elif val == "true":
        z = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        vm = f'cat /etc/xray/config.json | grep "#vmg" | wc -l'
        vms = subprocess.check_output(vm, shell=True).decode("ascii")

        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
  ☘️ **VMESS MENU MANAGER** ☘️
━━━━━━━━━━━━━━━━━━━━━━━
 **◈ Service:** `VMESS`
 **◈ Total Account  :** `{vms.strip()}` __account__
 **◈ Host:** `{DOMAIN}`
 **◈ ISP:** `{z["isp"]}`
 **◈ Country:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━
 **◈ @alawivpn**
━━━━━━━━━━━━━━━━━━━━━━━
"""
        x = await event.edit(msg, buttons=inline)
        if not x:
            await event.reply(msg, buttons=inline)

