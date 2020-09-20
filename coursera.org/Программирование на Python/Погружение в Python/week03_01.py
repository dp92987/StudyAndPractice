class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read(self):
        try:
            with open(self.file_path) as f:
                return f.read()
        except FileNotFoundError:
            return ''

a = FileReader('week04_01.py')
print(a.read())
