class Boiler:
    def __init__(self, current_temp):
        self.current_temp = current_temp
        self.target_temp = None
        self.heating = False

    def set_target_temperature(self, temp):
        if 15 <= temp <= 75:
            self.target_temp = temp
            print(f"Target temperature set to {temp}°C")
            self.control_heating()
        else:
            print("Temperature must be between 15 and 75 degrees Celsius.")

    def control_heating(self):
        if self.target_temp is None:
            print("Target temperature not set.")
            return

        if self.current_temp < self.target_temp:
            self.heating = True
            print("Heating is ON.")
            self.heat_water()
        else:
            self.heating = False
            print("Heating is OFF. Water is already at or above the target temperature.")

    def heat_water(self):
        while self.heating and self.current_temp < self.target_temp:
            self.current_temp += 1
            print(f"Current temperature: {self.current_temp}°C")
            if self.current_temp >= self.target_temp:
                self.heating = False
                print("Target temperature reached. Heating is OFF.")

# Use case
input = int(input("Set temperature: "))
boiler = Boiler(current_temp=26)  # Current tempereture is 20°C
boiler.set_target_temperature(input)  # Targer temperature is 30°C
