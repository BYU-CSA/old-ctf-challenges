import hashlib

def is_hexadecimal(input_string):
    valid_characters = set('0123456789abcdef')
    input_set = set(input_string.lower())
    
    # Check if there are any invalid characters
    if not input_set <= valid_characters:
        print("Invalid characters in input. Only characters 0-9 and a-f are allowed.")
        exit(1)

        # Check if the input string has an even number of characters
    if len(input_string) % 2 != 0:
        print("Input string must have an even number of characters. For example, decimal 1 in hex is 01")
        exit(1)
    
    return True

#!!!We want to give the competitors s2 as the password
s1 = bytes.fromhex('d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70')
s2 = bytes.fromhex('d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70')

#compute hex hashes
h1 = hashlib.md5(s1).hexdigest()
h2 = hashlib.md5(s2).hexdigest()

#request user input
i1 = input("Enter valid hex password now:\n")

#CHECK 1- ensure that input is hex characters only! 
is_hexadecimal(i1)

#CHECK 2- compute the hash for the inputed pasword (Saved as h3)
i1 = bytes.fromhex(i1)
h3 = hashlib.md5(i1).hexdigest()

#CHECK 3- Check if the hashes match, if not, exit
if h3 == h2:
    print("hashes match!")
    print("Expected hash: ", h2)
    print("computed hash: ", h3)
else:
    print("Hashes do not match, incorrect password.\n")
    print("Expected hash: ", h2)
    print("computed hash: ", h3)
    exit(1)

#CHECK 4- Check that inputed password is the collision password. The password we are looking for is s1, s2 is given to the competitor.

if s1 == i1:
    print("Correct password! byuctf{CrashImpactSmashClashJoltBumpCrunch}") #password matches what it should be!! Give flag
    exit(1)
if s2 == i1:
    print("Incorrect pasword, please try again.")
    exit(1)

