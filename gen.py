import os
import json

assets = "app\\src\\main\\assets\\"

packs = []


for d in os.listdir(assets):
	if d == "contents.json":
		continue

	images = os.listdir(assets + d)
	stickers = [{"image_file": x, "emojis": []} for x in images]
	packs.append({
		"identifier": d,
		"name": d,
		"publisher": "<publisher>",
		"tray_image_file": "<tray_image_file>",
		"image_data_version": "1",
		"avoid_cache": False,
		"publisher_email": "",
		"publisher_website": "<publisher_website>",
		"privacy_policy_website": "",
		"license_agreement_website": "",
		"stickers": stickers
	})


print(json.dumps({"sticker_packs": packs}))