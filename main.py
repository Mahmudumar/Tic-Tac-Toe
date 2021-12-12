
"""
Features include:.

1. Allow players to input their names to play multiplayer game
2. Undoing is possible but only once.
3. TODO: Setting of score limit for winner to be declared
        after the score has been reached.
4. TODO: Settings window available for setting of colors to
   suite the players likes (default is red for x and blue for o).
5. You can continue from where you stopped if you click the skip button
    or if you enter names that match the names in the last game.


Resources/Dependencies:
    1. map.json File for loading and dumping the whole game area texts.
    2. config.json File for loading and setting names,
     scores and checking stats
    3. settings.json File for settings colors for appearance of layout
    4. static.json File that holds info on the app: Version, language, etc...


NOTE: The Application is dependent on ALL these json files
so deleting or modifying them incorrectly will damage the app
"""

# Author: Mahmud Ahmad Umar from Maflah studio Dev

# Visit our page and follow us at
# https://www.facebook.com/maflahdev/

# This source code can be redistributed,
# studied and modified in any way.

# It was created in the hopes that it would be useful to the
# community

# -----------------------------------------------------------------
# I really like using classes in python because they are a very
# good way to organize things.

# Basically OOP is the best if you want your code to look neat.
# ---------

# if you want to add features of your own, Ensure
# to describe te feature in the docstring above^
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# Honestly i have no idea what i am doing exactly,
# i am learning new ways to do things.

# I came up with some of the ways i used to code here BY MISTAKE
# (hahaha,:D).
# Ok let's get to work
# ------------------------------------------------------------


# X and O game made with the built-in tkinter GUI:
# Features included in doc string above ^

import json  # For settings and object storage
import os  # For accessing files on hard drive
import tkinter as tk  # for GUI
import tkinter.messagebox as msgbox  # GUI For displaying messages
from tkinter.constants import BOTH, END
from typing import Any

# Personal imports (other python files created by me)
# NOTE These python files should be on the same folder as
# this one as it will crash if they are missing or corrupt
import defaults


# NOTE: json stands for JavaScipt Object Notation
# and it is used for storing and getting
#  data like settings, configurations, ...


# double forward slash added so that filename can be added without slashes
# as in lines NOTE and NOTE
# Directory for all json and other files
bin_dir = 'C:\\Users\\LENOVO\\Programming\\PYTHON\\XandO(new)\\.bin\\'

# just for reference
GAINSBRO = '#DCDCDC'
LIGHTGREY = '#A9A9A9'
CFBLUE = '#6495ED'
# ---------------------


def check_jsons(files='all'):
    """Check whether configuration,
        settings and map files have been corrupted
        and fix them"""
    if files.__contains__('all'):
        if os.path.isfile(f'{bin_dir}config.json'):
            with open(f'{bin_dir}config.json', 'r') as config_:
                intact = bool(config_.readlines(1))
                if intact:
                    print('config intact')
                else:
                    print('fixing config...')
                    print(defaults.reset('config'))
        else:
            with open(f'{bin_dir}config.json', 'x')as _config:
                print('fixing config...')
                print(defaults.reset('config'))

        if os.path.isfile(f'{bin_dir}settings.json'):
            with open(f'{bin_dir}settings.json', 'r') as config_:
                intact = bool(config_.readlines(1))
                if intact:
                    print('settings intact')
                else:
                    print('fixing settings...')
                    print(defaults.reset('settings'))
                    return intact
        else:
            with open(f'{bin_dir}settings.json', 'x')as _config:
                print('fixing settings...')
                print(defaults.reset('settings'))

        if os.path.isfile(f'{bin_dir}map.json'):
            with open(f'{bin_dir}map.json', 'r') as config_:
                intact = bool(config_.readlines(1))
                if intact:
                    print('map intact')
                else:
                    print('fixing map...')
                    print(defaults.reset('map'))
                    return intact
        else:
            print('Map.json doesn\'t exist')
            print('fixing map...')
            with open(f'{bin_dir}map.json', 'x')as _config:

                print(defaults.reset('map'))


# checks for corrupt or missing
# json files and fixies
check_jsons()

# global variables (defaults)
# when file is run or app is opened,
# these variables are picked from the config.json
# json file
with open(f'{bin_dir}config.json', 'r') as _turn:
    # True means X's turn False means O's turn
    turn = bool(dict(json.load(_turn))['turn'])
with open(f'{bin_dir}config.json', 'r') as _undo_x:
    # if player clicks the undo button, undo is set to 1
    xundo_counter = int(dict(json.load(_undo_x))['xundo_counter'])
with open(f'{bin_dir}config.json', 'r') as _undo_o:
    oundo_counter = int(dict(json.load(_undo_o))['oundo_counter'])
with open(f'{bin_dir}config.json', 'r') as _counter:
    # counter for number of clicks made or
    # counter for number of buttons that have an x or o
    counter = int(dict(json.load(_counter))['counter'])


