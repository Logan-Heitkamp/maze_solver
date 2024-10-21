import tkinter as tk
from time import sleep

height = 30
length = 50

root = tk.Tk()

root.geometry('2000x1000')
root.configure(bg='Black')
root.title('Pathfinding Thing')

# Welcome message
text = tk.Label(root, text="Welcome!", font=('Arial', 20))
text.configure(bg='Black', fg="White")
text.pack(pady=40, padx=10)


class Btn(tk.Button):
    def __init__(self, r, c):
        self.row_value = r
        self.column_value = c
        self.value = -1
        self.path_value = -1

        super().__init__(button_frame, text='', compound=tk.CENTER, width=1, height=1, bg='White',
                         command=self.click)

        self.cords = (r, c)
        self.on_path = False
        self.clicked = False

    def clear(self):
        self.value = -1
        self.color('White')
        self.path_value = -1
        self.on_path = False
        self.clicked = False

    def reset(self):
        self.path_value = -1
        self.on_path = False
        self.clicked = False

        if self.get_color() == 'Light Green':
            self.value = 1

        elif self.get_color() == 'Red':
            self.value = 2

        elif self.get_color() in ['Orange', 'Yellow']:
            self.value = -1
            self.color('White')

    def set_path_value(self, v):
        self.path_value = v

    def set_value(self, v):
        self.value = v

    def set_on_path(self):
        self.on_path = True

    def set_off_path(self):
        self.on_path = False

    def color(self, color):
        super().config(bg=color)

    def get_color(self):
        return super().cget('bg')

    def get_value(self):
        return self.value

    def get_path_value(self):
        return self.path_value

    def get_on_path(self):
        return self.on_path

    def click(self):
        num = player_main.get_btn()
        if self.get_color() == 'White':
            if num == 3:
                self.color('Grey')
                self.value = 3
            elif num == 2:
                self.color('Red')
                self.value = 2
                self.on_path = True
            elif num == 1:
                self.color('Light Green')
                self.value = 1
        else:
            self.color('White')
            self.value = -1

    # expands the searching algorithm
    def expand(self, pv, btnl):
        row = self.row_value
        column = self.column_value
        self.set_value(4)
        north_cords = (row - 1, column)
        east_cords = (row, column + 1)
        south_cords = (row + 1, column)
        west_cords = (row, column - 1)

        btn_n = Btn(-1, -1)
        btn_e = Btn(-1, -1)
        btn_s = Btn(-1, -1)
        btn_w = Btn(-1, -1)

        # finding surrounding buttons
        for button in btnl:
            if button.cords == north_cords:
                btn_n = button

            if button.cords == east_cords:
                btn_e = button

            if button.cords == south_cords:
                btn_s = button

            if button.cords == west_cords:
                btn_w = button

        # get values of surrounding spaces
        if north_cords[0] >= 0:
            value_north = btn_n.value
        else:
            value_north = 3

        if east_cords[1] < 50:
            value_east = btn_e.value
        else:
            value_east = 3

        if south_cords[0] < 30:
            value_south = btn_s.value
        else:
            value_south = 3

        if west_cords[0] >= 0:
            value_west = btn_w.value
        else:
            value_west = 3

        # expand to surrounding tiles
        if value_north == 2:
            btn_n.set_path_value(pv + 1)
            btn_n.set_on_path()
            print('foundn')
            return False
        elif value_north == -1:
            btn_n.color('Yellow')
            btn_n.set_path_value(pv + 1)

        if value_east == 2:
            btn_e.set_path_value(pv + 1)
            btn_e.set_on_path()
            print('founde')
            return False
        elif value_east == -1:
            btn_e.color('Yellow')
            btn_e.set_path_value(pv + 1)

        if value_south == 2:
            btn_s.set_path_value(pv + 1)
            btn_s.set_on_path()
            print('founds')
            return False
        elif value_south == -1:
            btn_s.color('Yellow')
            btn_s.set_path_value(pv + 1)

        if value_west == 2:
            btn_w.set_path_value(pv + 1)
            btn_w.set_on_path()
            print('foundw')
            return False
        elif value_west == -1:
            btn_w.color('Yellow')
            btn_w.set_path_value(pv + 1)

        # returns true if end is not found
        return True

    def find_path(self, pv, btnl):
        row = self.row_value
        column = self.column_value
        self.set_value(4)
        north_cords = (row - 1, column)
        east_cords = (row, column + 1)
        south_cords = (row + 1, column)
        west_cords = (row, column - 1)

        btn_n = Btn(-1, -1)
        btn_e = Btn(-1, -1)
        btn_s = Btn(-1, -1)
        btn_w = Btn(-1, -1)

        # finding surrounding buttons
        for button in btnl:
            if button.cords == north_cords:
                btn_n = button

            if button.cords == east_cords:
                btn_e = button

            if button.cords == south_cords:
                btn_s = button

            if button.cords == west_cords:
                btn_w = button

        # get path values of surrounding spaces
        if north_cords[0] >= 0:
            value_north = btn_n.path_value
        else:
            value_north = -1

        if east_cords[1] < 50:
            value_east = btn_e.path_value
        else:
            value_east = -1

        if south_cords[0] < 30:
            value_south = btn_s.path_value
        else:
            value_south = -1

        if west_cords[0] >= 0:
            value_west = btn_w.path_value
        else:
            value_west = -1

        # expand path back to start
        if value_north == pv - 1 and value_north != 0:
            btn_n.color('Orange')
            btn_n.set_on_path()
            return True
        elif value_north == 0:
            print('found2')
            return False

        if value_east == pv - 1 and value_east != 0:
            btn_e.color('Orange')
            btn_e.set_on_path()
            return True
        elif value_east == 0:
            print('found2')
            return False

        if value_south == pv - 1 and value_south != 0:
            btn_s.color('Orange')
            btn_s.set_on_path()
            return True
        elif value_south == 0:
            print('found2')
            return False

        if value_west == pv - 1 and value_west != 0:
            btn_w.color('Orange')
            btn_w.set_on_path()
            return True
        elif value_west == 0:
            print('found2')
            return False

        # returns true if start is not found
        return True


