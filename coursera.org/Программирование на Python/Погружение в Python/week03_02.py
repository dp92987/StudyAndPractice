import os
import csv


class CarBase:
    required = []

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate_input(brand)
        self.photo_file_name = self.validate_photo_ext(photo_file_name)
        self.carrying = float(carrying)

    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)

    @staticmethod
    def validate_input(data):
        if data:
            return data
        else:
            raise ValueError

    @staticmethod
    def validate_photo_ext(photo_file_name):
        file_name, file_ext = photo_file_name.split('.')
        if file_ext not in ('jpg', 'jpeg', 'png', 'gif') or not file_name:
            raise ValueError
        else:
            return photo_file_name

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    car_type = 'car'
    required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(self.validate_input(passenger_seats_count))


class Truck(CarBase):
    car_type = 'truck'
    required = ['brand', 'photo_file_name', 'carrying', 'body_whl']

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = self.parse_whl(body_whl)

    @staticmethod
    def parse_whl(body_whl):
        try:
            length, width, height = (float(c) for c in body_whl.split('x', 2))
        except ValueError:
            length, width, height = 0.0, 0.0, 0.0
        return length, width, height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    required = ['brand', 'photo_file_name', 'carrying', 'extra']

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = self.validate_input(extra)


def get_car_list(file_path):
    car_types = {'car': Car, 'truck': Truck, 'spec_machine': SpecMachine}
    car_list = []

    with open(file_path) as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            try:
                car_class = car_types[row['car_type']]
                car_list.append(car_class.create_from_dict(row))
            except (KeyError, ValueError):
                pass
    return car_list


if __name__ == '__main__':
    print(get_car_list('coursera_week3_cars.csv'))
