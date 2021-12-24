# Shadows
**Level**: Medium

**Points**: 454

**Author**: Micheal Erickson

**Description**:
```markdown
We've managed to get the `/etc/passwd` and `/etc/shadow` files from a target computer. Would you mind cracking the account for stark?

The flag is in the format `ctf{cracked-pw}`

[passwd] [shadow]
```

## Writeup
We will use John the Ripper and [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) for this challenge.

```shell
unshadow passwd shadow > unshadowed
john unshadowed --wordlist=/usr/share/wordlists/rockyou.txt 
```

**Flag** - `ctf{patriciaa}`