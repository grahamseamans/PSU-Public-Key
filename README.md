# Psu Public Key
* Graham Seamans
* seamansgraham@gmail.com
### To Run
* Place the plaintext into `./plaintext.txt` or the ciphertext into `./ciphertext.txt`
* Run: `python src/driver.py x` where `x` is `d` for decrypt, `e` for encrypt, or `k` for making keys.
* Find the plaintext, ciphertext, or keys in the appropriate file.

### Notes
* This runs with ASCII encode and decode so things will get weird with UTF-8 files, although the majority of the text will be just fine.

### Included Files
* `./plaintext.txt` - Put the plain text here to encrypt or find it here after decryption.
* `./ciphertext.txt` - Put the cipher text here to decrypt or find it here after encryption.
* `./prikey.txt` - Where private keys are stored.
* `./pubkey.txt` - Where public keys are stored.
* `./src/driver.py` - Takes user input about whether to encrypt and decrypt and reads from `plaintext.txt` and `cyphertext.txt`. interfaces with `crypt.py`.
* `./src/crypt.py` - Makes the keys, runs the encrypt and decrypt.
* `./src/utility.py` - Makes the primes and has Miller-Rabin implementation.
