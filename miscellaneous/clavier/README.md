# Clavier
Level: Medium

Description:
```
Mon ordinateur ne marche plus. Je ne sais pas pourquoi mon mode de passe n'est pas correct. Pouvez vous m'aider?

`nc byuctf.xyz 40013`
```

## Writeup
**Flag** - `byuctf{vivre°en°frqnce°le°clqvier°frqncqis°est°le°;eilleur°qllew°qwertyaz;}`

## Hosting
This challenge should be a Docker container that runs the python script `clavier.py` every time someone connects on port 40013. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t clavier .
```

The command to start the challenge is:

```bash
sudo docker run -p 40013:40000 --detach --name clavier clavier:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop clavier
```