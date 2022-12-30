#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"السلام عليكم يا  {message.from_user.mention},أنا بوت أقوم بتحميل قوائم يوتيوب \n\n فقط أرسل رابط قائمة التشغيل متبوعا بالصيغة التي تريد  \n\n مثلا \n\n youtube.com/playlist=××× audio  \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 \n\n لدعم استمرار المشروع هنا \n\n http://paypal.me/kelectronic89 ",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 Help", callback_data=f"help"),
					InlineKeyboardButton("🧰 About", callback_data=f"about")
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "help" in cb_data:
		await update.message.edit_text("Just Send URL with Format.(Audio/Video)\nExample: `https://youtube.com/playlist?list=xxxxxxxxxx audio`\n\nPowered by @TGBotsProJect",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🧰 About", callback_data=f"about"),
					InlineKeyboardButton("🔙 Back", callback_data=f"back")
				]]
			))
	elif "about" in cb_data:
		await update.message.edit_text("Language: Python\nFramework: Pyrogram\nEngine: YTDL\nCorded By: @ZauteKm\n\nPowered by @TGBotsProJect",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 Help", callback_data=f"help"),
					InlineKeyboardButton("🔙 Back", callback_data=f"back")
				]]
			))
	elif "back" in cb_data:
		await update.message.edit_text(f"Hi {update.from_user.mention},If you need any help, Just click help button.\n\nProject by @ZauteKm",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 Help", callback_data=f"help"),
					InlineKeyboardButton("🧰 About", callback_data=f"about")
				]]
			))
