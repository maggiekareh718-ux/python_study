text="software developer"
text1=text.capitalize()
print(text1)

#casefold->converts strings to lowercase
text2=text.casefold()
print(text2)

#lower->converts strings to lowercase
text3=text.lower()
print(text3)

#upper->converts strings to uppercase
text4=text.upper()
print(text4)

#count->counts the number of appearance of a specific character in a string
print(text.count('e'))
#.strip()->removes leading and trailing spaces
text_strip='   software developer   '
text_strip=text_strip.strip()
print(len(text_strip))

#.find()->returns the index of the first occurence of a character returns -1 if the character is not available
text="software Developer"
print(text.find('d'))

#.index()->returns the index of the first occurence of a character returns an error if the character is not available
print(text.index(('D')))

#replace
text=text.replace('software','Python')
print(text)

email="maggiekareh@gmail.com"
split_email=email.split('@')
print(split_email)
text="software Developer"
txt=text.split()
print(txt)

text="   jUnIoR deVelOper"

text=text.strip()
print(text)

text=text.capitalize()
print(text)