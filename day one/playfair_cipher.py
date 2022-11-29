class PlayFair:

    def __init__(self):
        self.basealphabets = "abcdefghijklmnopqrstuvwxyz"
        self.key = []


    def generate(self, key):
        temp_key = ""
        temp_elements = []
        for letter in key + self.basealphabets:
            if letter in " j": continue
            elif letter not in temp_key: temp_key += letter

        for i in range(len(temp_key)):
            temp_elements.append(temp_key[i])
            if ((i+1) % 5) == 0:
                self.key.append(temp_elements)
                temp_elements = []



obj = PlayFair()
obj.generate(key="monarchy")