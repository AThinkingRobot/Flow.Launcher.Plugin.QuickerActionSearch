import csv
from pypinyin import lazy_pinyin, Style
import pyperclip


class Actions:
    def __init__(self):
        self.dict_action = {}
        self.dict_py_action = {}

        with open('D:\Src\PyCharmProjects\Flow.Launcher.Plugin.QuickerActionSearch\quickeractions.csv') as f:
            f_csv = csv.reader(f)
            for index, row in enumerate(f_csv):
                if index == 0 or index == 1:
                    continue
                self.dict_action[row[1]] = row
                action_name_initial = ''.join(lazy_pinyin(row[1], style=Style.FIRST_LETTER))
                self.dict_py_action[action_name_initial] = row

    def actions(self, is_chinese):
        if is_chinese:
            return self.dict_action
        else:
            return self.dict_py_action


if __name__ == "__main__":
    u = Actions()
    u.actions(None)
