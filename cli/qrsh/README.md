# QRSH
Level - medium

Description:
> You've heard of `sh`, you've heard of `bash`, you know and love `ash`,
> `zsh`, and `fish`. Now try `qrsh`, you'll love it!
>
> `nc byuctf.xyz 40012`

## Hosting

This challenge's Docker image relies on a Docker image made by the Google team: [google/nsjail](https://github.com/google/nsjail). Clone the directory, then build the image inside it:

```bash
git clone https://github.com/google/nsjail.git
cd nsjail
docker build -t nsjailcontainer .
```

Now that the image is built, you can build the challenge's Docker image like so:

```bash
cd qrsh # or wherever
docker build -t qrsh .
```

Then run the container this way:

```bash
docker run --rm -d -p 40012:9000 --privileged --name qrsh qrsh
```

## Writeup
Log into server, type `ls -l` to get an `xxd` output of the command.
Un-`xxd`, open the resulting PNG. See there's a `flag_99lwmxip.txt`.
Type `cat flag_99lwmxip.txt` (and convert from text to PNG to text) to
get the flag.

**flag:** `byuctf{does_this_count_as_a_gui_vg8rhfst}`
