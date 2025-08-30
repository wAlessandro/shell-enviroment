from pathlib import Path
class Directory:
    def __init__(self, abs_dir: Path):
        self._abs_dir = abs_dir
    @property
    def get(self):
        return self._abs_dir
    
    def back(self):
        self._abs_dir = self._abs_dir.parent
        return self._abs_dir
    def add(self, direc: str):
        self._abs_dir = self._abs_dir / direc
    