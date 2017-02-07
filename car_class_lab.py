class Car(object):
    def __init__ (self, name, model):
        self.name = name
        self.model = model

    def speed(self, speed = 0):
        self.speed = speed
        return self.speed
    
    def drive(self, x):
        self.speed += x
        return self.speed

    def num_of_doors()
    if self.name == 'Porshe' or self.name == 'Koenigsegg':
        num_of_doors = 2
        return num_of_doors
    else:
        num_of_doors = 4
        return num_of_doors
    
    def num_of_wheels()
    if self.model == 'Trailer':
        num_of_wheels = 8
        return num_of_wheels
    else:
        num_of_wheels = 4
        return num_of_doors

if __name__ = '__main__':
    porshe = Car('Porshe', '911 Turbo')
    porshe.num_of_doors
    porshe.num_of_wheels
    porshe.drive(7).speed
    
