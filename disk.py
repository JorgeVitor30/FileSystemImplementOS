class Disk:
    def __init__(self):
        self.blocks: list[str] = []
    

    def allocate(self, data: str):
        self.blocks.append(data)
        return len(self.blocks) - 1

    def remove(self, pointers: list[int]):
        for pointer in reversed(pointers):
            if 0 <= pointer < len(self.blocks):
                self.blocks.pop(pointer)