class Desk:
    def __init__(self, color):
        self.color = color
        print("I'm made!")

    def re_color(self, new_color):
        self.color = new_color

d = Desk("Blue")
d.re_color('red')
print(d.color)