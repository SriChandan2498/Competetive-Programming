# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
    s = ""
    for i in msg:
        if i.isalpha():
            ascii_value = ord(i)
            if ascii_value>=65 and ascii_value<=90:
                new_value = ascii_value + shift
                if new_value>90:
                    new_value = 65 + (new_value-1-90)
                    s += chr(new_value)
                elif new_value<65:
                    new_value = 90 - (65 - new_value-1)
                    s += chr(new_value)
                else:
                    s += chr(new_value)
            if ascii_value>=97 and ascii_value<=122:
                new_value = ascii_value + shift
                if new_value>122:
                    new_value = 97 + (new_value-1-122)
                    s += chr(new_value)
                elif new_value<97:
                    new_value = 122 - (97 - new_value-1)
                    s += chr(new_value)
                else:
                    s += chr(new_value)
        else:
            s += i
    return s




