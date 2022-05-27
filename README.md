# Android Stickers Apps for WhatsApp

## Overview

* Stickers must be exactly 512 x 512 pixels
* Each static sticker must be less than or equal to 100KB and each animated sticker must be less than or equal to 500KB. See the section [Tips for Reducing File Size](#tips-for-reducing-file-size) below.
* Animated stickers must have frames with minimum duration of 8ms. Animation duration should be less than or equal to 10 seconds total.
* For animated stickers, the first frame should say it all - WhatsApp ends the animation on the first frame after looping so please make sure your first frame is the complete image of your sticker and adjust the sequence of the stickers accordingly so users don’t see a jumpy experience going from the last to first frame. Ex. A sticker that animated “Hi!” should have the first frame show all words “Hi!”.

* Sticker Picker/Tray Icon
  * Provide an image that will be used to represent your sticker pack in the WhatsApp sticker picker/tray
  * This image should be static and 96 x 96 pixels
  * Max file size of 50KB

https://nukesaq88.github.io/Pngyu

* [Android Studio](https://developer.android.com/studio/) allows you to convert PNGs to WebP. Simply create a new project in Android Studio, open your PNG and right click on the image and select convert to WebP ([https://developer.android.com/studio/write/convert-webp](https://developer.android.com/studio/write/convert-webp)). Make sure you uncheck the box next to "Skip images with transparency/alpha channel" in the export flow.
* Use [squoosh](https://squoosh.app/), an online browser tool, by the Google Chrome Labs

## How to create a sticker app

* After downloading this repo, open the sample app's Android folder in [Android Studio](https://developer.android.com/studio/). If you are new to Android development, visit https://developer.android.com/training/basics/firstapp/index.html for more information on setting up your Android development environment.
* Navigate to SampleStickerApp/app/src/main/assets in Android Studio.
* Inside the assets folder, folder 1 contains a number of sample sticker art files. Replace these with your own sticker files.
* Also replace the sample tray icon PNG with your own tray icon.
* If you'd like to have more than 1 sticker pack in your app, simply create a folder named "2" or "3", etc. within the assets folder and place your art and tray icon in there.

### Modifying the contents.json file
You must also modify the contents.json file in SampleStickerApp/app/src/main/assets. Replace the values of the metadata with your own. A few notes:

* `name`: the sticker pack's name (128 characters max)
* `identifier`: The identifier should be unique and can be alphanumeric: a-z, A-Z, 0-9, and the following characters are also allowed "_", "-", "." and " ". The identifier should be less than 128 characters.
* `publisher`: name of the publisher of the pack (128 characters max)
* Replace the "image_file" value with the file name of your sticker image. It must have both the file name and extension. The ordering of the files in the JSON will dictate the ordering of your stickers in your pack.
* `image_data_version` : an overall representation of the version of the stickers and tray icon. When you update stickers or tray icon in your pack, please update this string, this will tell WhatsApp that the pack has new content and update the stickers on WhatsApp side.
* `avoid_cache` : this tells WhatsApp that the stickers from your pack should not be cached. By default, you should keep it false. Exception is that if your app updates stickers without user actions, you can keep it true, for example: your app provides clock sticker that updates stickers every minute.
* `android_play_store_link` and `ios_app_store_link` (optional fields): here you can put the URL to your sticker app in the Google Play Store and Apple App Store (if you have an iOS version of your sticker app). If you provide these URLs, users who receive a sticker from your app in WhatsApp can tap on it to view your sticker app in the respective App Stores. On Android, the URL follows the format https://play.google.com/store/apps/details?id=de.vincentscode.where "de.vincentscode. is your app's package name.
* `emojis` (required): add up to 1-3 emojis for each sticker file. Select emoji that best describe or represent that sticker file. For example, if the sticker is portraying love, you may choose to add a heart emoji like 💕. If your sticker portrays pizza, you may want to add the pizza slice emoji 🍕. In the future, WhatsApp will support a search function for stickers and tagging your sticker files with emoji will enable that. The sticker picker/tray in WhatsApp today already categorizes stickers into emotion categories (love, happy, sad, and angry) and it does this based on the emoji you tag your stickers with. see emoji list for tagging (https://github.com/WhatsApp/stickers/blob/main/Android/README.md#emoji-list-to-use-for-tagging)
* `animated_sticker_pack`: boolean value to indicate whether the sticker pack is animated (required for animated sticker packs, optional for static sticker packs)

The following fields are optional: `ios_app_store_link`, `android_play_store_link`, `publisher_website`, `privacy_policy_website`, `license_agreement_website`
All the links need to start with either "http" or "https"

If your app has more than 1 sticker pack, you will need to reference it in contents.json. Simply create a second array within the "sticker_packs" section of the JSON and include all the metadata (name, identifier, etc) along with all the references to the sticker files.

## Submit your app
You need to build a release version of your app for submission to the Google Play Store. Click Build > Generate Signed Bundle/APK. For more information, visit https://developer.android.com/studio/publish/app-signing#sign-apk. Note that Android Studio saves the APKs you build in project-name/module-name/build/outputs/apk. For more information on building your app, visit https://developer.android.com/studio/run/.

Importantly, when naming your app, it is strongly advised you do *not* use "WhatsApp" anywhere in the name of your app or in the name field of your app listing on the Google Play Store. However, when preparing your app for submission in Google Play Store, you'll have the option to add description associated with your app and it's okay to mention WhatsApp in the description. WhatsApp can also launch the Google Play Store and perform a search for other sticker pack apps. To help your app appear in this list, also add the keyword WAStickerApps to app's description when setting up your app in the Google Play Store console. You can use additional keywords, but make sure you at least use this one.

To submit your app to the Google Play Store, follow the instructions here: https://developer.android.com/distribute/best-practices/launch/.

It is advised that you create Multiple APKs per ABI (CPU Architecture), it will make the published app size smaller. see https://developer.android.com/studio/build/configure-apk-splits for more information. In order to do that, uncomment the lines 47-52 in app/build.gradle line.
