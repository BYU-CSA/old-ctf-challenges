# Automation
**Level**: Hard

**Author**: Justin Giboney

**Description**:
```markdown
[password_1.png]
[flag_1.zip]

Note - the format is NOT `ctf{text}`, it's `flag{text_here}`
```

## Writeup
The password to each file is translated into Morse code and placed in the picture. This pattern is dozens of layers deep. This can be solved either by manually decoding each picture in Morse code (which would take hours), or creating a wordlist of every possible combination of 3 characters and brute forcing each one.

**Flag** - `flag{automation_is_the_best}`