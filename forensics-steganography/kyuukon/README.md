## Kyuukon
* Category: Forensics
* Difficulty: Hard
* Author: Richard Fountain

Description: 
```
It looks like we managed to get our hands on a sensitive folder. We're not quite sure what we're looking at though so maybe you can take a crack at it?

https://drive.google.com/file/d/1zrKNUx8-d9mA6wbYMwvJ2VRSpxByista/view?usp=sharing 

```

## Writeup
This gives you a file which contains two Firefox profiles - using the tool [firepwd](https://github.com/lclevy/firepwd), you can extract the username/password for byu.ctfd.io - `admin:byuctf{yBv9NbniJMsWmR1lYSOo}`. Note that this project will not run on Python >=3.10. 

**Flag**: `byuctf{yBv9NbniJMsWmR1lYSOo}`