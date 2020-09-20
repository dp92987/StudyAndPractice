import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def __add__(self, other):
        new_file = type(self)(tempfile.NamedTemporaryFile().name)
        new_file.write('{0}{1}'.format(self.read(), other.read()))
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            f.seek(self.current_position)
            data = f.readline()
            if not data:
                self.current_position = 0
                raise StopIteration
            else:
                self.current_position = f.tell()
                return data

    def __str__(self):
        return self.path

    def read(self):
        with open(self.path) as f:
            return f.read()

    def write(self, data):
        with open(self.path, 'w') as f:
            f.write(data)
        return len(data)


if __name__ == '__main__':
    file1 = File(os.path.join(tempfile.gettempdir(), 'test1.txt'))
    file1.write('kek')

    file2 = File(os.path.join(tempfile.gettempdir(), 'test2.txt'))
    file2.write('lol')

    file3 = file1 + file2
    print(file3, file3.read())

    file = File('coursera_week3_cars.csv')
    for line in file:
        print(line)
