## Looking forward to strong passwords
Level - TBD
Misc

Description
```
Pick the flag to rule them all. If the flag (including the byuctf{) is longer than 82 characters it could be shorter.

=== rule these ===
byuctf{my_c0rv3tTe}
byuctf{hi*bY38n3ver}
byuctf{we ar3BYU}
byuctf{to&M0rr0w}
byuctf{im@Cs4}
byuctf{be%oNe01}
byuctf{mc=eEinst3in}
byuctf{am|Pm711}
byuctf{il#Rul3Th3m4ll}
byuctf{di[N0s4ur}

=== not these ===
byuctf{6o2theraces}
byuctf{byu_rules!}
byuctf{by|_|Fo0tb4ll}
byuctf{cybersecurity}
byuctf{C5|T|5}
byuctf{not the answer}
byuctf{N3V3R.G01NG.T0.G1V3.Y0U.UP}
byuctf{pr@Fortnite}
byuctf{As*1am}
byuctf{im,AllUNeed}
```

### Flags
Challenge flag(s): these should be static flags - `byuctf{[a-z]{2}[^a-zA-Z](?![^0-9a-zA-Z]).*(?=.*[0-9]).*(?=.*[a-z]).*(?=.*[A-Z]).*}`,
`byuctf{[a-z]{2}[^a-zA-Z](?![^0-9a-zA-Z]).*(?=.*[0-9]).*(?=.*[a-z]).*(?=.*[A-Z]).*`

### Hints
Hint(s): How do passwords checkers know if a user inputs a strong password?

### Other
Setup instructions: None
Walk through of how to solve:
The pattern to look for is two lowercase characters followed by a special character that is followed by at least 1 lowercase, 1 uppercase, and one number.

Note: This may not be the only regex that matches. Hopefully it is the shortest. We may want to do further testing to find alternative flags.
