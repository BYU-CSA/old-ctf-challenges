# Blue 3?
Level: Hard

Description:
> Oh my gosh I'm so sick of the color blue. Hasn't this been done
> before? Make an original challenge!
>
> Maybe if there's enough of these, someone will make a blue-solving
> tool...
>
> Flag format: `byuctf{[0-9a-zA-Z_]*}`
>
> [blue.png](./blue.png)

## Write-up
This challenge was created by taking a flag, splitting it into
individual characters, and adding 1 to a random color channel in a pixel
in a section. The sectioning is as follows, for the flag `ctf{123}`:

```
blue.png
┌─┬──────────────┐
│c│              │
├─┼─┐            │
│ │t│            │
│ └─┼─┐          │
│   │f│          │
│   └─┼─┐        │
│     │{│        │
│     └─┼─┐      │
│       │1│      │
│       └─┼─┐    │
│         │2│    │
│         └─┼─┐  │
│           │3│  │
│           └─┼─┐│
│             │}││
│             └─┘│
└────────────────┘
```

The result is some slightly-not-the-same blue along the diagonal. It is
created using a base image of solid blue (made on-the-fly) in
[`create.py`](./create.py) which grabs text from
[`flag.txt`](./flag.txt).

It can be solved by guessing the proper length of the flag, counting all
the differences in each section to make a character, and seeing if that
matches our flag format. (See [`solve.py`](./solve.py).)

Hard mode is giving out `blue.png` alone. Easy mode is giving out
`create.py` as well. I think there are some participants who might like
another blue challenge, namely Liam (or myself), on hard mode. That's
why I left it off. (Also, the original was like this.)

**Flag** - `byuctf{more_blue_steganography_da_ba_dee_nkiY9CyP}`