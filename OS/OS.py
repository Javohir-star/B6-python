#1 with open("files/test.txt", "r") as f:
#     print(f.read())

#2 with open("files/test.txt", "w") as f:
#     f.write("Hello Eshmat\n"
#             "Hello Toshmat\n"
#             "Hello Gulchapchap")

#3 with open("files/test.txt", "r+") as f1, open("files/test2.txt", "r+") as f2:
#     res = f1.read()
#     f2.write(res)

#4 with open("files/test.txt", "w") as f1,\
#     open("files/test2.txt", "w") as f2,\
#     open("files/test3.txt", "w") as f3:
#
#     for f in (f1, f2, f3):
#         f.write("Hello")

# import os
# import time

#1 print(os.getcwd())

#2 os.chdir("files")
# print(os.getcwd())

#3 print(os.listdir("files"))

#28 os.makedirs("testdir")
# os.chdir("./testdir")
# for i in range(5):
#     open(f"file_{i + 1}.txt", "x")
# open("file6.go", "x")
#
# print("TXT files are created...")
# time.sleep(10)
#
# for filepath in os.listdir(os.curdir):
#     filename, ext = filepath.split(".")
#     if ext == "txt":
#         os.rename(f"{filename}.{ext}", f"{filename}.bak")
#
# print("Waiting for user to check...")
# time.sleep(60)
#
# for file in os.listdir(os.curdir):
#     os.remove(file)
# os.chdir(os.pardir)
# os.rmdir("./testdir")
# print("Musorlar tozalandi!")

