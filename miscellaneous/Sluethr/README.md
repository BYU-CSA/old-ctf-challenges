# Sluethr - A DNS and Hosts File Challenge #

## Setup ##

Two webpages are needed for this challnege: `index.html` and `gotcha.html`. They need to be hosted on separate IP addresses. `index.html` must also be given a domain name. For the purposes of this guide, we'll assume the following:
* `index.html` is hosted at `10.100.1.50`
* `gotcha.html` is hosted at `10.100.1.51`
* `10.100.1.50` has been given the DNS name of `sluethr.byu.edu`

The virtual machine, `sluethr.ova`, can be downloaded from the following link: [BOX](https://byu.box.com/s/mbf597jfqpxix7wtjj8oxioo2coocge8). This ova will be provided to challengers, along with the following instructions:

> Welcome agents, one and all! We have an incredibly important mission for you, should you choose to accept it. One of our intelligence agents, at great risk to her own life, stole information about a flag hidden in a secret website from an enemy base. The website is sluethr.byu.edu. However, one can only retrieve the flag if they access that website from a certain virtual machine, which our agent also stole. Apparently these agents are noobs, because they didn't change the default credentials on it (username and password are both vagrant). Can you set up the VM and retrive the flag?

The flag for this challenge is `byuctf{e8e823dbeac61d61b26565c518907549}`

### Adjusting the hosts file ###

The hosts file of the VM will need to be edited once we have the correct IP addresses and DNS names. This will require spinning up the VM, changing the entry in the hosts file, then saving a new OVA file for the VM. The hosts file can be found at C:\Windows\System32\drivers\etc\hosts. 

## Explanation ##

The virtual machine has an entry in the hosts file that associates the DNS name with the IP address of the gotcha page. The piece of the flag that is missing from the website is a comment in the hosts file; this means that challengers must locate the hosts file in order to complete the flag. Challengers can access the website from any device, and it fact, that could be an essential part of their research process. But only by locating and fixing the hosts file can they get the full flag. 