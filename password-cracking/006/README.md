# 006 - A Series of Password Cracking Challenges #

006 is a series of James Bond themed password cracking challenges based on his movie: Goldeneye. The main villain in the movie is a perfect antithesis to Bond, an ex secret agent gone rouge who used to go by 006. Challengers will receive recovered password hashes from 006 and his cronies, and must crack them to stop the evil plan and save the world.

## Setup ##

### 006 I ###

Provide challengers with the following prompt:
> In this James Bond themed CTF challenge, you're tasked with cracking the password of Janus, and evil crime lord, to access his encrypted files containing crucial information about the organization's plans for a devastating attack. Time is of the essence, and the fate of millions rests on your ability to crack the password and stop the impending disaster.  
Flag format: byuctf{cracked_password}

Also provide challengers with `006_1.txt`

The flag is byuctf{brittishhottie}

### 006 II ###

Provide challengers with the following prompt:
> You did well recovering the first password, but unfortunately as our hackers were accessing their system the enemies ids spotted them and they were blocked. We know that Janus reset his password, because we intercepted a different password hash on their network. We can expect that he made this one a bit trickier to guess. Can you crack it in time for us to stop him?
Flag format: byuctf{cracked_password}

Also provide challengers with `006_2.txt`

The flag is byuctf{Arkhangelsk}

### 006 III ###

Provide challengers with the following prompt:
> We've finally got a foothold in Janus' network, and we're ready to take them down. This time we've recovered a small batch of passwords that seem to belong to various henchmen in his organisation. We'll need all of them cracked so we can do as much damage as possible this time around. Are you up to the task?  
Flag format: byuctf{password1_password2_password3_password4}

Also provide challengers with `006_3.txt`

The flag is byuctf{goldeneye007_goldeneye641_goldeneye069_goldeneye159}

## Solving Theory ##

### 006 I ###

This password is one found in the rockyou list, and the hashing algorithm is MD5. Challengers can use Google to recognize the hash format and either hashcat or John the ripper to crack it.

### 006 II ###

This password most likely won't be found on any standard lists, but it an important part of Alec's backstory in the movie. Challengers will need to create a wordlist based on information about Alec, most likely using a web crawler like `cewl`. Challengers might also find it on a massive list such as the Torrent file (https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm). The hash is a SHA1, which is different than the previous challenge.

### 006 III ###

The four passwords provided all follow the same format, "goldeneye" + three random digits (ex: goldeneye123). This is a pretty standard (and unfortunately insecure) corporate policy put in place by IT/Cyber teams who want to make password management easy. Two of the passwords can be found on the rockyou list, which will give challengers an idea of what they're working with. It's up to them to create a custom wordlist with all possible three digit combonations. The hashes are SHA512, which take longer to crack but are pretty recognizable. 