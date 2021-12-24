# Austenland
**Level**: Medium

**Points**: 442

**Author**: Anna Pratt

**Description**:
```markdown
Elizabeth zipped some files for her Jane Austen blog and sent them to a friend. A flag was hidden along the way, can you find it?

[Austenland.zip]
```

## Writeup
When the ZIP file is unzipped, there are three documents - two Word documents and a hidden ZIP file called `.secrets.zip`. The period hides it in Linux, and it was also hidden in Windows. This secret ZIP file was also password protected. While reading through the Word documents, one would find that the character uses the password `spellbound`, which is also the password to the secret ZIP file. Once unzipped, `.secrets.zip` reveals another Word document with the flag inside.

**Flag** - `ctf{B7U-W1NN3R-4UST3N}`