cipherText = input("Enter the encrypted text : ")
distance = int(input("Enter the distance: "))

plainText = ""

k=128

for i in cipherText:
    new_distance = ord(i)-(distance%k)
    if new_distance < 0:
        new_distance   = new_distance + k
    plainText = plainText + chr(new_distance)
    
print("Plain text is : %s" %plainText)
