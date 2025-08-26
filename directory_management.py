from pathlib import Path
class Directory:
    def __init__(self, abs_dir: Path):
        self._abs_dir = abs_dir

    def back(self):
        self._abs_dir = self._abs_dir.parent
        return self._abs_dir
    def add(self, direc: str):
        self._abs_dir = self._abs_dir / direc

    def __repr__(self):
        return str(self._abs_dir)
# def change(*p):
#     print(p)
# change(*[1,2,3,4])
# print(*("aaaa")[1:])