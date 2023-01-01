class player:
    value = 0  # the position of the players

    def __init__(self, value):
        self.name = None
        self.value = value
        self.image = None
        self.p_x = 0
        self.p_y = 0

    def give_name(self, newname):
        self.name = newname

    def get_value(self, move_value):
        # the dictionary used to judge if players meet the snakes
        snakes = {34: 1, 25: 5, 47: 19, 65: 52, 87: 57, 91: 61, 99: 69}
        # the dictionary used to judge if players meet the ladders
        ladders = {3: 51, 6: 27, 20: 70, 36: 55, 63: 95, 68: 98}
        self.value += move_value
        if self.value in snakes:
            self.value = snakes.get(self.value, self.value)
        elif self.value in ladders:
            self.value = ladders.get(self.value, self.value)
        if self.value > 100:
            self.value -= move_value
        self.p_x = movement(self.value)[0]
        self.p_y = movement(self.value)[1]
        return self.p_x, self.p_y


def movement(a):
    address1 = \
        [[340, 760], [420, 760], [500, 760], [580, 760], [660, 760], [740, 760], [820, 760], [900, 760], [980, 760], [1060, 760],
         [1140, 760],
         [420, 680], [500, 680], [580, 680], [660, 680], [740, 680], [820, 680], [900, 680], [980, 680], [1060, 680],
         [1140, 680],
         [420, 600], [500, 600], [580, 600], [660, 600], [740, 600], [820, 600], [900, 600], [980, 600], [1060, 600],
         [1140, 600],
         [420, 520], [500, 520], [580, 520], [660, 520], [740, 520], [820, 520], [900, 520], [980, 520], [1060, 520],
         [1140, 520],
         [420, 440], [500, 440], [580, 440], [660, 440], [740, 440], [820, 440], [900, 440], [980, 440], [1060, 440],
         [1140, 440],
         [420, 360], [500, 360], [580, 360], [660, 360], [740, 360], [820, 360], [900, 360], [980, 360], [1060, 360],
         [1140, 360],
         [420, 280], [500, 280], [580, 280], [660, 280], [740, 280], [820, 280], [900, 280], [980, 280], [1060, 280],
         [1140, 280],
         [420, 200], [500, 200], [580, 200], [660, 200], [740, 200], [820, 200], [900, 200], [980, 200], [1060, 200],
         [1140, 200],
         [420, 120], [500, 120], [580, 120], [660, 120], [740, 120], [820, 120], [900, 120], [980, 120], [1060, 120],
         [1140, 120],
         [420, 40], [500, 40], [580, 40], [660, 40], [740, 40], [820, 40], [900, 40], [980, 40], [1060, 40], [1140, 40]]
    address2 = address1[a]
    x = address2[0]
    y = address2[1]
    return x, y

