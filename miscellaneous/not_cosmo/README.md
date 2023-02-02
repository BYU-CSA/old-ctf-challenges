## Not Cosmo
* Level - medium
* Author: Justin Giboney

Description: 
```
Somewhere in all these numbers is not Cosmo.

11111 11000 10101 10011 11111
10000 01010 10011 10010 00001
10111 01000 00101 01010 11101
10111 01011 10101 10010 11101
10111 01001 00000 00010 11101

10000 01011 01111 11010 00001
11111 11010 10101 01011 11111
00000 00001 11010 01000 00000
11111 01111 01011 11101 01010
01100 00100 10101 11100 10000

11010 01000 10011 10110 10101
01010 10110 00101 01001 01100
11111 11001 10100 11101 10011
10010 10101 00000 00100 10011
10110 11101 11111 10111 10111

10110 00101 01001 01101 00011
10011 11100 11010 11111 10001
00000 00010 10101 01000 10001
11111 11011 00011 01010 11111
10000 01000 10111 01000 11000

10111 01011 00101 01111 10100
10111 01011 00001 11010 10011
10111 01010 11100 00101 00101
10000 01010 11000 00110 10010
11111 11011 01100 01001 01011
```

**Flag** - `byuctf{kosmoceratops}`

## Hint
Find a way to visualize the binary

## Writeup
The binary represents black (1) and white (0) pixels. When put into a graphical form, it represents a QR code. Scanning the code gives the flag. The spacing is meaningless, but helps the binary not look like a QR code.