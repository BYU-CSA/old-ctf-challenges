# Web-inator

## Description
The evil Dr Doofenshmirtz has pwned all of BYU's computers and it only displays this web page, can you assist Agent P. in taking him and his inator down before it wipes BYU off of the map?? 

## Solution
1. **Step 1**: Open the website in a web browser and explore.
2. **Step 2**: Use the inspector and view the cookies, noting the user cookie.
3. **Step 3**: Put the cookie in a base64 decoder, and reverse the string. It will say `user=public_user,inator_self_destruct=false` 
4. **Step 4**: change the user to admin, and the inator self destruct to true in the cookie `user=admin,inator_self_destruct=true`. Reverse the text and base64 encode it.  
5. **Step 5**: in the inspector of the webpage, edit the cookie the browser gave you and insert the string made in the step above. Refresh the page and retreive the flag.  
## Flag
The flag for this challenge is `{d0of-and-h1s-cl13nt-s1d3-co0k13-4uth3nt1c4t10n}`

## Lessons Learned
It is anticipated that the competitor will learn about how to find and modify a cookie for client side authentication. 

## Notes
Additional notes and comments about the challenge or the writeup process.