# TODO: Settings window
# XXX: NOT FINISHED. Might crash the app if enabled
# class Settings:
    #    """TODO: settings file for changing of colors."""
    #
    #    widget = {}
    #
    #    def _read_settings(self, event=None):
    #        with open(f'{bin_dir}settings.json', 'r') as _read_file:
    #            self.settings = dict(json.load(_read_file))
    #        self.x_color = self.settings['Theme']['xColor']
    #        self.o_color = self.settings['Theme']['oColor']
    #        self.bck_color = self.settings['Theme']['backframe']['Background']
    #        self.lblfrm_color = self.settings['Theme'
    #                                          ]['labelframe']['Background']
    #        self.lbl_bg = self.settings['Theme']['label']['Background']
    #        self.lbl_fg = self.settings['Theme']['label']['Foreground']
    #        self.bt_bg = self.settings['Theme']["button"]["Background"]
    #        self.bt_fg = self.settings['Theme']["button"]["Foreground"]
    #        self.g_bg = self.settings['Theme']['gamearea']['Background']
    #
    #    def _upload_settings(self, **kw):
    #        with open(f"{bin_dir}settings.json", 'w') as _update_file:
    #            self.settings.update(**kw)
    #            json.dump(self.settings, _update_file, indent=4)
    #
    #    def _read_config(self, event=None):
    #        with open(f'{bin_dir}config.json', 'r') as _read_file:
    #            self.config = dict(json.load(_read_file))
    #        # configurations
    #        self.x_score = self.config['Score']['X']
    #        self.o_score = self.config['Score']['O']
    #
    #        self.scores = [self.x_score, self.o_score]
    #
    #        self.name_x = self.config['Name']['X']
    #        self.name_o = self.config['Name']['O']
    #
    #        self.names = [self.name_x, self.name_o]
    #
    #        # --------------------------------------------------
    #
    #    def _upload_config(self, **kw):
    #        with open(f"{bin_dir}config.json", 'w') as _update_file:
    #            self._temp_config.update(**kw)
    #            json.dump(self._temp_config, _update_file, indent=4)
    #
    #    def __init__(self, event=None) -> None:
    #        """Initialize the Settings window and call it with show()."""
    #        self.title = 'User Preferences'
    #
    #        self._read_settings()
    #        self._read_config()
    #
    #        # define mandatory widgets
    #        self.root = tk.Toplevel()
    #        self.root.wm_title(self.title)
    #
    #        self.backframe = tk.Frame(self.root, bg=self.bck_color)
    #        self.backframe.pack(expand=True, fill=BOTH)
    #
    #        # call widgets
    #        self.colors_area()
    #        self.bottom_area()
    #
    #        # show the window
    #        self.show()
    #
    #    def back_frame(self, event=None):
    #        """Call the back frame button and label."""
    #        self.bckfrm_area = tk.Frame(self.col_area)
    #        self.bckfrm_area.grid()
    #
    #        self.bckframe_lbl = tk.Label(
    #            self.bckfrm_area, fg=self.lbl_fg,
    #            bg=self.lbl_bg, text='BackFrame Color :',
    #            name='bckfrm_lbl')
    #        self.bckframe_lbl.pack(side='left')
    #
    #        self.bckframe_bt = tk.Button(
    #            self.bckfrm_area, width=20, bg=self.bck_color,
    #            name='bckfrm_bt', command=lambda:
    #            self.choose_col('backframe', False))
    #        self.bckframe_bt.pack(side='left')
    #
    #        self.widget.update(backfrm_lbl=self.bckframe_lbl)
    #        self.widget.update(backframe_bt=self.bckframe_lbl)
    #
    #    def label(self, event=None):
    #        # frame
    #        self.lbl_bg_area = tk.Frame(self.col_area)
    #        self.lbl_bg_area.grid()
    #
    #        # lABEL and bt
    #        self.lbl_bg_lbl = tk.Label(
    #            self.lbl_bg_area, fg=self.lbl_fg, bg=self.lbl_bg,
    #            text='Label Background :',
    #            name='lbl_bg')
    #        self.lbl_bg_lbl.pack(side='left')
    #
    #        # background bt
    #        self.lbl_bg_bt = tk.Button(
    #            self.lbl_bg_area, width=20, bg=self.lbl_bg,
    #            name='lbl_bt', command=lambda:
    #            self.choose_col('label', False))
    #        self.lbl_bg_bt.pack(side='left')
    #
    #        # Frame
    #        self.lbl_fg_area = tk.Frame(self.col_area)
    #        self.lbl_fg_area.grid()
    #
    #        # Label and button
    #        self.lbl_fg_lbl = tk.Label(
    #            self.lbl_fg_area, bg=self.lbl_bg, fg=self.lbl_fg,
    #            text='X Foreground :')
    #        self.lbl_fg_lbl.pack(side='left')
    #
    #        self.lbl_fg_bt = tk.Button(
    #            self.lbl_fg_area, width=20, bg=self.lbl_fg,
    #            command=lambda:
    #            self.choose_col('label', True)
    #        )
    #        self.lbl_fg_bt.pack(side='left')
    #
    #        self.widget.update(lbl_bg_bt=self.lbl_bg_bt)
    #        self.widget.update(lbl_fg_bt=self.lbl_fg_lbl)
    #        self.widget.update(lbl_fg_bt=self.lbl_bg_lbl)
    #        self.widget.update(lbl_bg=self.lbl_bg_bt)
    #
    #    def colors_area(self, event=None):
    #        self.col_area = tk.LabelFrame(
    #            self.backframe, text='Colors', bg=self.lblfrm_color)
    #        self.col_area.pack()
    #
    #        self.back_frame()
    #        self.label()
    #
    #    # TODO update when ok is pressed
    #
    #    def choose_col(self, widg: str, Foreground: bool, event=None):
    #        self._read_settings()
    #        color = col.askcolor()
    #        if Foreground:
    #            self.settings['Theme'][widg]['Foreground'] = color[1]
    #            self._upload_settings()
    #        elif not Foreground:
    #            self.settings['Theme'][widg]['Background'] = color[1]
    #            self._upload_settings()
    #
    #        elif Foreground is None:
    #            self.settings['Theme'][widg]['Background'] = color[1]
    #            self._upload_settings()
    #
    #        return color[1]
    #
    #    def bottom_area(self):
    #        self.btm_frame = tk.Frame(self.root)
    #        self.btm_frame.pack()
    #        self.ok_bt = ttk.Button(self.btm_frame, text='OK',
    #                                command=self.okay)
    #        self.ok_bt.pack()
    #
    #    def okay(self):
    #        # TODO
    #        for widg in self.widget:
    #            pass
    #        self.root.destroy()
    #
    #    def show(self, event=None):
    #        self.root.update()
    #        # self.root.wm_attributes('-toolwindow', True)
    #        self.root.wm_attributes('-top', True)
    #        self.root.mainloop()

