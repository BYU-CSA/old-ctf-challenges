# Pixecutable
Level: Easy

Description:
> I've taken an executable which would output the flag, and I instead
> hid it inside an image where you'll never be able to retrieve it!
>
> [`hidden.png`](./hidden.png) [`hide.py`](./hide.py)

## Write-up

This challenge takes an executable, and uses its binary representation
as the colors for an image. It is created using `hide.py`, and can be
unhidden using `unhide.py`.

For this challenge, I made a simple Go program to write the flag to the
screen, and built it, to use as the input. All you need is access to a
Linux box to run the result from `unhide.py`, or just run `strings` and
`grep`.

**Flag** - `byuctf{i_think_the_output_is_kinda_cool_uGyvv455}`