## Vigenere 2

- Category: Cryptography
- Difficulty: Medium
- Author: Tanner Meeves

Description:
This is a famous cipher called the Vigenere cipher. I have used this cipher to encrypt a secret hot take of mine. Unfortunately, it takes a key to decrypt. So my secret should be safe as long as no one knows the key. I'm confident you won't guess the key either because the key is the name of a dinosaur.

Wrap the flag inside byuctf{}

Flag:
byuctf{the_third_ice_age_movie_is_the_best_of_them_all}

Solution:
The key is allosaurus. This time there is no byuctf{} to look for. So you will have to search through common dinosaurs and try them as the potential key in a vigenere decoder. Then you wrap that message in byuctf{} and that's the flag
