from kyt import *


@bot.on(events.CallbackQuery(data=b'add7-ip'))
async def add_ip(event):
	async def add_ip_(event):
		ox2 = "VIP"
		ox = requests.get(f"https://ipv4.icanhazip.com").text.strip()
		bz = f" curl -sS https://raw.githubusercontent.com/vmessh/izin/script/registrasi.txt | grep '{ox}' | cut -d ' ' -f7 "
		bo = subprocess.check_output(bz, shell=True).decode("ascii").strip()
		if not ox2 != bo:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**👉 Input New IP VPS:**
/cancel Kembali KeMENU
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			per = "/cancel"
			if exp == per:
				await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
			else:
				async with bot.conversation(chat) as pw1:
					await event.respond(f"""
**👉 Input Nama IP VPS:**
""")
					pw1 = pw1.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					pw1 = (await pw1).raw_text
				async with bot.conversation(chat) as pw:
					await event.respond(f"""
**👉 Input Your Expired (day) :**
""")
					pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					pw = (await pw).raw_text
				async with bot.conversation(chat) as exp2:
					await event.respond("**Choose your Choice**",buttons=[
[Button.inline("👉 ADMIN","1"),
Button.inline("👉 NORMAL ","2")]])
					exp2 = exp2.wait_event(events.CallbackQuery)
					exp2 = (await exp2).data.decode("ascii")
				per2 = "1"
				if exp2 == per2:
					async with bot.conversation(chat) as key:
						await event.respond(f"""
**👉 Input Total Key Admin :**
""")
						key = key.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
						key = (await key).raw_text
					cmd = f'printf "%s\n" "1" "{exp}" "{pw1}" "{pw}" "{exp2}" "{key}" | m-ip | sleep 9 | exit'
					subprocess.check_output(cmd, shell=True).decode("utf-8")
					await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])

				else:
					cmd = f'printf "%s\n" "1" "{exp}" "{pw1}" "{pw}" "{exp2}" | m-ip | sleep 9 | exit'
					subprocess.check_output(cmd, shell=True).decode("utf-8")
					await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
		else:
			async with bot.conversation(chat) as user:
				await event.respond(f"""
**👉 Input Your IP :**
/cancel Kembali KeMENU
""")
				user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				user = (await user).raw_text
			per = "/cancel"
			if user == per:
				await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
			else:
				async with bot.conversation(chat) as exp:
					await event.respond(f"""
**👉 Input Your Name :**
""")
					exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					exp = (await exp).raw_text
				async with bot.conversation(chat) as pw:
					await event.respond(f"""
**👉 Input Your Expired (day) :**
Max 30 Day
""")
					pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					pw = (await pw).raw_text
				cmd = f'printf "%s\n" "1" "{user}" "{exp}" "{pw}" | m-ip | sleep 9 | exit'
				subprocess.check_output(cmd, shell=True).decode("utf-8")
				await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await add_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'change7-ip'))
async def change_ip(event):
	async def change_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond(f"""
**👉 Input Your IP old :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**👉 Input Your IP new :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "7" "{user}" "{exp}" | m-ip | sleep 9 | exit'
			subprocess.check_output(cmd, shell=True).decode("utf-8")
			await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await change_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'renew7-ip'))
async def renew_ip(event):
	async def renew_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond(f"""
**👉 Input Your IP to Renew :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**👉 Input Your Expired (day) :**
Max 30 Day
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "5" "{user}" "{exp}" | m-ip | sleep 9 | exit'
			subprocess.check_output(cmd, shell=True).decode("utf-8")
			await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'delete7-ip'))