class ChooseSide:
    """Change your names"""

    # choose side

    def _read_map(self, event=None):
        with open(f"{bin_dir}map.json", 'r') as _map_file:
            self._map = dict(json.load(_map_file))

    def _load_map(self, event=None):
        for b in self.bt_list:
            b['text'] = self._map[b.winfo_name()]

    def _update_map(self, b: tk.Button, player):
        """Used to update the map temporarily.
        Call the _update_to_map() function to
        upload the whole map to the map.json file
        """
        self._read_map()
        self.bt_name = b.winfo_name()
        self._temp_map[self.bt_name] = player

    def _update_to_map(self, **kw):
        """Dumps whole map into the map.json file"""
        with open(f"{bin_dir}map.json", 'w') as most_rcnt:
            json.dump(self._temp_map, most_rcnt, indent=4)
            return 'Done'

    def _read_settings(self, event=None):
        with open(f'{bin_dir}settings.json', 'r') as _read_file:
            self.settings = dict(json.load(_read_file))
        self.x_color = self.settings['Theme']['xColor']
        self.o_color = self.settings['Theme']['oColor']
        self.bck_color = self.settings['Theme']['backframe']['Background']
        self.lblfrm_color = self.settings['Theme'
                                          ]['labelframe']['Background']
        self.lbl_bg = self.settings['Theme']['label']['Background']
        self.bt_bg = self.settings['Theme']["button"]["Background"]
        self.bt_fg = self.settings['Theme']["button"]["Foreground"]
        self.g_bg = self.settings['Theme']['gamearea']['Background']
        self.g_fg = self.settings['Theme']['gamearea']['Foreground']
        self.bt_win_fg = self.g_fg

    def _upload_settings(self, **kw):
        with open(f"{bin_dir}settings.json", 'w') as _update_file:
            self.settings.update(**kw)
            self.settings['Theme']['xColor'] = self.x_color
            self.settings['Theme']['oColor'] = self.o_color
            self.settings['Theme']['backframe']['Background'] = self.bck_color
            self.settings['Theme'
                          ]['labelframe']['Background'] = self.lblfrm_color
            self.settings['Theme']['label']['Background']
            self.settings['Theme']["button"]["Background"]
            self.settings['Theme']["button"]["Foreground"]
            self.settings['Theme']['gamearea']['Background']
            self.settings['Theme']['gamearea']['Foreground']
            self.g_fg
            json.dump(self.settings, _update_file, indent=4)

    def _read_config(self, event=None):
        with open(f'{bin_dir}config.json', 'r') as _read_file:
            self.config = dict(json.load(_read_file))
        # configurations
        self.x_score = self.config['Score']['X']
        self.o_score = self.config['Score']['O']

        self.name_x = self.config['Name']['X']
        self.name_o = self.config['Name']['O']

        self.scores = [self.x_score, self.o_score]

        self.fullscreen = bool(self.config['fullscreen'])
        # --------------------------------------------------

    def _upload_config(self, **kw):
        with open(f"{bin_dir}config.json", 'w') as _update_file:
            self._temp_config.update(**kw)
            json.dump(self._temp_config, _update_file, indent=4)

    title = 'X and O [Configure]'
    message = 'Enter your names'

    def __init__(self):
        self.names_root = tk.Tk(className=" Tic Tac Toe (X and O)")
        self.names_root.wm_attributes('-top', True)
        self.names_root.wm_title(self.title)

        self._read_config()
        self._read_map()

        self._temp_config = self.config.copy()
        self._temp_map = self._map.copy()

        self.holder = tk.Frame(self.names_root)
        self.holder.pack()

        self.help_area()
        self.sides()
        self.entries()
        self.bottom_area()
        self.show()
        # holder for everything

    def show(self):
        self.names_root.geometry('550x320+390+200')
        self.names_root.mainloop()

    def help_area(self):
        # help
        self.helptab = tk.Frame(self.holder)
        self.helptab.pack()

        self.help = tk.Label(self.helptab, text=self.message,
                             font=('sans-serif', 30))
        self.help.pack()
        #

    def sides(self):
        self.sidesframe = tk.Frame(self.holder)
        self.sidesframe.pack(expand=1, fill='y')

        self.x_bt = tk.Button(self.sidesframe, relief='flat', text='X',
                              activebackground='red',
                              command=self.start_play_with_x,
                              activeforeground='white',
                              disabledforeground='red',
                              fg="red", width=5, height=1,
                              state='disabled',
                              font=('sans-serif', 20))

        self.o_bt = tk.Button(self.sidesframe, relief='flat', text='O',
                              activebackground='blue',
                              command=self.start_play_with_o,
                              activeforeground='white',
                              disabledforeground='blue',
                              fg="blue", width=5, height=1,
                              state='disabled',
                              font=('sans-serif', 20))
        self.o_bt.grid(column=1, row=1, padx=20)
        self.x_bt.grid(column=0, row=1, padx=20)

        self.x_bt.bind('O', self.start_play_with_o)
        self.x_bt.bind('X', self.start_play_with_x)

        # For choosing who plays against who

    def entries(self):
        self.playervar1 = tk.StringVar(self.names_root)
        self.playervar2 = tk.StringVar(self.names_root)

        self.nametab = tk.Frame(self.holder)
        self.nametab.pack(expand=1)

        self.whos_player1 = tk.Text(self.nametab, bg=LIGHTGREY, width=14,
                                    height=1, fg='red',
                                    font=('sans-serif', 20), relief='flat',
                                    selectbackground='red',
                                    selectforeground='white', name='p1')

        self.whos_player2 = tk.Text(self.nametab, bg=LIGHTGREY, width=14,
                                    height=1,
                                    font=('sans-serif', 20),
                                    relief='flat', fg='blue',
                                    selectbackground='blue',
                                    selectforeground='white', name='p2')

        self.whos_player1.pack(side='left', padx=20, pady=20, expand=1)
        self.whos_player2.pack(side='left', padx=20, pady=20, expand=1)

        self.names_root.bind('<Return>', self.advance)

    def bottom_area(self):
        # bar for buttons like continue...etc
        self.taskbar = tk.Frame(self.names_root)
        self.taskbar.pack(expand=1, pady=30)

        self.skip_bt = tk.Button(self.taskbar, text='Skip', font=(
            'sans-serif', 15), command=self.skip, bg='red', fg='white',
            name='skip')
        self.advance_bt = tk.Button(self.taskbar, fg='white', bg='#030',
                                    text='Continue', font=(
                                        'sans-serif', 15),
                                    command=self.advance, name='continue')

        self.advance_bt.pack(side='left', padx=30)
        self.skip_bt.pack(side='left', padx=30)

        self.advance_bt.bind('<Enter>', self.advance_hover)
        self.advance_bt.bind('<Leave>', self.advance_leave)

    def advance_hover(self, widget=None):
        self.advance_bt['fg'] = 'white'
        self.advance_bt['bg'] = '#090'
        self.advance_bt['relief'] = 'flat'

    def advance_leave(self, event=None):
        self.advance_bt['bg'] = '#030'
        self.advance_bt['fg'] = 'white'
        self.advance_bt['relief'] = 'groove'

    def skip(self):
        """Skip the names entry."""
        skip_bt_name = self.skip_bt.winfo_name()
        self.names_root.destroy()
        Layout(skipped=True)

    def get_names(self, event=None) -> str:
        self.name1 = self.whos_player1.get(1.0, END).capitalize().strip()
        self.name2 = self.whos_player2.get(1.0, END).capitalize().strip()

    def advance(self, event=None):
        self.get_names()
        self._temp_config['Name']['X'] = self.name1
        self._temp_config['Name']['O'] = self.name2
        self._upload_config()

        filled1 = bool(self.name1.strip())
        filled2 = bool(self.name2.strip())

        # if the box is filled then False else true
        if filled1 and filled2:
            self.start_play_with_x()

        elif not filled1 and filled2:
            self.whos_player1.focus()
            self.whos_player2.delete(1.0, END)
            self.whos_player2.insert(1.0, self.name2)

        elif filled1 and not filled2:
            self.whos_player2.focus()
            self.whos_player1.delete(1.0, END)
            self.whos_player1.insert(1.0, self.name1)

        elif not filled1 and not filled2:
            self.whos_player1.focus()

    def start_play_with_x(self):
        self._upload_config()
        advance_bt_name = self.advance_bt.winfo_name()
        self.names_root.destroy()
        Layout(skipped=False)

    def start_play_with_o(self):
        pass


