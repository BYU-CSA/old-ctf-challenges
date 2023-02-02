
# CHALLENGE TITLE: "IOT"
# Prompt

This homeowner has decided to hide their special flag inside of their..... Samsung smart refrigerator? Strange. See if you can connect to their device over wifi and access the flag. (This challenge requires OSINT)

# SOLVE

Pretty straightforward. The number one weakness for IOT devices is default credentials. If you google "samsung smart fridge default credentials" or any variation, you will find this article:
https://us.community.samsung.com/t5/Kitchen-and-Family-Hub/Refrigerator-RF28R2701SR-Default-Wifi-Password-not-working/td-p/1090329

It tells you that the password is  1111122222

If you enter that password, you get the flag: 

byuctf{D3F4U1T_6R3D3NT1AL5_4_IOT}

# INFRASTRUCTURE

Hosted on port 40006

