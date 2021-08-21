
f = open("words.txt", "r", encoding="utf8")
f_s = open("../words_short.txt", "a", encoding="utf8")
f_m = open("../words_med.txt", "a", encoding="utf8")
f_l = open("../words_long.txt", "a", encoding="utf8")

invalid_strs=list(open("names.txt", "r", encoding="utf8"))
roman=["VIII", "LXXX", "DCCC"]
invalid_strs=invalid_strs+roman

f_s.truncate(0)
f_m.truncate(0)
f_l.truncate(0)

flag=True;
for line in f:
	if(line in invalid_strs):
		line=''

	if(len(line) > 4 and len(line)<=7 and (not line.isupper())):
		flag=True
		for char in line:
			if(char == '-' or char == 'k' or char == 'y' or char == 'w' or char == 'K' or char == 'Y' or char == 'W'):
				flag=False
		if(flag==True):
			f_s.write(line.upper())
	elif(len(line) > 6 and len(line)<=10 and (not line.isupper())):
		flag=True
		for char in line:
			if(char == '-' or char == 'k' or char == 'y' or char == 'w' or char == 'K' or char == 'Y' or char == 'W'):
				flag=False
		if(flag==True):
			f_m.write(line.upper())
	elif(len(line) > 10 and len(line) < 14):
		flag=True
		for char in line:
			if(char == '-' or char == 'k' or char == 'y' or char == 'w' or char == 'K' or char == 'Y' or char == 'W'):
				flag=False
		if(flag==True):
			f_l.write(line.upper())