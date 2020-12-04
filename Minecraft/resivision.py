from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color= color.white,
            texture = 'white_cube',
            rotation=Vec3(45,45,45)
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            model="cube",
            parent= scene,
            texture="brick",
            color= color.blue,
            highlight_color=color.red,
            pressed_color=color.lime
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                print("Button pressed")

def update():
    if held_keys['a']:
        test_square.x -= 4* time.dt

app = Ursina()

test_square = Entity(model = 'quad', color = color.pink, scale = (1,4), position = (5,4))
sans = Entity(model = 'quad', texture = 'assets/sans.png')

test_cube = Test_button()

app.run()from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color= color.white,
            texture = 'white_cube',
            rotation=Vec3(45,45,45)
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            model="cube",
            parent= scene,
            texture="brick",
            color= color.blue,
            highlight_color=color.red,
            pressed_color=color.lime
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                print("Button pressed")

def update():
    if held_keys['a']:
        test_square.x -= 4* time.dt

app = Ursina()

test_square = Entity(model = 'quad', color = color.pink, scale = (1,4), position = (5,4))
sans = Entity(model = 'quad', texture = 'assets/sans.png')

test_cube = Test_button()

app.run()