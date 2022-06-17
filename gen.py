import os
import json

assets = "app\\src\\main\\assets\\"

packs = []


for d in os.listdir(assets):
	if d == "contents.json":
		continue

	images = os.listdir(assets + d)
	stickers = [{"image_file": x, "emojis": ["🦕"]} for x in images]
	packs.append({
		"identifier": d,
		"name": f"Dinos {d}",
		"animated_sticker_pack": True,
		"publisher": "MetalpigMii",
		"tray_image_file": "bongodino.webp",
		"image_data_version": "2",
		"avoid_cache": False,
		"publisher_email": "",
		"publisher_website": "https://www.twitch.tv/metalpigmii",
		"privacy_policy_website": "",
		"license_agreement_website": "",
		"stickers": stickers
	})


print(json.dumps({"sticker_packs": packs}))