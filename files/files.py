#1, 2 f = open("files_in_files/test.txt", "a+")
#
# f.seek(0)
# f.write("Javohir Mamadiyorov\n")
# f.seek(0)
#
# print(f.read())
#
# f.close()

#3 f = open("files_in_files/test.txt", "a+")
#
# f.write("""Tong saharda shabada mayin esardi. Ko‘chalar hali
# jim, faqat qushlarning sayrashi eshitilardi.
# Daryo bo‘yidan tuman asta-sekin ko‘tarilayotgan, quyoshning
# ilk nurlari yer yuzini iliqlikka to‘ldirardi.
# Shu payt Ahmad eski daftarini ochib, yangi kun uchun reja yozishni boshladi — har kuni bir qadam oldinga, har kuni bir oz yaxshiroq
# bo‘lish uchun.
# """)
#
# print(f.read())
#
# f.close()

#4 f = open("files_in_files/test.txt", "r")
#
# print(len(f.readlines()))
#
# f.close()

#5 f = open("files_in_files/test.txt", "r")
#
# text = f.read()
#
# f.close()
#
# print(len(text.split()))

#6 f = open("files_in_files/test.txt", "r")
#
# text = f.read()
#
# f.close()
#
# print(len(text))

#7 f = open("files_in_files/test.txt")
# text = f.read()
# f.close()
#
# f2 = open("files_in_files/test2.txt", "x")
# f2.write(text)
# f.close()
#
# print("Success!")

#8 f = open("files_in_files/test.txt", "r")
# text = f.readlines()
# f.close()
#
# for i in range(len(text)):
#     print(f"{i+1}: {text[i]}")

#9 try:
#     open("files_in_files/hello", "x")
# except FileExistsError:
#     print("File exists, continue...")
#
# f = open("files/hello.txt", "r")
# text = f.read()
# print(text)
# print("saharda" in text)

#10 for i in range(5):
#     open(f"files_in_files/test1_{i+1}.txt", "x")