class ChangeNames(ChooseSide):
    def __init__(self):
        super().__init__()
        self.advance_bt['command'] = self.update_names()

    def continue_game(self):
        self._temp_config["Name"]["X"] = self.name1
        self._temp_config["Name"]["O"] = self.name2
        self._upload_config()
        self.names_root.destroy()

    def update_names(self):
        self.get_names()
        filled1 = bool(self.name1.strip())
        filled2 = bool(self.name2.strip())

        # if the box is filled then False else true
        if filled1 and filled2:
            self.continue_game()

        elif not filled1 and filled2:
            self.whos_player1.focus()
            self.whos_player2.delete(1.0, END)
            self.whos_player2.insert(1.0, self.name2)

        elif filled1 and not filled2:
            self.whos_player2.focus()
            self.whos_player1.delete(1.0, END)
            self.whos_player1.insert(1.0, self.name1)

        elif not filled1 and not filled2:
            self.whos_player1.focus()


class Layout:
    """Layout of the game window."""
    # widgets = Dictionary to be passed as a parameter for Functions below
    widgets = {}
    labels = {}

    g_area_checker = []
    current_players = []  # max must be two

    def _read_settings(self, event=None):
        with open(f'{bin_dir}settings.json', 'r') as _read_file:
            self.settings = dict(json.load(_read_file))
        self.x_color = self.settings['Theme']['xColor']
        self.o_color = self.settings['Theme']['oColor']
        self.bck_color = self.settings['Theme']['backframe']['Background']
        self.lblfrm_color = self.settings['Theme'
                                          ]['labelframe']['Background']
        self.lbl_bg = self.settings['Theme']['label']['Background']
        self.bt_bg = self.settings['Theme']["button"]["Background"]
        self.bt_fg = self.settings['Theme']["button"]["Foreground"]
        self.g_bg = self.settings['Theme']['gamearea']['Background']
        self.g_fg = self.settings['Theme']['gamearea']['Foreground']
        self.bt_win_fg = self.g_fg

    def _upload_settings(self, **kw):
        with open(f"{bin_dir}settings.json", 'w') as _update_file:
            self.settings.update(**kw)
            self.settings['Theme']['xColor'] = self.x_color
            self.settings['Theme']['oColor'] = self.o_color
            self.settings['Theme']['backframe']['Background'] = self.bck_color
            self.settings['Theme'
                          ]['labelframe']['Background'] = self.lblfrm_color
            self.settings['Theme']['label']['Background']
            self.settings['Theme']["button"]["Background"]
            self.settings['Theme']["button"]["Foreground"]
            self.settings['Theme']['gamearea']['Background']
            self.settings['Theme']['gamearea']['Foreground']
            self.g_fg
            json.dump(self.settings, _update_file, indent=4)

    def _read_config(self, event=None):
        with open(f'{bin_dir}config.json', 'r') as _read_file:
            self.config = dict(json.load(_read_file))
        # configurations
        self.x_score = self.config['Score']['X']
        self.o_score = self.config['Score']['O']

        self.name_x = self.config['Name']['X']
        self.name_o = self.config['Name']['O']

        self.scores = [self.x_score, self.o_score]

        self.fullscreen = bool(self.config['fullscreen'])
        # --------------------------------------------------

    def _upload_config(self, **kw):
        with open(f"{bin_dir}config.json", 'w') as _update_file:
            self._temp_config.update(**kw)
            json.dump(self._temp_config, _update_file, indent=4)

    def _read_map(self, event=None):
        with open(f"{bin_dir}map.json", 'r') as _map_file:
            self._map = dict(json.load(_map_file))

    def _load_map(self, event=None):
        for b in self.bt_list:
            b['text'] = self._map[b.winfo_name()]

    def _update_map(self, b: tk.Button, player):
        """Used to update the map temporarily.
        Call the _update_to_map() function to
        upload the whole map to the map.json file
        """
        self._read_map()
        self.bt_name = b.winfo_name()
        self._temp_map[self.bt_name] = player

    def _update_to_map(self, **kw):
        """Dumps whole map into the map.json file"""
        with open(f"{bin_dir}map.json", 'w') as most_rcnt:
            json.dump(self._temp_map, most_rcnt, indent=4)
            return 'Done'

    # if name of x and o in the previous game
    # and names in the new game,
    # ask to load last game.
    def _update_last_gameof(self):
        self._temp_map["Gameof"]["X"] = self.name_x
        self._temp_map["Gameof"]["O"] = self.name_o
        self._update_to_map()

    def _check_g_area(self, event=None):
        self.g_area_checker.clear()
        self._read_map()
        for b in self.bt_list:
            for bt in self._map[b.winfo_name()]:
                self.g_area_checker.append(bool(bt.strip()))

    def _get_bool_map(self, event=None):
        return self.g_area_checker

    def __init__(self, **kw) -> None:
        """Initialize the tictactoe game and call it with .show()."""
        self.title = 'Tic Tac Toe (X and O)'
        self.kw = kw
        self.root = tk.Tk()
        self.root.wm_title(self.title)

        self._read_settings()
        self._read_config()
        self._read_map()

        if self.kw:
            if 'skipped' in self.kw:
                self.skipped = self.kw['skipped']

        # dictionary for modifying configurations,
        # settings and maps
        self._temp_config = self.config.copy()
        self._temp_settings = self.settings.copy()

        self._temp_map = self._map.copy()

        # Used as background for theme setting
        self.backframe = tk.Frame(self.root, bg=self.bck_color,
                                  name='backframe')
        self.backframe.pack(expand=1, fill=BOTH)
        # ---------------------------------------------

        # Arrange widgets-----------------------------
        self.menu()
        self.score_area()
        self.game_area()
        self.help_area()
        self._check_g_area()
        # --------------------------------------------

        self.root.wm_protocol('WM_DELETE_WINDOW', self._quit)
        self.shortcuts()

        # after asking to load or start new game
        # if loaded, check for winner
        # self.check_winner('')

        self.load_or_new()
        self.show()

    def shortcuts(self):
        self.root.bind("<Configure>", self.focus)
        self.root.bind('<Alt-F4>', self._quit)
        self.root.bind('<Shift-Alt-S>', self.setting_cmds)
        self.root.bind_all('<F11>', self.toggle_fullscreen)
        for button in self.bt_list:
            button.bind('<Button-3>', self.b_undo)

    def focus(self, event=None):
        self.root.focus_force()

    # Show the window------------
    def show(self, event=None):
        """
        Show the game window.

        This function should
        be called outside the
        '__init__' function.
        i.e After an instance
        of the class
        has been created

        EXAMPLE;\n

        game = Layout()\n
        game.show()
        .
        """
        self.state = self.root.wm_state(
            'normal') if not self.fullscreen else self.root.wm_state(
                'zoomed')
        self.helper.after(1500, self.hlp_cmds)
        self.root.mainloop()
    # -------------------------------

    # Widgets
    def menu(self, event=None):
        """Arrange menu items in the menubar."""
        self.menubar = tk.Menu(tearoff=False)
        self.menumenu = tk.Menu(tearoff=False)
        self.toolmenu = tk.Menu(tearoff=False)

        self.menumenu.add_command(
            label='Restart Round', command=lambda: self.menu_cmds(False))
        self.menumenu.add_command(
            label='Start Over', command=lambda: self.menu_cmds(True))
        self.menumenu.add_command(
            label='New Game', command=lambda: self.new_game(True)
        )
        self.menubar.add_cascade(menu=self.menumenu, label='Menu')
        self.menubar.add_cascade(menu=self.toolmenu, label='Tools')
        self.root.config(menu=self.menubar)

    def score_area(self, event=None):
        """Arrange players' names and scores."""
        # frame for players' scores and names
        self.s_area = tk.Frame(self.backframe, bg=f'white')
        self.s_area.pack(pady=30)
        # --------------------------------------------------

        # Frame for player1 (x) [name and score]
        self.x_info_area = tk.Frame(self.s_area)
        self.x_info_area.pack(side='left', padx=50)

        # Frame for player2 (o) [name and score]
        self.o_info_area = tk.Frame(self.s_area)
        self.o_info_area.pack(side='left', padx=50)

        self.x_label = tk.Label(self.x_info_area,
                                text=f"{self.name_x} (X): ",
                                font=('consolas', 30),
                                background='white',
                                foreground=self.x_color
                                )

        self.x_slabel = tk.Label(self.x_info_area,
                                 text=f'{self.x_score}',
                                 font=('consolas', 30),
                                 fg=self.x_color,
                                 bg='white')

        self.o_label = tk.Label(self.o_info_area,
                                text=f'{self.name_o} (O): ',
                                font=('consolas', 30),
                                background='white',
                                foreground=self.o_color
                                )

        self.o_slabel = tk.Label(self.o_info_area,
                                 text=f'{self.o_score}',
                                 font=('consolas', 30),
                                 fg=self.o_color,
                                 bg='white')

        self.x_label.pack(side='left')
        self.x_slabel.pack(side='left')

        self.o_label.pack(side='left')
        self.o_slabel.pack(side='left')

    def game_area(self, event=None):
        """Call the main game area."""
        self.g_area = tk.Frame(self.backframe, bg=self.g_bg)
        self.g_area.pack(pady=20)

        self.bt1 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt1),
                             name='bt1')
        self.bt2 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt2),
                             name='bt2')
        self.bt3 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt3),
                             name='bt3')
        self.bt4 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt4),
                             name='bt4')
        self.bt5 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt5),
                             name='bt5')
        self.bt6 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt6),
                             name='bt6')
        self.bt7 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt7),
                             name='bt7')
        self.bt8 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt8),
                             name='bt8')
        self.bt9 = tk.Button(self.g_area, bg=self.bt_bg,
                             fg=self.bt_fg, text=' ', font=('consolas', 50),
                             relief='flat', height=1, width=4,
                             command=lambda: self.bt_cmds(self.bt9),
                             name='bt9')
        self.bt_list = [
            self.bt1,
            self.bt2,
            self.bt3,
            self.bt4,
            self.bt5,
            self.bt6,
            self.bt7,
            self.bt8,
            self.bt9
        ]

        self.bt1.grid(row=1, column=1, padx=2, pady=2)
        self.bt2.grid(row=1, column=2, padx=2, pady=2)
        self.bt3.grid(row=1, column=3, padx=2, pady=2)

        self.bt4.grid(row=2, column=1, padx=2, pady=2)
        self.bt5.grid(row=2, column=2, padx=2, pady=2)
        self.bt6.grid(row=2, column=3, padx=2, pady=2)

        self.bt7.grid(row=3, column=1, padx=2, pady=2)
        self.bt8.grid(row=3, column=2, padx=2, pady=2)
        self.bt9.grid(row=3, column=3, padx=2, pady=2)

        self.widgets.update(bt_list=self.bt_list)

    def help_area(self, event=None):
        """Call the helper area."""
        self.helpframe = tk.Frame(self.backframe, bg='white')
        self.helpframe.pack(pady=20)

        # fg (modify)
        # text (modify)
        self.helper = tk.Label(
            self.helpframe, text=f'Welcome',
            font=('consolas', 30),
            bg='white',
            fg=self.x_color)

        self.widgets.update(helper=self.helper)

        self.helper.pack()

    # Commands to call functions
    def menu_cmds(self, all_=False):
        """Call reset commands for menu button."""
        self.reset(all_)

    def setting_cmds(self, event=None):
        """Call settings window."""
        ChangeNames()

    def bt_cmds(self, bt):
        """Call button commands."""
        self._b_clicked(bt)
        self._check_g_area()

    def hlp_cmds(self, event=None):
        """Animate the helper label at app startup."""
        self.animate(self.helper)

    def toggle_fullscreen(self, event=None):
        """Toggle between fullscreen and normal for the main window."""
        self._read_config()
        if not self.fullscreen:
            self.root.wm_state('zoomed')
            self.root.wm_overrideredirect(True)
            self._upload_config(fullscreen=True)
        elif self.fullscreen:
            self.root.wm_state('normal')
            self.root.wm_overrideredirect(False)
            self._upload_config(fullscreen=False)

        # Initialize window class

    # winning arrangement----------------------
    def _winstance(self, who):
        """Instances that must be true to win a round."""
        self.instance1 = [
            self.bt1['text'] == who,
            self.bt2['text'] == who,
            self.bt3['text'] == who
        ]
        self.instance2 = [
            self.bt4['text'] == who,
            self.bt5['text'] == who,
            self.bt6['text'] == who
        ]
        self.instance3 = [
            self.bt7['text'] == who,
            self.bt8['text'] == who,
            self.bt9['text'] == who
        ]
        self.instance4 = [
            self.bt1['text'] == who,
            self.bt4['text'] == who,
            self.bt7['text'] == who
        ]
        self.instance5 = [
            self.bt2['text'] == who,
            self.bt5['text'] == who,
            self.bt8['text'] == who
        ]
        self.instance6 = [
            self.bt3['text'] == who,
            self.bt6['text'] == who,
            self.bt9['text'] == who
        ]
        self.instance7 = [
            self.bt1['text'] == who,
            self.bt5['text'] == who,
            self.bt9['text'] == who
        ]
        self.instance8 = [
            self.bt7['text'] == who,
            self.bt5['text'] == who,
            self.bt3['text'] == who
        ]

    def _winarrange(self, event=None):
        """Buttons in Rows and columns (for winning)."""
        self.row1 = [
            self.bt1,
            self.bt2,
            self.bt3
        ]
        self.row2 = [
            self.bt4,
            self.bt5,
            self.bt6
        ]
        self.row3 = [
            self.bt7,
            self.bt8,
            self.bt9
        ]

        self.col1 = [
            self.bt1,
            self.bt4,
            self.bt7
        ]
        self.col2 = [
            self.bt2,
            self.bt5,
            self.bt8
        ]
        self.col3 = [
            self.bt3,
            self.bt6,
            self.bt9
        ]

        self.diag1 = [
            self.bt1,
            self.bt5,
            self.bt9
        ]
        self.diag2 = [
            self.bt3,
            self.bt5,
            self.bt7
        ]
    # ---------------------------------

    # FUNCTIONS------------------------------------
    def animate(self, label: tk.Label):
        """Change text after 1 second."""
        if turn is True:
            label['text'] = f"{self.name_x}'s turn"
            label['fg'] = self.x_color
        elif turn is False:
            label['text'] = f"{self.name_o}'s turn"
            label['fg'] = self.o_color

    def _b_clicked(self, bt: tk.Button, event=None):
        """bt=Button."""
        global turn, counter
        self.b = bt
        b_text = self.b['text'].strip()
        b_taken = bool(b_text)

        if b_text == '' and turn is True:
            self.b['text'] = 'X'
            turn = False
            counter += 1
            self._upload_config(turn=turn, counter=counter)

            self.helper['fg'] = self.o_color
            self.helper['text'] = f"{self.name_o}'s turn"

            self._update_map(self.b, 'X')
            self._update_to_map()
            self.check_winner('X')

        elif b_text == '' and turn is False:
            self.b['text'] = 'O'
            turn = True
            counter += 1
            self._upload_config(turn=turn, counter=counter)

            self.helper['fg'] = self.x_color
            self.helper['text'] = f"{self.name_x}'s turn"

            self._update_map(self.b, 'O')
            self._update_to_map()
            self.check_winner('O')

        else:
            self.bell()

    def b_undo(self, event=None):
        """Undo last action."""
        global turn, xundo_counter, oundo_counter, counter

        if turn is False and self.b['text'] == 'X':
            if xundo_counter >= 1:
                self.bell()
            else:
                self.b['text'] = ' '
                turn = True

                self.helper['fg'] = 'red'
                self.helper['text'] = f"{self.name_x}'s replay"
                counter -= 1
                xundo_counter += 1
                oundo_counter = 0

        elif turn is True and self.b['text'] == 'O':
            if oundo_counter >= 1:
                self.bell()
            else:
                self.b['text'] = ' '
                turn = False

                self.helper['fg'] = 'blue'
                self.helper['text'] = f"{self.name_o}'s replay"
                counter -= 1
                oundo_counter += 1
                xundo_counter = 0

    def bell(self, event=None):
        """Ring a displays bell."""
        self.root.bell()

    def check_winner(self, who):
        """Check for winner between two players."""
        self._winstance(who)
        self._winarrange()

        if all(self.instance1):
            if who == 'X':
                for b in self.row1:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.row1:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance2):
            if who == 'X':
                for b in self.row2:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.row2:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance3):
            if who == 'X':
                for b in self.row3:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.row3:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance4):
            if who == 'X':
                for b in self.col1:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.col1:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance5):
            if who == 'X':
                for b in self.col2:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.col2:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance6):
            if who == 'X':
                for b in self.col3:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.col3:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance7):
            if who == 'X':
                for b in self.diag1:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.diag1:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif all(self.instance8):
            if who == 'X':
                for b in self.diag2:
                    b['bg'] = self.x_color
                    b['fg'] = self.bt_win_fg

            elif who == 'O':
                for b in self.diag2:
                    b['bg'] = self.o_color
                    b['fg'] = self.bt_win_fg
            self.declare_winner(who)

        elif counter >= 9:
            if self.msg_win('Nobody won', 'Nobody Won this round'):
                self.next_round('Nobody')

    def msg_win(self, title, msg, type_='okcancel') -> bool:
        """Popup window for messages."""
        ms = msgbox.Message(self.root, title=title,
                            message=msg).show(type_=type_)
        if type_ == 'yesno':
            if ms.__contains__('yes'):
                return True
            elif ms.__contains__('no'):
                return False
        if type_ == 'okcancel':
            return bool(ms)

    def declare_winner(self, who, game=False):
        """Declare the winner for the round."""
        global turn
        if not game:
            if who == 'X':
                self.helper['fg'] = self.x_color
                self.helper['text'] = f'{self.name_x} won'
                turn = True  # Changes who plays first after win
                self._upload_config(turn=turn)
                if self.msg_win(f'X won',
                                f'{self.name_x}. You won this round'):
                    self.next_round('X')
                    self.helper['text'] = f'{self.name_x}\'s turn'

            elif who == 'O':
                self.helper['fg'] = self.o_color
                self.helper['text'] = f'{self.name_o} won'
                turn = False  # Changes who plays first after win
                self._upload_config(turn=turn)
                if self.msg_win(f'O won',
                                f'{self.name_o}. You won this round'):
                    self.next_round('O')
                    self.helper['text'] = f'{self.name_o}\'s turn'
        elif game:
            pass

    def next_round(self, who_won):
        """Go to next round."""
        global turn
        self.reset()
        if who_won == 'X':
            turn = True
            self._upload_config(turn=turn)
            self.award_score_to('X')
        elif who_won == 'O':
            turn = False
            self._upload_config(turn=turn)
            self.award_score_to('O')
        elif str(who_won).capitalize().__contains__('Nobody'):
            self.reset()
        else:
            self.reset()

    def award_score_to(self, who):
        """Give a score to 'who'."""
        if who == 'X':
            self._temp_config['Score']['X'] += 1
            self._upload_config()
            self._read_config()
            self.x_slabel['text'] = self.x_score
        elif who == 'O':
            self._temp_config['Score']['O'] += 1
            self._upload_config()
            self._read_config()
            self.o_slabel['text'] = self.o_score
        else:
            pass

    def reset(self, with_scores=False, with_names=False):
        """Clear the game area that is used by
        next_round(self, who_won)."""
        global counter, turn
        counter = 0
        self._upload_config(counter=0)
        self._reset_map()

        if not with_scores:
            for b in self.bt_list:
                b['text'] = ' '
                b['fg'] = self.bt_fg
                b['bg'] = self.bt_bg

        elif with_scores:
            self._temp_config['Score']['X'] = 0
            self._temp_config['Score']['O'] = 0
            self._upload_config()
            self._read_config()
            self.x_slabel['text'] = self.x_score
            self.o_slabel['text'] = self.o_score

            for b in self.bt_list:
                b['text'] = ' '
                b['fg'] = self.bt_fg
                b['bg'] = self.bt_bg

        if with_names:
            self.start_afresh()

        else:
            pass

    def _reset_map(self, event=None):
        """Reset the map json file"""
        global counter, turn
        for bt in self.bt_list:
            self._temp_map[bt.winfo_name()] = ' '
        self._update_to_map()
        counter = 0
        self._upload_config(counter=counter)

    def _ask_load_game(self, event=None):
        """Ask whether to load last game or start a new game."""
        return self.msg_win(
            'Load or New?',
            'Do you want to continue from where you stopped?',
            'yesno')

    # Game
    def load_or_new(self, skipped=True, event=None):
        self._read_map()
        self._read_config()
        # if names are inputed and names are equal to most
        # recent game names then ask

        # if yes continue last game
        # if no reset scores

        #  else if names are not
        # inputed then take the names from previous game
        # and ask for continuation

        # if yes continue last game
        # if no reset to defaults

        # This checks if names of current game matches with
        # previous game names and stores it in the variable
        # as a true or false value
        eq_to_prev_game = (
            self.name_x == self._map['Gameof']['X'] and
            self.name_o == self._map['Gameof']['O']
        )

        # Checks if continue button was clicked
        # and if the names inputted are equal to
        # previous game names
        if (not self.skipped) & eq_to_prev_game:
            if self._ask_load_game():
                self.load_game()
            else:
                self.new_game()

        elif (not self.skipped) and (not eq_to_prev_game):
            self.new_game()

        elif skipped:
            self._read_map()
            if any(self.g_area_checker) | any(self.scores):
                if self._ask_load_game():
                    self.load_game()
                else:
                    self.new_game(True)

    def load_game(self, event=None):
        """Load last saved game."""
        self._load_map()

        # count how many buttons have an X or an O
        self.count = self.g_area_checker.count(True)

        self._upload_config(counter=self.count)
        self.check_winner('X')
        self.check_winner('O')
        self.check_winner('Nobody')

    def new_game(self, reset_names=False, event=None):
        """Play new game."""
        self.reset(with_scores=True, with_names=reset_names)

    def start_afresh(self):
        self._temp_config["Name"]["X"] = defaults.X_NAME
        self._temp_config["Name"]["O"] = defaults.O_NAME
        self._temp_config["turn"] = defaults.TURN
        self._upload_config()

        self._read_config()
        self.x_label['text'] = f"{self.name_x} (X): "
        self.o_label['text'] = f"{self.name_o} (O): "

    # Definitions for properties
    def _get_x_color(self, event=None):
        self._read_settings()
        return self.x_color

    def _get_o_color(self, event=None):
        self._read_settings()
        return self.o_color

    def _set_x_color(self, color: str):
        self._read_settings()
        self._temp_settings['Theme']['xColor'] = color
        self.settings['Theme']['xColor'] = color
        self._upload_settings()

    def _set_o_color(self, color: str, event=None):
        self.settings['Theme']['oColor'] = color
        self._upload_settings()

    color_x = property(_get_x_color, _set_x_color)
    color_o = property(_get_o_color, _set_o_color)

    # exit
    def _quit(self, event=None):
        """Exit the app."""
        self._update_to_map()
        self._update_last_gameof()
        self.root.destroy()

    # Assignment of variables to methods for clearer understanding
    load_map_to_current_game = _load_map


if __name__ == '__main__':
    ChooseSide()

    # NOTE List problems here
    # after loading, check for winner DONE
