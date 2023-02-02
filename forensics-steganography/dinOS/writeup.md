# dinOS - spoutingwhale
 > flag: byuctf{dang_this_is_a_tiny_image_in_an_image}

## Challenge intro:
for this challenge, I would just give the competitors the dinOS.jpg image with no context.

# Solution:

in this challenge, you are given a file titled `dinOS.jpg`. Upon getting this file, I ran it through binwalk and found that there was a zip file, and some virtual machine files included. I extracted the image.zip file using binwalk, then unzipped it. I could see the virtaul machine files, I then imported them with vmware workstation player, it works with virtualbox as well. Boot the VM, open a terminal,  type `ls`, and you will find the flag file there, then you can `cat` the flag out

*note: if you use binwalk, it will run for a long time 9and extrat almost 1tb of data, you can kill it after it gets the files, or use a hex editor to remove the jpg portion  of the file.*