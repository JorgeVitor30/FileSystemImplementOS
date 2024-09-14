import math
from datetime import datetime
from disk import Disk

BLOCK_SIZE = 4
DISK = Disk()

            
class INode():
    def __init__(self, name):
        self.name = name
        self.lenght = 0
        self.pointers: list[int] = []

class DirINode():
    def __init__(self, name):
        self.name = name
        self.lenght = 0
        self.inodes: list = []

class File():
    def __init__(self, name, owner) -> None:
        self.name = name
        self.owner = owner
        self.index_inode = INode(name)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.flg_open = False

    def open(self):
        self.flg_open = True

    def close(self):
        self.flg_open = False

    def write(self, data: str, disk: Disk):
        if not self.flg_open:
            return

        for i in range(0, len(data), BLOCK_SIZE):
            block = data[i: i + BLOCK_SIZE]
            block_index = disk.allocate(block)
            self.index_inode.pointers.append(block_index)

        self.index_inode.lenght += len(data)
        self.updated_at = datetime.now()

    def read(self, disk: Disk):
        if not self.flg_open:
            return
        
        strings = []
        
        for pointer in self.index_inode.pointers:
            strings.append(disk.blocks[pointer])
            
        data = ''.join(strings)

        return data

    def delete(self, disk: Disk):
        disk.remove(self.index_inode.pointers)
            
        self.index_inode.pointers = []



class Directory():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.flg_open = False
        self.index_inode = DirINode(name)

    def open(self):
        self.flg_open = True


    def close(self):
        self.flg_open = False


    def add_file(self, file: File):
        if not self.flg_open:
            return
        
        if file.index_inode in self.index_inode.inodes:
            return
            
        self.index_inode.inodes.append(file.index_inode)
    

    def add_dir(self, dir):
        if not self.flg_open:
            return
        
        if dir.index_inode in self.index_inode.inodes:
            return
        
        self.index_inode.inodes.append(dir.index_inode)
    

    def remove_file(self, file):
        if not self.flg_open:
            return
        
        if file.index_inode not in self.index_inode.inodes:
            return
        
        file.delete(DISK)

        self.index_inode.inodes.remove(file.index_inode)
    

    def remove_dir(self, dir, disk: Disk):
        
        for inode in dir.index_inode.inodes:
            if isinstance(inode, INode):
                disk.remove(inode.pointers)
            else:
                dir.remove_dir(inode, disk)
        self.index_inode.inodes.remove(dir.index_inode)
        dir.__self_destruct()


    def move_file(self, file: File, dir):
        
        dir.index_inode.inodes.append(file.index_inode)  
        self.index_inode.inodes.remove(file.index_inode)


    def list(self):
        if not self.flg_open:
            return
        
        for i in self.index_inode.inodes:
            print(i.name, end = ' ')

    def __self_destruct(self):
        self.close()
        del self
