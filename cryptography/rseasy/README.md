# RSeAsy
Level - Medium

Description:
> I made an RSA challenge. 4096-bit RSA is supposed to be unbreakable, right?
>
> [`create.py`](./create.py) [`output.txt`](./output.txt)

## Writeup
Because `p` and `q` are so close, we can figure out one of them by
finding the next prime number after `isqrt(n)` (where `isqrt(n)` is the
integer square root of `n`).

**Flag** - `byuctf{easy_rsa_is_rseasy_right_8n260p3b}`