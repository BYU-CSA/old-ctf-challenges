# WinRawr
Author: Daniel Taylor

## Challenge

A curator told me she found this in the museum archives, but it's encrypted.  You might be able to get in using a wordlist from the Wikipedia page for dinosaurs.

[winrawr.rar](./winrawr.rar)


## Solution

### Extract the password hash from the rar

```
rar2john winrawr.rar > rarhash.txt
```

rarhash.txt will contain the following:
```
winrawr.rar:$rar5$16$62ca8e6f86c27fde34d72b3b9e14667a$15$951daa09109f58933233f58c2cc69894$8$7a4a5ebb50b7cb33
```

If using hashcat (rather than john), remove `winrawr.rar:` from the beginning of the hash.

### Create a wordlist from the Wikipedia Dinosaur page

```
cewl https://en.wikipedia.org/wiki/Dinosaur -d 0 -w wordlist.txt
```

### Get cracking!

```
hashcat -a 0 -m 13000 rarhash.txt wordlist.txt
```

After initializing, hashcat was able to crack this in 40 seconds on a Chromebook.  So computing power shouldn't be a problem for anyone.

### Show the password

```
hashcat -m 13000 rarhash.txt --show
```

The password is `supratemporal`.

### Extract the file

```
unrar winrawr.rar
```

When prompted, use the password (`supratemporal`).

The flag can be found in flag.txt: `byuctf{what_does_an_unrawr_sound_like?}`
