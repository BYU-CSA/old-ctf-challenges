## Vigenere 1

- Category: Cryptography
- Difficulty: Easy
- Author: Tanner Meeves

Description:
This is a famous cipher called the Vigenere cipher. I have used this cipher to encrypt a secret hot take of mine. Unfortunately, it takes a key to decrypt. So my secret should be safe as long as no one knows the key. I'm confident you won't guess the key either because the key is the name of a dinosaur.

Flag:
byuctf{the_good_dinosaur_is_a_good_movie}

Solution:
The key is brachiosaurus. Looking at the ciphertext, you can see that the byuctf{} signature is still present. You can use the first few characters known of the plaintext as byuctf, and find the first 6 letters of the key. That will help the user know what the complete name of the dinosaur is.
