from kyt import *
@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
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
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**◈ KETIK PASWORD AKUN :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**◈ KETIK EXP AKUN (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**◈ KETIK LIMIT IP LOGIN :**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "1" "{user}" "{pw}" "{exp}" "{pw2}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CREATED**
**◈ DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST DELETE USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ KETIK NOMOR :**
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
			cmd = f'printf "%s\n" "4" "{user}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES Delete**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'limit-ssh'))
async def limit_ssh(event):
	async def limit_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ CHANGE LIMIT USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ KETIK NOMOR :**
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
**◈ Ketik Limit IP Login Baru :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "7" "{user}" "{exp}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES Change Limit**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		async with bot.conversation(chat) as exp:
			await event.edit(f"""
**KETIK MENIT (Minutes) :**
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
			cmd = f'printf "%s\n" {2} "{exp}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CREATE**
**◈ DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
@bot.on(events.CallbackQuery(data=b'cek-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		time.sleep(0)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		cmd = 'bot-cek-login-ssh'.strip()
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
**◈ SSH USER ONLINE**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'renew-ssh'))
async def renew_ssh(event):
	async def renew_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST RENEW USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ MASUKAN NOMOR :**
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
**◈ KETIK EXPIRED BARU (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "3" "{user}" "{exp}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/sshx/listlock | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ LIST MULTI LOGIN USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ KETIK NOMOR :**
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
			cmd = f'printf "%s\n" "9" "{user}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES UNLOCK**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'akun-ssh'))
async def akun_ssh(event):
	async def akun_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
━━━━━━━━━━━━━━━━━━━━━━━
**◈ CEK CONFIG USER**
━━━━━━━━━━━━━━━━━━━━━━━
{z}
━━━━━━━━━━━━━━━━━━━━━━━
**◈ KETIK NOMOR :**
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
			cmd = f'printf "%s\n" "6" "{user}" | m-sshovpn | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**◈ SUCCES CEK AKUN**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await akun_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.NewMessage(pattern=r"(?:/ssh|.ssh)$"))
@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
    inline = [
        [Button.inline(" Trial ", "trial-ssh"),
         Button.inline(" Create ", "create-ssh"),
         Button.inline(" Login ", "cek-ssh")],
        [Button.inline(" Delete ", "delete-ssh"),
         Button.inline(" Unlock ", "login-ssh"),
         Button.inline(" Limit ", "limit-ssh")],
        [Button.inline(" Renew", "renew-ssh"),
         Button.inline(" Akun ", "akun-ssh"),
         Button.inline("🔙", "menu")]
    ]
    sender = await event.get_sender()
    val = valid(str(sender.id))
    if val == "false":
        try:
            await event.answer("Akses Ditolak", alert=True)
        except:
            await event.reply("Akses Ditolak")
    elif val == "true":
        sh = f' cat /etc/xray/ssh | grep "###" | wc -l'
        ssh_count = subprocess.check_output(sh, shell=True).decode("ascii")
        z = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()

        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
    ☘️ **SSH MENU MANAGER** ☘️
━━━━━━━━━━━━━━━━━━━━━━━
**◈ Service:** `SSH`
**◈ Total Account  :** `{ssh_count.strip()}` __account__
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