async def delete_ip(event):
	async def delete_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond(f"""
**👉 Input Your IP to Delete :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
		else:
			cmd = f'printf "%s\n" "3" "{user}" | m-ip | sleep 9 | exit'
			subprocess.check_output(cmd, shell=True).decode("utf-8")
			await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)


@bot.on(events.CallbackQuery(data=b'add7-key2'))
async def add_key(event):
	async def add_key_(event):
		ox2 = "VIP"
		ox = requests.get(f"https://ipv4.icanhazip.com").text.strip()
		bz = f" curl -sS https://raw.githubusercontent.com/vmessh/izin/script/registrasi.txt | grep '{ox}' | cut -d ' ' -f7 "
		bo = subprocess.check_output(bz, shell=True).decode("ascii").strip()
		if not ox2 != bo:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**👉 Input Name Admin Jangan Spasi:**
/cancel Kembali KeMENU
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			per = "/cancel"
			if exp == per:
				await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
			else:
				async with bot.conversation(chat) as pw1:
					await event.respond(f"""
**👉 Input Total Create Key:**
""")
					pw1 = pw1.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					pw1 = (await pw1).raw_text
				async with bot.conversation(chat) as pw:
					await event.respond(f"""
**👉 Input Your Expired (day) :**
""")
					pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					pw = (await pw).raw_text
				async with bot.conversation(chat) as exp2:
					await event.respond("**Choose your Choice**",buttons=[
[Button.inline("👉 ADMIN","1"),
Button.inline("👉 NORMAL ","2")]])
					exp2 = exp2.wait_event(events.CallbackQuery)
					exp2 = (await exp2).data.decode("ascii")
				per2 = "1"
				if exp2 == per2:
					async with bot.conversation(chat) as key:
						await event.respond(f"""
**👉 Input Total Key Admin :**
""")
						key = key.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
						key = (await key).raw_text
					cmd = f'printf "%s\n" "2" "{exp}" "{pw1}" "{pw}" "{exp2}" "{key}" | m-ip | sleep 9 | exit'
					subprocess.check_output(cmd, shell=True).decode("utf-8")
					await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
				else:
					cmd = f'printf "%s\n" "2" "{exp}" "{pw1}" "{pw}" "{exp2}" | m-ip | sleep 9 | exit'
					subprocess.check_output(cmd, shell=True).decode("utf-8")
					await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**👉 Input Total Create Key :**
/cancel Kembali KeMENU
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			per = "/cancel"
			if exp == per:
				await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
			else:
				async with bot.conversation(chat) as pw:
					await event.respond(f"""
**👉 Input Your Expired (day) :**
Max 30 Day
""")
					pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					pw = (await pw).raw_text
				cmd = f'printf "%s\n" "2" "{exp}" "{pw}" | m-ip | sleep 9 | exit'
				subprocess.check_output(cmd, shell=True).decode("utf-8")
				await event.edit(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","admin")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await add_key_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		

@bot.on(events.NewMessage(pattern=r"(?:.admin|/admin)$"))
@bot.on(events.CallbackQuery(data=b'admin'))
async def start(event):
	inline = [
[Button.inline("KEY GENERATOR","add7-key2")],
[Button.inline("ADD IP","add7-ip"),
Button.inline("CHANGE IP","change7-ip")],
[Button.inline("RENEW IP","renew7-ip"),
Button.inline("DELETE IP","delete7-ip")],
[Button.inline("‹ Main Menu ›","menu")]]
	ox2 = "ON"
	ox = requests.get(f"https://ipv4.icanhazip.com").text.strip()
	bz = f" curl -sS https://raw.githubusercontent.com/vmessh/izin/script/registrasi.txt | grep '{ox}' | cut -d ' ' -f5 "
	bo = subprocess.check_output(bz, shell=True).decode("ascii").strip()
	if not ox2 != bo:
		sender = await event.get_sender()
		val = valid(str(sender.id))
		if val == "false":
			try:
				await event.answer("Akses Ditolak", alert=True)
			except:
				await event.reply("Akses Ditolak")
		elif val == "true":
			sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
			namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
			ipvps = f" curl -s ipv4.icanhazip.com"
			ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
			citsy = f" cat /etc/xray/city"
			city = subprocess.check_output(citsy, shell=True).decode("ascii")

			msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
            **PANEL REGIST MENU**
━━━━━━━━━━━━━━━━━━━━━━━
**» OS     :** `{namaos.strip().replace('"','')}`
**» CITY :** `{city.strip()}`
**» DOMAIN :** `{DOMAIN}`
**» IP VPS :** `{ipsaya.strip()}`
━━━━━━━━━━━━━━━━━━━━━━━
"""
			x = await event.edit(msg,buttons=inline)
			if not x:
				await event.reply(msg,buttons=inline)
	else:
		await event.respond(f"**Your Not Admin Chat @alawivpn For buy Key**")


