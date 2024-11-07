# Dino Stickerpack for WhatsApp

## Adding new stickers

* Stickers must be exactly 512 x 512 pixels
* Each static sticker must be less than or equal to 100KB and each animated sticker must be less than or equal to 500KB. See the section [Tips for Reducing File Size](#tips-for-reducing-file-size) below.
* Animated stickers must have frames with minimum duration of 8ms. Animation duration should be less than or equal to 10 seconds total.
* For animated stickers, the first frame should say it all - WhatsApp ends the animation on the first frame after looping so please make sure your first frame is the complete image of your sticker and adjust the sequence of the stickers accordingly so users don’t see a jumpy experience going from the last to first frame. Ex. A sticker that animated “Hi!” should have the first frame show all words “Hi!”.

* Sticker Picker/Tray Icon
  * Provide an image that will be used to represent your sticker pack in the WhatsApp sticker picker/tray
  * This image should be static and 96 x 96 pixels
  * Max file size of 50KB

* [Android Studio](https://developer.android.com/studio/) allows you to convert PNGs to WebP. Simply create a new project in Android Studio, open your PNG and right click on the image and select convert to WebP ([https://developer.android.com/studio/write/convert-webp](https://developer.android.com/studio/write/convert-webp)). Make sure you uncheck the box next to "Skip images with transparency/alpha channel" in the export flow.
* Use [squoosh](https://squoosh.app/), an online browser tool, by the Google Chrome Labs

* The sticker must be added to `src/app/src/main/assets/<sticker-pack-index>` folder and the `contents.json` file must be updated with the new sticker details.

* The `image_data_version` of all packs should always match the app version. This is to ensure that the app can detect if there are new stickers to download.
