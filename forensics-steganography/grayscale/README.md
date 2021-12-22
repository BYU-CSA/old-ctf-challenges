# Grayscale
**Level**: Hard

**Author**: Justin Giboney

**Description**:
```
Can you decipher the message using this grayscale photo?

[grayscale.png]

Note - the flag format is NOT `ctf` this time, it's `flag{text_here}`
```

## Writeup
If you zoom into the photo enough, you'll see that it's made up of several vertical lines 1 pixel wide. Each of these lines is a different shade of grey. Using a tool like Gimp allows you to find the exact hex color value for each vertical line. When the first two hex digits from each line is translated into ASCII, the flag is discovered.

Flag: `flag{ant_go_marching_one_by_one_horrah}`