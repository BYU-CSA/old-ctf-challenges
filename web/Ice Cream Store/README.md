# Ice Cream

There is a new ice cream store in Jurassic Park land! Can you find the hidden flag?

## WRITEUP

The website content talks about the /chocolate, /vanilla, and /strawberry files on the website, hinting there are more. If you run dirb on the website, you'll get the following list of pages with a 200 status code:

---- Scanning URL: http://10.4.154.161:40008/ ----
* http://10.4.154.161:40008/2013 (CODE:200|SIZE:92)                            
* http://10.4.154.161:40008/admin (CODE:200|SIZE:94)                           
* http://10.4.154.161:40008/flag (CODE:200|SIZE:99)                            
* http://10.4.154.161:40008/mojo (CODE:200|SIZE:93)                            
* http://10.4.154.161:40008/tuscany (CODE:200|SIZE:94)                         
* http://10.4.154.161:40008/zeus (CODE:200|SIZE:98)                            
* http://10.4.154.161:40008/zimbra (CODE:200|SIZE:93) 

Each file path has the following content, respecitively:

* 2013: `3 - i`
* admin: `4 - rb_`
* flag: `1 - byuctf{`
* mojo: `6 - lo`
* tuscany: `7 - ml}`
* zeus: `5 - is_the_`
* zimbra: `2 - d`

If you put the phrases/letters in numerical order, you get the FLAG:

byuctf{dirb_is_the_loml}

# INFRASTRUCTURE

Running on port 40008