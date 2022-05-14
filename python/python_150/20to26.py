# 20
name = input("Enter your name")
print(len(name))
# 21
first = input("First name: ")
last = input("Last name ")
full = first+' '+last
print(full, len(full))

# 22
first = input("First name in lowercase: ")
last = input("Last name in lowercase: ")
full = first.capitalize()+' '+last.capitalize()
print(full)

# 23
phrase = input("Enter the first line of song: ")
print(len(phrase))
startindex = int(input("Enter startindex "))
endindex = int(input("endindex"))
print(phrase[startindex:endindex])

# 24
temp = input("Enter anything ")
print(temp.upper())

# 25
name = input("Enter your name: ")
if len(name) < 5:
    lastname = input("Enter your last name")
    print((name+lastname).upper())
else:
    print(name.lower())

# 26
pig = input("Enter a word: ")
if pig[0].lower() == 'a' or pig[0].lower() == 'e' or pig[0].lower() == 'i' or pig[0].lower() == 'o' or pig[0].lower() == 'e':
    pig += "way"
    print(pig)
else:  # 문자열 수정 안됨###
    temp = pig[0]
    templast = pig[-1]
    ans = pig[1:len(pig)] + temp + "ay"
    print(ans)
