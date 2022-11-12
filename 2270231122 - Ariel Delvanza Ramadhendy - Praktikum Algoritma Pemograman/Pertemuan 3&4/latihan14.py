# Pertemuan 3
data = ("ini adalah string")

print (data)
print (type(data))

# Cara membuat string

'''
 1. dengan menggunakan single quote '...'
 2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'

print(data)

data = "Mengguanakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# Mengguanakan tanda \
# Membuat tanda ' menjadi string

print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

#backlash
print("C:\\user\\Ucup")

#tab
print("ucup\t\t\totong, semakin jauhan")

#backspace
print("ucup\botong, jadi deketan")

#newline
print("baris pertama.\rbaris kedua.") # LF -> Line Feed -> unix,macos,linux

print("baris pertama.\rbaris kedua.") # CR -> Cariange Return -> commodore, acorn, lisp

print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau raw
# hati-hati
print('C:\new folder') # akan salah pathnya
# menggunakan raw string
print(r'C:\new folder')
# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD 
""")
# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal 
Website : www.ucup.com/newID
""")



