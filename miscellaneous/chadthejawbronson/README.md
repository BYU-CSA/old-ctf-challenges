# Chad "The Jaw" Bronson
Level: Medium

Description:
```
Chad "The Jaw" likes nothing more than pumping iron and looking good. He left behind a favorite song of his for us to analyze. Can you find his deepest, darkest secret?

[can-you-feel-my-heart-chad.mp3]
```

## Writeup
Running the last few seconds of the song in a spectogram gives you the phrase "twitter me". Looking him up on Twitter reveals two posts with pastebin links - one has a cipher where the number of words on each line corresponds to a letter (1=A, 2=B, etc.) that gives you the password `iamthechaddest213`. The other one has a photo with a RAR file hidden inside. The password unlocks the RAR file, filled with photos and videos. One of the photos has the flag towards the bottom.

**Flag** - `byuctf{cyb3r_ch@ds_are_th3_r3aL_ch@ds}`
