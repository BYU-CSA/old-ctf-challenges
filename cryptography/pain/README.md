# The Most Worthy Distinction of Pain
Level: Hard

Description:
> We intercepted a code:
> 
> [`encrypted.txt`](./encrypted.txt)
>
> Yeah, so, this is a lot of nonsense. It's mostly words that start with
> `d`, but at least we know how it was created?
>
> [`encrypt.go`](./encrypt.go)
>
> We also know where the dictionary file came from:
> [`CROSSWD.TXT`](https://www.gutenberg.org/files/3201/files/CROSSWD.TXT)
>
> Note: The `CROSSWD.TXT` file can be verified with an md5 hash of
> `e58eb7b851c2e78770b20c715d8f8d7b`. It starts with 1st word `aa`, and
> ends with the 113809th word `zymurgy`.

## Writeup
This challenge takes in text, combines each two letters pairwise, gets
their combined encoding, and gets that nth word from the dictionary. As
it turns out, that's mostly the `d`s of this particular dictionary.

It can be solved by taking each word, finding its position in the
dictionary, taking the `0xff00` mask for the first letter the word
represents, and the mask `0x00ff` for the second letter.

**Flag** - `byuctf{what_an_inefficient_code_ug2Ko8Cz}`