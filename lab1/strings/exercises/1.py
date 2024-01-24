#exercises
#22
x = "Hello World"
print(len(x))

#23
txt = "Hello World"
x = txt[0]
#output: H

#24
txt = "Hello World"
x = txt[2:5]
#output: llo

#25
txt = " Hello World "
x = txt.strip()
#Return the string without any whitespace at the beginning or the end.

#26
txt = "Hello World"
txt = txt.upper()

#27
txt = "Hello World"
txt = txt.lower()

#28
txt = "Hello World"
txt = txt.replace("H", "J")

#29
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))