class Dragons:
    def __init__(self, color, power, age):
        self.color = color
        self.power = power
        self.age = age


Nimo = Dragons('red', 'mind-reading', 4500)
Nahal = Dragons('blue', 'breathing underwater', 3000)

print('Nimo is a', Nimo.color, 'dragon, her magic power is', Nimo.power, 'and she is', f" {Nimo.age}-years-old. ")
print('Nahal is a', Nahal.color, 'dragon, her magic power is', Nahal.power, 'and she is', f"{Nahal.age}-years-old. ")


