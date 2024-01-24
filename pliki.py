# praca z pliki

# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
fh = open("test.txt", "w")
fh.write("Radek\n")
fh.close()
# context manager
with open("test.log", "w", encoding='utf-8') as f:
    f.write("Powitanie\n")
    f.write("Kolejne\n")
    f.write("Jeszcze jedno\n")
# f.write('Test')  # ValueError: I/O operation on closed file.

# with open("test.log", "x") as f:  # FileExistsError: [Errno 17] File exists: 'test.log'
#     f.write("Test")
# with open("test2.log", "x") as f:  # FileExistsError: [Errno 17] File exists: 'test.log'
#     f.write("Test")

with open("test.log", "a", encoding='utf-8') as fh:
    fh.write("Dodane\n")
    fh.write("Dodane\n")
    fh.write("Dodane\n")
    fh.write("Dodane\n")
    fh.write("Dodane\n")
    fh.write("Doącńśdane\n")

with  open("test.log", "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
