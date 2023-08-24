# Smash, bang, crash, boom!

## Description
*write fun instructions here* Competitor is given a console that they need to enter a password in. They are given this as the password, and that is it. 
`d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70`

## Solution
1. **Step 1**: Netcat to the script
2. **Step 2**: Play around with the script. You will notice that when you enter the given password that was thought to be correct, the hashes are the same but it is still incorrect. 
3. **Step 3**: Google the string that was given to the competitor as the password. 
4. **Step 4**: You will notice that it is an MD5 collision, you can find information on it here: https://gist.github.com/mateuszszulc/7e4b8108f54fad9fb8b2213163c3376c
5. **Step 5**: If you look at line 5 of the text file, you will notice that is the string that was given as the password. If you look at line 3, this is the password that needs to be submitted. `d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70`
6. **Step 6**: Netcat in again, enter the password, and retreive the flag! 

## Flag
The flag for this challenge is `byuctf{CrashImpactSmashClashJoltBumpCrunch}`

## Lessons Learned
It is anticipated that the competitor will learn MD5 collisions and why it should be avoided. 

## Notes
This python script can be accessed over a netcat session. 
