# Fetaverse
Level: Medium

Description:
```
Come explore the fetaverse of cheesy puns and pics. It's an un-brie-lievably well-designed site!

`http://fetaverse.byuctf.xyz`
```

## Writeup
If you access the images directory which is listable, you will find the memes folder. One of the memes has the flag hidden in the image.

**Flag**: `byuctf{welc0me_t0_the_fetaverse}`

## Hosting
Move the static files to a new Nginx subdomain, and modify the configuration file `/etc/nginx/sites-available/fetaverse.byuctf.xyz` by adding the following line inside of the `location / {}` block - `autoindex on;`. This should allow directories to be listable.