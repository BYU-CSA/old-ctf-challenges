# Predictodactyl

- Difficulty: easy
- Author: obet

## Description
```
What is the next word in (___)?

Flag format is byuctf{words_then_eight_alphabetical_characters_jciwkzsv}

[predictodactyl.tar.gz]
```
Author: obet


## Hosting
The command to build the docker container is (when located inside of the `src/` directory):

```bash
sudo docker build -t predictodactyl .
```

The command to start the challenge is:

```bash
sudo docker run -p 40013:8000 --detach --name predictodactyl predictodactyl:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop predictodactyl
```