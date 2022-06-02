# Wordle
Level: Easy

Description:
> It's just wordle.
>
> `nc byuctf.xyz 40009`

## Write-up
It's literally just wordle.

**Flag** - `byuctf{simple_little_wordle_AYhrQTWb}`

## Hosting
This challenge needs to allow many people to connect to it, at the same
time. Using `netcat` normally doesn't allow for that. I've found a
utility called `tcpserver` created by `ucspi` which is a TCP
_server_—that is, it acts like an HTTP server, but for TCP connections
instead.

Use the `Dockerfile` provided, by downloading these files, and while
in the directory, running:

```bash
docker build -t wordle .
docker run --rm -p 40009:9000 -d --name wordle wordle
```

Test it out with:
```bash
nc localhost 40009
```