# Question: Everything is an OSINT problem if you try hard enough. 
 
Welcome to my OSINT, 7 Layers of Hell!
Enjoy!
ps. there are quite literally seven layers to this. Goodluck!


ctf{hello}


## Writeup: 
In this challenge, the link to the RickRoll video is given. By clicking that, the user then needs to find a comment made by me, to another youtube video. This was a gif uploaded to youtube with a link visible on several frames of the gif. That link led to a pastebin where a body of text in braille is presented. Translating from braille text back into ascii ( best done with robobraille.org), yields a file in SQL format. This format is used to populate a database in SQL. Theoretically the next step could have been skipped, by parsing out the data by hand. The SQL file is best understood by converting from SQL format to a CSV. This CSV can then be turned into a .kml file, used by mapping applications. By now it would be clear that you have a list of coordinates, which when plotted on a map either by upload to google maps or by hand, presents the flag "hello". 


Map _> kml -> csv -> sql -> braille. -> audio file (box) -> pastebin -> gif -> rickroll

https://pastebin.com/jXNdLbAM

https://www.robobraille.org/


# Question: Y Not?
Cybersecurity is tough. Sometimes you can slack, sometimes you can't. That's why we have family. To be a 1337 hacker you should be able to do the following:

- Know how to use nmap
- Make great Kate memes
- Memorize the rick roll link perfectly
- try your best no matter what
- Did i mention meme?
- Be a fan of Cosmo the Cougar
- Join the ctf-group slack channel
format: Replace the 0s in the flag with curley brackets and submit that.
*ctf{slack_is_back}*

## Writeup
Multiple hints point to a slack flag. With enough digging, one could find a new custom cosmo the cougar emote for the server. The text command behind this emote is ctf0slack_is_back0.
