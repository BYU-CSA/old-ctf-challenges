# Woodchuck
**Level**: Medium

**Points**: 498

**Author**: Micheal Erickson

**Description**:
```
We've captured an encoded message by some tongue-twister enthusiasts. Can you decode it?

[woodchuck.txt]
```

## Writeup
The challenge looks really confusing at first since it has the words `wood` and `chuck` a lot in what seems to be a random pairing, but closer inspection will reveal a pattern - each line starts with the phrase `How much wood would a ` and ends with the phrase `wood?`. When these beginning and ending phrases are stripped from each line, you'll find another pattern, where each line is composed of two different phrases repeated in different orders - `woodchuck could chuck ` and `woodchuck chuck if a `.

If you substitute `woodchuck could chuck ` for a `0` and `woodchuck chuck if a ` for a `1` and binary decode it, you'll get the flag.

Flag: `ctf{i_bet_he_could_chuck_a_heck_of_a_lot_of_wood}`