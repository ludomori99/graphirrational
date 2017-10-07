
           # VAR
value = 'e'

name = str(value)+".txt"
pre_file = "pre.txt"
in_file = open(pre_file,"r")
out_file = open(name, "w")
text = in_file.read()
final_nums = ''
for val in text:
	if ord(val) >= 48 and ord(val) <= 57:
		final_nums += val

out_file.write(final_nums)
out_file.close()
in_file.close()
print('finish')