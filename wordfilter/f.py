
words = open("words.txt", "r", encoding="utf8")
f4 = open("../words4.txt", "a", encoding="utf8")
f5 = open("../words5.txt", "a", encoding="utf8")
f6 = open("../words6.txt", "a", encoding="utf8")
f7 = open("../words7.txt", "a", encoding="utf8")
f8 = open("../words8.txt", "a", encoding="utf8")
f9 = open("../words9.txt", "a", encoding="utf8")
f10 = open("../words10.txt", "a", encoding="utf8")
f11 = open("../words11.txt", "a", encoding="utf8")
f12 = open("../words12.txt", "a", encoding="utf8")

#Clear files
f4.truncate(0)
f5.truncate(0)
f6.truncate(0)
f7.truncate(0)
f8.truncate(0)
f9.truncate(0)
f10.truncate(0)
f11.truncate(0)
f12.truncate(0)

flag=True;
for line in words:
	if len(line)-1 == 4:
		f4.write(line.upper())
	elif len(line)-1 == 5:
		f5.write(line.upper())
	elif len(line)-1 == 6:
		f6.write(line.upper())
	elif len(line)-1 == 7:
		f7.write(line.upper())
	elif len(line)-1 == 8:
		f8.write(line.upper())
	elif len(line)-1 == 9:
		f9.write(line.upper())
	elif len(line)-1 == 10:
		f10.write(line.upper())
	elif len(line)-1 == 11:
		f11.write(line.upper())
	elif len(line)-1 == 12:
		f12.write(line.upper())