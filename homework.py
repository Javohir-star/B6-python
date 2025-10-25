import os
from pathlib import Path

# 1
print("Current dir:", os.getcwd())

# 2
os.makedirs("../OS/subfolder_example", exist_ok=True)
os.chdir("../OS/subfolder_example")
print("After cd:", os.getcwd())

# 3
print("Contents:", os.listdir())

# 4
os.mkdir("practice_dir")
print("Created:", os.path.exists("practice_dir"))

# 5
fpath = os.path.join("practice_dir", "file.txt")
f = open(fpath, "w")
f.write("salom")
f.close()
print("File exists:", os.path.exists(fpath))

# 6
os.rename("practice_dir", "test_dir")
print("Renamed:", os.path.exists("test_dir"))

# 7
os.remove(os.path.join("test_dir", "file.txt"))
print("Removed file:", not os.path.exists(os.path.join("test_dir", "file.txt")))

# 8
os.rmdir("test_dir")
print("Removed dir:", not os.path.exists("test_dir"))

# 9
print("os.name =", os.name, "→ nt=Windows, posix=Linux/Mac")

# 10
print("Join:", os.path.join("data", "notes.txt"))

# 11
head, tail = os.path.split("/home/user/docs/file.txt")
print("Head:", head)
print("Tail:", tail)

# 12
print("Basename:", os.path.basename("/home/user/docs/file.txt"))

# 13
print("Dirname:", os.path.dirname("/home/user/docs/file.txt"))

# 14
print("isdir:", os.path.isdir(".."))
print("isfile:", os.path.isfile(__file__))

# 15
os.makedirs("a/b/c", exist_ok=True)
os.rmdir("a/b/c")
os.rmdir("a/b")
os.rmdir("a")
print("Nested dirs made and removed")

# 16
print("TXT files:")
for i in os.listdir():
    if i.endswith(".txt"):
        print(i)

# 17
for i in os.listdir():
    if i.endswith(".txt"):
        os.rename(i, i[:-4] + ".bak")

# 18
for root, dirs, files in os.walk("../OS"):
    for f in files:
        print(os.path.abspath(os.path.join(root, f)))

# 19
print("curdir:", os.curdir)
print("pardir:", os.pardir)



# 1
print("cwd:", Path.cwd())

# 2
print("home:", Path.home())

# 3
p = Path("example.txt")
print("example.txt exists:", p.exists())

# 4
temp = Path("temp_data")
temp.mkdir(exist_ok=True)
print("Created:", temp.exists())

# 5
f = temp / "greeting.txt"
f.write_text("Hello, World!")

# 6
print("Read:", f.read_text())

# 7
newf = temp / "welcome.txt"
f.rename(newf)
print("Renamed:", newf.exists())

# 8
newf.unlink()
print("Deleted:", not newf.exists())

# 9
print("Items:")
for i in Path("../OS").iterdir():
    print(i.name)

# 10
print("*.py:", list(Path("../OS").glob("*.py")))

# 11
print("Recursive *.py:")
for i in Path("../OS").rglob("*.py"):
    print(i)

# 12
p = Path("folder/example.txt")
print("suffix:", p.suffix)
print("stem:", p.stem)
print("name:", p.name)

# 13
print("joinpath:", Path("data").joinpath("notes.txt"))

# 14
print("parent:", p.parent)

# 15
print("parts:", p.parts)

# 16
p = Path("../OS")
files = 0
dirs = 0
for i in p.iterdir():
    if i.is_file():
        files += 1
    elif i.is_dir():
        dirs += 1
print("Files:", files, "| Dirs:", dirs)

# 17
for i in Path("../OS").glob("*.log"):
    i.unlink()
    print("Deleted .log:", i)

# 18
for i in Path("../OS").rglob("*.txt"):
    print("TXT path:", i.resolve())

# 19
backup = Path("backup")
backup.mkdir(exist_ok=True)
for i in Path("../OS").glob("*.txt"):
    data = i.read_text()
    (backup / i.name).write_text(data)
print("Backed up .txt files to backup/")

# 20
os.chdir("../OS")
print("Python files inside current dir:")
for i in Path("../OS").glob("*.py"):
    print(i.name)
