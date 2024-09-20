class Device:
    def turn_on(self):
        pass 


class TV(Device):
    def turn_on(self):
        return "TV is now on"
    
class Fan(Device):
    def turn_on(self):
        return "Fam is now spinning"
    
class Light(Device):
    def turn_on(self):
        return "Light is now on"
    
# function that uses polymorphism
def activate_device(device):
    print(device.turn_on())

tv = TV()
fan = Fan()
light = Light()

activate_device(tv)
activate_device(fan)
activate_device(light)

