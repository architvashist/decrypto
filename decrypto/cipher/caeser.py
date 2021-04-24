class Caesar:

    def _decrypt(message, key = None):
        ans = ""
        key = 26 - key
        # traverse message
        for i in range(len(message)):
            char = message[i]
            ans += chr((ord(char) + key - 97) % 26 + 97)

        return ans

    @classmethod
    def decrypt(cls, message):
        message = message.lower()
        data = {}
        # traverse message
        for i in range(1, 26):
            data.update({ i : cls._decrypt(message, key=i) })
        return {"Caesar" : data}