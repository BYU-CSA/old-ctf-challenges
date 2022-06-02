# Black
Level: Medium

Description:
```
One cool thing about Vue is that it's really hard to figure out what's going on in the page

Flag format - `byuctf{Phrase Separated By Spaces}`

`http://black.byuctf.xyz`
```

## Writeup
The first page will reveal sections of a QR code if you mouse over them. The QR code goes to another page on the site. An mp4 video is listed in the network tab, and if you go through the video, you'll get the words `Oh Canada Our Home And Native Land` in a random order. If you put them in the right order, you'll get the flag.

**Flag**: `byuctf{Oh Canada Our Home And Native Land}`

## Hosting
The video `loadButton.mp4` is too big to include in Git, but is located [here](https://app.box.com/s/rbdoh3eyhcli15pkavvtvjzidaol8t4t) and should be downloaded and appear in the `files/` directory. It should also be downloaded, moved to the `files/_nuxt/videos/` and called `loadButton.85316c6.mp4`.