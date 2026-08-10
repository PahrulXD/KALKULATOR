import os

def masuk():
	os.system("clear")
	print ("\033[1;97m[\033[1;92m1\033[1;97m] penjumlahan")
	print ("\033[1;97m[\033[1;92m2\033[1;97m] pengurangan")
	print ("\033[1;97m[\033[1;92m3\033[1;97m] pembagian")
	print ("\033[1;97m[\033[1;92m4\033[1;97m] perkalian")
	operator = input("\n- pilih : ")
	angka1 = int(input("\n- masukkan angka pertama: "))
	angka2 = int(input("- masukkan angka kedua: "))
	if operator == "1":
		hasil = angka1 + angka2
		print ("\n\033[1;97m- hasil :\033[1;92m",hasil)
	elif operator == "2":
		hasil = angka1 - angka2
		print ("\n\033[1;97m- hasil :\033[1;92m",hasil)
	elif operator == "3":
		hasil = angka1 / angka2
		print ("\n\033[1;97m- hasil :\033[1;92m",hasil)
	elif operator == "4":
		hasil = angka1 * angka2
		print ("\n\033[1;97m- hasil :\033[1;92m",hasil)
	else:
		exit()
		

masuk()
