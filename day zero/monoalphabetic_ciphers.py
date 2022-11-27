class MonoalphabeticCipher:

    def __init__(self, key):
        self.encrypted_message = ""
        self.decrypted_message = ""
        self.plain_message = ""
        self.key = ""
        self.alpha = "abcdefghijklmnopqrstuvwxyz" # Base alphabets

        # Generating key as per input by user
        for _ in key:
            if _ == " ": continue
            elif _ not in self.key: self.key += _


    def encrypt(self, plain_message):  # Function to encrypt plain message to cipher text
        self.plain_message = plain_message
        for _ in self.plain_message:
            if _ == " ":
                self.encrypted_message += " "
            else:
                self.encrypted_message += self.key[self.alpha.index(_)]
        if plain_message != self.encrypted_message:
            print("\n["+u'\u2714'+"] Successfully Encrypted\n")
        else:
            print("\n[" + u'\u2716' + "] Problem in Encryption\nTry with different key\n")


    def decrypt(self, ciphertext):  # Function to decrypt cipher text to plain message
        for _ in ciphertext:
            if _ == " ":
                self.decrypted_message += " "
            else:
                self.decrypted_message += self.alpha[self.key.index(_)]

        if self.decrypted_message == self.plain_message:
            print("\n["+u'\u2714'+"] Successfully Decrypted\n")
        else:
            print("\n[" + u'\u2716' + "] Problem in Decryption\n")


# Making an instance of MonoalphabeticCipher Class and passing value of number of rotation
Raven = MonoalphabeticCipher("The quick brown fox jumps over the lazy dog".lower())

# Passing plain message to encrypt function of MonoalphabeticCipher Class
Raven.encrypt(plain_message=input("Enter a message: ").lower())
enc_msg = Raven.encrypted_message # fetching encrypted message/ciphertext generated by encrypt method
print("Encrypted Message: "+enc_msg)

# Passing encrypted message to decrypt function of MonoalphabeticCipher Class
Raven.decrypt(ciphertext=enc_msg)
dec_msg = Raven.decrypted_message # fetching encrypted message/ciphertext generated by decrypt method
print("Decrypted Message: "+dec_msg)
