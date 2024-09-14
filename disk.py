class Disk():
    def __init__(self):
        self.blocks: list[str] = []

    def allocate(self, data: str):
        self.blocks.append(data)
        return len(self.blocks) - 1

    def remove(self, pointers: list):
        for pointer in reversed(pointers):
            self.blocks.pop(pointer)