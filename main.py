from classes import *
from disk import *


file1 = File('FILE1', 'levy')
file1.open()
file1.write("TEXTO COM PALAVRAS", DISK)
file1.close()

file2 = File('file2', 'jorge')
file2.open()
file2.write("TEXTO SEM SENTIDO", DISK)
file2.close()

file1.open()
file1.write(" TEXTO 2 DO FILE1", DISK)
file1.close()

file1.open()
file1.read(DISK)



#### DIRETORIO ####

dir = Directory("PASTA", "Levy")
dir.open()

dir2 = Directory("PASTA2", "Jorge")
dir2.open()

dir.add_file(file1)
dir.add_dir(dir2)

dir.list()

dir.move_file(file1, dir2)

dir2.list()

dir.list()

dir.remove_dir(dir2, DISK)