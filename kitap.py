fruit = "banana"
for ch in fruit:
    print(ch)
    
    
prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    print (letter + suffix)
    
"""word = input("kelime girin: ")
if word == "muz":
    print("2 tane muz var")
elif word<"muz":
    print(word + " muzdan önce gelir")
elif word>"muz":
    print(word + " muzdan sonra gelir")
else:
    print("hiç muz yok")
    """
def f(strng, ch):
    index = 0
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
f("merhaba","h")