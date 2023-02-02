# CHALLENGE TITLE: "Don't Get Phished"

# Prompt - Use the final.html on the CTF website (source.html is just for CTF group leader reference)

Melissa got this email but it looks phishy.... looks like an attacker is trying to steal her credentials. Can you find the malicious website to which the attacker is exfiltrating credentials? Submit the entire website URL as the flag.

*Note: This is a fake phishing email/website, it is not malicious. The HTML has purposefully been "broken" so that competitors need to look at the source code to find the flag, instead of just loading the HTML in a browser. 


# ANSWER

If you deobfuscate the javascript using the by using the unescape functions and the base64 decoding, you will find the website is:

http://annalanes.com/filethisaway/txt.txt