# class for the option buttons
class Obtn(tk.Button):

    def __init__(self, text_):
        super().__init__(option_frame, text=text_, compound=tk.CENTER, width=1, height=1, bg='White',
                         font=('Arial', 15), command=lambda: self.click(self.cget('text')))

    def select(self, s):
        if s:
            super().config(bg='Blue', fg='White')
        else:
            super().config(bg='White', fg='Black')

    def click(self, button):
        player_main.click(button)

        for obtn_ in obtn_list:
            obtn_.select(False)
        self.select(True)


def clear():
    for button in button_list:
        button.clear()


def reset():
    for button in button_list:
        button.reset()


def save():

    x = ''

    for button in button_list:
        if button.get_color() == 'Light Green':
            x += '1 '

        elif button.get_color() == 'Red':
            x += '2 '

        elif button.get_color() == 'Grey':
            x += '0 '

        else:
            x += '-1 '

    print(x)

    with open('Save_file.txt', 'w') as f:
        f.write(x)


def load():

    with open('Save_file.txt', 'r') as f:
        y = f.read()

    value = ''
    values = []

    for char in y:
        if char != ' ':
            value += char
        else:
            values.append(int(value))
            value = ''

    print(values)

    for idx, button in enumerate(button_list):
        button.path_value = -1
        button.on_path = False
        button.clicked = False

        if values[idx] == 0:
            button.value = 0
            button.color('Grey')

        elif values[idx] == 1:
            button.value = 1
            button.color('Light Green')

        elif values[idx] == 2:
            button.value = 2
            button.color('Red')

        elif values[idx] == -1 or button.get_color() in ['Orange', 'Yellow']:
            button.value = -1
            button.color('White')


class Player:
    def __init__(self):
        self.button_selected = -1

    def click(self, button):

        if button == 'Starting Block':
            self.button_selected = 1
        if button == 'Ending Block':
            self.button_selected = 2
        if button == 'Wall':
            self.button_selected = 3
        if button == 'Begin Simulation':
            self.button_selected = -1
            run(button_list)
        if button == 'Clear':
            self.button_selected = 4
            clear()
        if button == 'Reset':
            self.button_selected = 5
            reset()
        if button == 'Save':
            self.button_selected = 6
            save()
        if button == 'Load':
            self.button_selected = 7
            load()

    def get_btn(self):
        return self.button_selected


# tool selector
option_list = ['Starting Block', 'Ending Block', 'Wall', 'Begin Simulation', 'Reset', 'Clear', 'Save', 'Load']

option_frame = tk.Frame(root)
option_frame.rowconfigure(0, weight=1)
for i in range(len(option_list)):
    option_frame.columnconfigure(i, weight=1)

obtn_list = []
for option in option_list:
    obtn_list.append(Obtn(option))
for i, obtn in enumerate(obtn_list):
    obtn.grid(row=0, column=i, sticky='NESW')


def get_cords(num):
    x = num // length
    y = num % length
    ret = (x, y)
    return ret


# setting up the frame for the buttons
button_frame = tk.Frame(root)
for i in range(0, 50):
    button_frame.columnconfigure(i, weight=1)
for j in range(0, 30):
    button_frame.rowconfigure(j, weight=1)

# creating the buttons
button_list = {}
button_list_ = []
for grid_height in range(height):
    for grid_length in range(length):
        button_list_.append(Btn(grid_height, grid_length))

for i, b in enumerate(button_list_):
    button_list.update({b: [i, get_cords(i)]})

# assigning buttons to button_frame
for btn, cords in button_list.items():
    btn.grid(row=cords[1][0], column=cords[1][1], sticky='NESW')

# creating the player
player_main = Player()


# Run the simulation
def run(btnl):
    for button in btnl:
        if button.value == 1:
            button.set_path_value(0)

    current_path_value = 0
    true_loop = True
    loop = True
    while True:
        for button in btnl:
            if button.get_path_value() == current_path_value:
                loop = button.expand(current_path_value, btnl)
            if not loop:
                true_loop = False
            else:
                root.update()
        if not true_loop:
            current_path_value += 1
            break
        sleep(0.025)
        current_path_value += 1

    true_loop = True
    loop = True
    while True:
        for button in btnl:
            if button.get_path_value() == current_path_value and button.get_on_path():
                loop = button.find_path(current_path_value, btnl)
            if not loop:
                true_loop = False
            else:
                root.update()
        if not true_loop:
            break
        sleep(0.005)
        current_path_value -= 1


# packing frames
option_frame.pack(fill='x', pady=10)
button_frame.pack(fill='both')

# mainloop... duh...
root.mainloop()
