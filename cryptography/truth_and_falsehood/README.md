# Truth and Falsehood
Level: Easy

Description:
> Someone tried to send me the flag, but I think I missed a few
> characters, because most of this doesn't make sense.
>
> The flag should be in `byuctf{[a-zA-Z0-9_]*}` format, but I don't see
> it there.
>
> [truth64.txt](./truth64.txt)

## Write-up
This challenge was created by hiding a flag in a long text document,
then encoding that to base64, then removing characters periodically from
that. It is solved by either removing some characters or adding some
characters to the beginning of the file, to change which sections are
properly decoded. You can find it with the following command:

```bash
base64 -d <(echo -n "aa"; cat truth64.txt ) | grep 'byuctf{[a-zA-Z0-9_]*}'
```

Send the `truth64.txt` as the challenge, not `truth.txt`.

**Flag** - `byuctf{base64_has_no_error_corrections_a5EdFabe}`