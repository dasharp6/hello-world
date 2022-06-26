def caesar(plainText, shift):
    cipherText = ""
    for char in plainText:
        newChar = ord(char) + shift
        if newChar > 128:
            newChar = newChar % 128
        finalChar = chr(newChar)
        cipherText += finalChar
    return cipherText

text = input("Enter plain text: ")
s = input("Shift: ")
print(caesar(text, int(s)))
