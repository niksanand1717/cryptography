class CaesarCipher():
    def __init__(self, rot):
        self.k = rot # Specifying Rotaion
        self.plain_message = ""
        self.encrypted_message = ""
        self.decrypted_message = ""
        self.alpha = "abcdefghijklmnopqrstuvwxyz" # Base alphabets
        self.rotated = self.alpha[rot:]+self.alpha[:rot] # Rotated left values

    def encrypt(self, plain_message): # Function to encrypt plain message to cipher text
        self.plain_message = plain_message
        for _ in plain_message:
            self.encrypted_message += self.alpha[self.rotated.find(_)]
        if plain_message != self.encrypted_message:
            print("\n["+u'\u2714'+"] Successfully Encrypted\n")
        else:
            print("\n[" + u'\u2716' + "] Problem in Encryption\nTry to select rotation\nbetween 1-25")

    def decrypt(self, ciphertext): # Function to decrypt cipher text to plain message
        for _ in ciphertext:
            self.decrypted_message += self.rotated[self.alpha.find(_)]
        if self.decrypted_message == self.plain_message:
            print("\n["+u'\u2714'+"] Successfully Decrypted\n")
        else:
            print("\n[" + u'\u2716' + "] Problem in Decryption\n")

# Making an instance of CaesarCipher Class and passing value of number of rotation
Raven = CaesarCipher(rot=13)

# Passing plain message to encrypt function of CaesarCipher Class
Raven.encrypt(plain_message=input("Enter a message: ").lower())
enc_msg = Raven.encrypted_message # fetching encrypted message/ciphertext generated by encrypt method
print("Encrypted Message: "+enc_msg)

# Passing encrypted message to decrypt function of CaesarCipher Class
Raven.decrypt(ciphertext=enc_msg)
dec_msg = Raven.decrypted_message # fetching encrypted message/ciphertext generated by decrypt method
print("Decrypted Message: "+dec_msg)
