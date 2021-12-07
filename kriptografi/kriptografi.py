print("Pilih mode: 1) Enkripsi 2) Dekripsi")
mode = input(">>> ")
inp = input('Masukkan pesan rahasia: ')
kode = input('Masukkan kode rahasia: ')


# cek isi kode harus desimal
if kode.isdecimal():
	# cek isi mode
	if mode.isdecimal() and mode in ['1','2']:
		kode = int(kode)
		# positif mode nya 1, negatif modenya 2
		kode = (kode * -1) if mode == '2' else kode
		# if mode =='2':
		# 	kode = kode *-1
		# else:
		# 	kode
		# ubah huruf ke asci ord(a) or sebaliknya chr(a)
		out = ''
		for c in inp:
			# rumusnya ((ord(a)+key-abjad terkecil)modulus 26(total alfabet) )+ 65 = ((ord(a) - 3 +65)%26) 65
			if c.isupper():
				out += chr((ord(c) + kode - 65) %26 + 65)
			elif c.islower():
				out += chr((ord(c) + kode - 97) % 26 + 97)
			else:
				out += c
		print(f"Hasil : {out}")

	else:
		print('mode tidak ada')

else:
	print("Kode bukan angka")
