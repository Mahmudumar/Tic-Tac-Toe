import json  # For data dumping and loading
import os  # For directory checking and stuff...
bin_dir = 'C:\\Users\\LENOVO\\Programming\\PYTHON\\XandO(new)\\.bin\\'
settings = {
    "Theme": {
        "themeColor": "",

        "label": {
            "Background": "white",
            "Foreground": "black"
        },
        "labelframe": {
            "Background": "white",
            "Foreground": "black"
        },
        "backframe": {
            "Background": "white"
        },
        "button": {
            "Background": "white",
            "Foreground": "black",
            "WinForeground": "white"
        },
        "gamearea": {
            "Background": "#dcdcdc",
            "Foreground": "white"
        },
        "xColor": "red",
        "oColor": "blue"
    },

    "Score": {
        "ScoretoPlay": 20,
        "withSystem": False
    },

    "Font": {
        "Family": 'consolas',
        "Size": 30
    }

}

config = {
    "Name": {
        "X": "Player 1",
        "O": "Player 2"
    },

    "Score": {
        "X": 0,
        "O": 0
    },
    "turn": True,
    "counter": 0,
    "xundo_counter": 0,
    "oundo_counter": 0,
    "fullscreen": False
}

Stats = {
    "Wins": {
        "lifeWins": {  # wins throughout lifetime
            "X": 0,
            "O": 0}
    },

    "Loses": {
        "lifeLoses": {  # loses throughout lifetime
            "X": 0,
            "O": 0}
    }

}

most_recent_game = {
    "Gameof": {"X": "",
               "O": ""},
    "bt1": ' ', "bt2": ' ', "bt3": ' ',
    "bt4": ' ', "bt5": ' ', "bt6": ' ',
    "bt7": ' ', "bt8": ' ', "bt9": ' '
}

X_NAME = str(config["Name"]["X"])
O_NAME = str(config["Name"]["O"])
TURN = bool(config["turn"])
COUNTER = int(config["counter"])
XUNDO_COUNTER = int(config["xundo_counter"])
OUNDO_COUNTER = int(config["oundo_counter"])


class Settings:
    def reset_to_defaults(self):
        if os.path.isfile(f'{bin_dir}settings.json'):
            with open(f'{bin_dir}settings.json', 'w') as _settings:
                json.dump(settings, _settings, indent=4)
        return 'done'


class Configuration:
    def reset_to_defaults(self):
        if os.path.isfile(f'{bin_dir}config.json'):
            with open(f'{bin_dir}config.json', 'w') as _configuration:
                json.dump(config, _configuration, indent=4)
        return 'done'


class Maps:
    def reset_to_defaults(self):
        with open(f"{bin_dir}map.json", 'w') as most_rcnt:
            json.dump(most_recent_game, most_rcnt, indent=4)
        return 'done'


def reset(what: str):
    if what.__contains__('settings'):
        return Settings().reset_to_defaults()
    elif what.__contains__('config'):
        return Configuration().reset_to_defaults()
    elif what.__contains__('map'):
        return Maps().reset_to_defaults()
    elif what.__contains__('all'):
        Settings().reset_to_defaults()
        Maps().reset_to_defaults()
        Configuration().reset_to_defaults()
        return True

    else:
        raise TypeError(
            f"{what} is not valid. Must be one of settings, config or map ")


def ask_reset():
    ask = input("What do you want to reset: ")
    reset(ask)


if __name__ == '__main__':
    ask_reset()
