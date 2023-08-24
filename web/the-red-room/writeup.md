
# The Red Room

## Description
You trying to obtain information on the whereabouts of all the blackwidows, but the login is password protected!! Can you help Natasha get in, we wouldnt want hydra to obtain this information! All you know is the username: administrator. 

## Solution
1. **Step 1**: Open the website in a web browser and explore
2. **Step 2**: attempt a login and notice that you need the password! 
3. **Step 3**: Use hydra to brute force the directories (https://infinitelogins.com/2020/02/22/how-to-brute-force-websites-using-hydra/)
4. **Step 4**: The command looks like this: ```hydra -l admin -P /home/wyatt/rockyou.txt 127.0.0.1 http-post-form "/index.php:username=admin&password=^PASS^:Invalid username or password. Please try again"```
6. **Step 5**: enter username and password in the website

The flag for this challenge is `byuctf{did_black_widow_just_bow_to_hydra?}`

## Lessons Learned
It is anticipated that the competitor will learn about hydra

## notes
This is a docker container. Also, automated tools are allowed. Should take approximatley 20 minutes. The correct password is `1chocolate`
