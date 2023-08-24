# IMF Flag Portal

## Description
The competitor is presented with a webpage that tells them that they need to give the page the correct request to *put* the unencrypted flag on the page. 

## Solution
1. **Step 1**: Open the website in a web browser and explore.
2. **Step 2**: Open Burpsuite, navigate to the proxy tab, turn intercept on, and open the browser. 
3. **Step 3**: In the burpsuite browser, navagate to the site. It will hang.
4. **Step 4**: Return to burpsuite, right click on the request code shown and select "send to repeater", then click on the repeater tab above. 
5. **Step 5**: In the reeater tab, you can edit the web request type on the first line. To print the flag, enter a PUT request. The flag should be written in the response to the right, or you can render the webpage. 

## Flag
The flag for this challenge is `byuctf{spo0o0o0o0o0o0o0o0o0o0o0o0o0o0o0f3d-w3b-r3qu3st}`

## Lessons Learned
It is anticipated that the competitor will learn about how to spoof a web request and how to use burp suite. 

## Notes
Additional notes and comments about the challenge or the writeup process.
