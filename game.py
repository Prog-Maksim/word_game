# -*- coding: utf-8 -*-

import json
import os.path
import random
from datetime import datetime, timedelta, time as d_time

import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


def create_json_file() -> None:
    """
    Создаем json файл где в последующем храним статистику игры
    :return: None
    """

    with open("game_statistics.json", 'w', encoding='utf-8') as file:
        data = {
            "number_of_games": 0,
            "number_of_wins": 0,
            "number_of_losers": 0,
            "series_of_victories": [0],
        }

        json.dump(data, file, indent=4, ensure_ascii=False)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.monitor_height = self.winfo_screenheight()
        self.monitor_width = self.winfo_screenwidth()
        pos_x = int((self.monitor_width - 325) / 2)
        pos_y = int((self.monitor_height - 550) / 2)
        self.geometry(f'325x560+{pos_x}+{pos_y}')
        self.title('Five letter game')

        self.delete_mode = False  # Режим игры с удалением клавиатуры
        self.game = False  # Игра false - игры нет, true - идет игра
        self.inform_menu = False  # Открыто или закрыто дополнительное окно (меню)

        # Вызов меню создания интерфейса
        self.create_window()

    def create_window(self) -> None:
        """
        Создаем основное пустое меню и вызываем функции для их заполнения
        :return: None
        """

        # Фрейм вырхнего меню
        self.inform_frame = ctk.CTkFrame(master=self, width=280, height=50)
        self.inform_frame.place(x=20, y=20)

        # Фрейм меню игры
        self.game_frame = ctk.CTkFrame(master=self, width=280, height=335)
        self.game_frame.place(x=20, y=80)

        # Фрейм клавиатуры
        self.keyboard_frame_1 = ctk.CTkFrame(master=self, width=280, height=120)
        self.keyboard_frame_1.place(x=20, y=425)

        if not os.path.exists('game_statistics.json'):
            create_json_file()

        self.label_function()
        self.menu_entry()
        self.start_game()

    def label_function(self) -> None:
        """
        Создает заголовок игры а также кнопку "меню"
        :return: None
        """

        self.label_button_1 = ctk.CTkButton(
            master=self.inform_frame,
            width=30, height=30,
            text='5',
            font=('Arial', 15, 'bold'),
            text_color='black',
            fg_color='#FEDE2B',
            corner_radius=7,
            hover=False
        )
        self.label_button_1.place(x=10, y=10)

        self.label_button_2 = ctk.CTkButton(
            master=self.inform_frame,
            width=30, height=30,
            text='Б',
            font=('Arial', 15, 'bold'),
            text_color='black',
            fg_color='#FEDE2B',
            corner_radius=7,
            hover=False
        )
        self.label_button_2.place(x=45, y=10)

        self.label_button_3 = ctk.CTkButton(
            master=self.inform_frame,
            width=30, height=30,
            text='У',
            font=('Arial', 15, 'bold'),
            text_color='black',
            fg_color='#FEDE2B',
            corner_radius=7,
            hover=False
        )
        self.label_button_3.place(x=80, y=10)

        self.label_button_4 = ctk.CTkButton(
            master=self.inform_frame,
            width=30, height=30,
            text='К',
            font=('Arial', 15, 'bold'),
            text_color='black',
            fg_color='#FEDE2B',
            corner_radius=7,
            hover=False
        )
        self.label_button_4.place(x=115, y=10)

        def mode():
            if not self.game:
                if self.delete_mode:
                    self.delete_mode = False
                    self.label_button_5.configure(fg_color='#FEDE2B')
                else:
                    self.delete_mode = True
                    self.label_button_5.configure(fg_color='white')

        self.label_button_5 = ctk.CTkButton(
            master=self.inform_frame,
            width=30, height=30,
            text='В',
            font=('Arial', 15, 'bold'),
            text_color='black',
            fg_color='#FEDE2B',
            corner_radius=7,
            hover=False,
            command=mode
        )
        self.label_button_5.place(x=150, y=10)

        self.image_arrow = ctk.CTkImage(
            Image.open('image/information.png'),
            size=(20, 20))

        self.information_button = ctk.CTkButton(
            master=self.inform_frame,
            width=30, height=30,
            text='',
            fg_color='transparent',
            image=self.image_arrow,
            hover=False,
            command=self.open_instruction
        )
        self.information_button.place(x=180, y=10)

    def menu_entry(self) -> None:
        """
        Функция создает разметку для игровой клетки в определенной позиции
        :return: None
        """
        self.obj = list()
        num = 1
        x = 5
        y = 5
        for i in range(35):
            if num <= 5:
                obj = self.create_game_entry(pos_x=x, pos_y=y)
                self.obj.append(obj)
                num += 1
                x += 55
            else:
                num = 1
                x = 5
                y += 55

    def create_game_entry(self, pos_x: int, pos_y: int) -> None:
        """
        Создает игровую клетку где вводятся буквы
        :param pos_x: Позиция игровой клетки по оси X
        :param pos_y: Позиция игровой клетки по оси Y
        :return:
        """

        self.entry_button_1 = ctk.CTkEntry(
            master=self.game_frame,
            width=50, height=50,
            fg_color='#2B2B2B',
            font=('Arial', 25, 'bold'),
            corner_radius=7,
            border_width=1,
            border_color='#FEDE2B',
            state='disabled'
        )
        self.entry_button_1.place(x=pos_x, y=pos_y)
        return self.entry_button_1

    def open_instruction(self) -> None:
        """
        Создает дополнительное окно с инструкцией как играть и статистикой игры
        :return: None
        """

        if not self.inform_menu:
            self.instruction_frame = ctk.CTkFrame(master=self, width=280, height=525)
            self.instruction_frame.place(x=310, y=20)

            pos_x = int((self.monitor_width - 500) / 2)
            pos_y = int((self.monitor_height - 550) / 2)
            self.geometry(f'610x560+{pos_x}+{pos_y}')

            self.instruction_text_frame = ctk.CTkFrame(
                master=self.instruction_frame,
                width=210, height=40,
                fg_color='#545454',
                bg_color='transparent',
                corner_radius=10
            )
            self.instruction_text_frame.place(x=10, y=10)

            self.text = ctk.CTkLabel(
                master=self.instruction_text_frame,
                width=200, height=30,
                text='Правила игры',
                fg_color='transparent',
                bg_color='transparent',
                text_color='white',
                font=('Arial', 15, 'bold')
            )
            self.text.place(x=5, y=5)

            self.exit_image = ctk.CTkImage(
                Image.open('image/Exit_menu.png'),
                size=(20, 20))

            self.exit_frame = ctk.CTkFrame(
                master=self.instruction_frame,
                width=40, height=40,
                fg_color='#545454',
                bg_color='transparent',
                corner_radius=10
            )
            self.exit_frame.place(x=230, y=10)

            def close_instruction_menu():
                pos_x = int((self.monitor_width - 325) / 2)
                pos_y = int((self.monitor_height - 550) / 2)
                self.geometry(f'325x560+{pos_x}+{pos_y}')
                self.inform_menu = False

                self.instruction_frame.destroy()

            self.exit_button = ctk.CTkButton(
                master=self.exit_frame,
                width=30, height=30,
                fg_color='transparent',
                bg_color='transparent',
                image=self.exit_image,
                text='',
                hover=False,
                command=close_instruction_menu
            )
            self.exit_button.place(x=2, y=5)

            self.instruction_text = ctk.CTkFrame(
                master=self.instruction_frame,
                width=260, height=310,
                fg_color='#545454',
                bg_color='transparent',
                corner_radius=10
            )
            self.instruction_text.place(x=10, y=60)

            text = "Как играть в игру 5 букв \nВ начале игры появляется поле, \nсостоящее из 30 клеток, по пять \nштук в строчках и по шесть штук в \nстолбцах. В это поле можно вписать \nшесть слов, состоящих из пяти букв. \nПринимаются только сущ в ед числе. \nНиже клавиатура на которой \nпоказывается статус букв. \nНачинайте вводить любое слово, \nкак например слово «океан», \nнажмите на кнопку ввод и буквы \nпоменяют цвет. Расшифровка такая: \n1) желтая буква — есть в слове на \nсвоем месте. \n2) белая — есть в слове но в другом \nместе. \n3) серая — буквы в слове нет."

            self.instr_text = ctk.CTkLabel(
                master=self.instruction_text,
                width=250, height=300,
                text=text,
                text_color='white',
                anchor='w',
                font=('Arial', 14)
            )
            self.instr_text.place(x=5, y=5)

            self.score_text = ctk.CTkFrame(
                master=self.instruction_frame,
                width=260, height=135,
                fg_color='#545454',
                bg_color='transparent',
                corner_radius=10
            )
            self.score_text.place(x=10, y=380)

            self.text = ctk.CTkLabel(
                master=self.score_text,
                width=100, height=125,
                text='Процент побед: \n\nСлов отгадано: \n\nВ среднем попыток: \n\nЛучшая серия побед:',
                text_color='white',
                justify='left',
                font=('Arial', 15, 'bold')
            )
            self.text.place(x=7, y=5)

            self.score_txt_1 = ctk.CTkLabel(
                master=self.score_text,
                width=40, height=20,
                text='0%',
                text_color='#FEDE2B',
                justify='right',
                font=('Arial', 15, 'bold')
            )
            self.score_txt_1.place(x=210, y=5)

            self.score_txt_2 = ctk.CTkLabel(
                master=self.score_text,
                width=40, height=20,
                text='0',
                text_color='#FEDE2B',
                justify='right',
                font=('Arial', 15, 'bold')
            )
            self.score_txt_2.place(x=210, y=40)

            self.score_txt_3 = ctk.CTkLabel(
                master=self.score_text,
                width=40, height=20,
                text='0',
                text_color='#FEDE2B',
                justify='right',
                font=('Arial', 15, 'bold')
            )
            self.score_txt_3.place(x=210, y=75)

            self.score_txt_4 = ctk.CTkLabel(
                master=self.score_text,
                width=40, height=20,
                text='0',
                text_color='#FEDE2B',
                justify='right',
                font=('Arial', 15, 'bold')
            )
            self.score_txt_4.place(x=210, y=110)

            self.inform_menu = True
            self.update_score()

    def update_score(self) -> None:
        """
        Данная функция обновляет игровую статистику на экране меню
        :return: None
        """
        if self.inform_menu:
            with open("game_statistics.json", 'r', encoding='utf-8') as file:
                data = dict(json.load(file))

            try:
                win_percentage: str = str(int((data['number_of_wins'] / data['number_of_games']) * 100))
            except ZeroDivisionError:
                win_percentage: str = '0'

            self.score_txt_1.configure(text=win_percentage + '%')
            self.score_txt_2.configure(text=data['number_of_wins'])
            self.score_txt_3.configure(text=data['number_of_games'])
            self.score_txt_4.configure(text=max(data['series_of_victories']))

    def save_resurlt_game(self, status_game: bool) -> None:
        """
        :param status_game: принимает True или False
        True - игра выйграна
        False - игра проиграна
        :return: None
        """

        with open("game_statistics.json", 'r', encoding='utf-8') as file:
            data = dict(json.load(file))

        with open("game_statistics.json", 'w', encoding='utf-8') as file:
            data['number_of_games'] += 1
            data['number_of_wins'] += 1 if status_game else 0
            data['number_of_losers'] += 1 if not status_game else 0

            if status_game:
                data['series_of_victories'][-1] += 1
            else:
                data['series_of_victories'].append(0)

            json.dump(data, file, indent=4, ensure_ascii=False)

    def start_game(self, label: str = 'Начать игру?', text: str = 'Отгадайте слово', button_text: str = 'Начать') -> None:
        """
        Создает меню начала игры, или меню после проигрыша
        :param label: Заголовок меню
        :param text: Текст меню
        :param button_text: Текст кнопки
        :return: None
        """

        self.inform_label = ctk.CTkLabel(
            master=self.keyboard_frame_1,
            width=270,
            text=label,
            font=("Arial", 17, 'bold'),
            text_color='#FEDE2B'
        )
        self.inform_label.place(x=5, y=5)

        self.start_frame = ctk.CTkFrame(
            master=self.keyboard_frame_1,
            width=250, height=70,
            fg_color='#545454',
            corner_radius=17
        )
        self.start_frame.place(x=15, y=40)

        self.start_label = ctk.CTkLabel(
            master=self.start_frame,
            width=240,
            text=text,
            text_color='#F2F2F4',
            font=("Arial", 15)
        )
        self.start_label.place(x=5, y=2)

        def start():
            self.inform_label.destroy()
            self.start_frame.destroy()

            try:
                for num, i in enumerate(self.obj):
                    i.configure(state='normal', border_color='#FEDE27', fg_color='#2B2B2B', text_color='white')
                    i.delete(0, tk.END)
                    i.configure(state='disabled', border_color='#FEDE27', fg_color='#2B2B2B', text_color='white')
            except:
                pass

            self.start_time_game()

        self.start_button = ctk.CTkButton(
            master=self.start_frame,
            width=150, height=35,
            text=button_text,
            font=('Arial', 15, 'bold'),
            text_color='white',
            fg_color='#373737',
            corner_radius=13,
            hover_color='#3D3D3D',
            command=start
        )
        self.start_button.place(x=50, y=28)

    def random_word_game(self) -> None:
        """
        Данная функция достает и загадывает рандомное слово из data-set
        :return: None
        """

        with open("word_dictionary.json", 'r', encoding='utf-8') as file:
            data = dict(json.load(file))

            symbol = random.choice(list((data.keys())))
            self.game_in_words = str(random.choice(data[symbol])).upper()

    def start_time_game(self) -> None:
        """
        Данная функция начинает игровой процесс, устанавливает время и создает клавиатуру для игры
        :return: None
        """

        self.game = True

        self.words = dict()
        self.game_level = 1  # Уровень игры (соответствует ряду слов) (1 уров == 1 ряд)

        a = [[0, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]
        for i in range(1, 7):
            self.words[i] = {"game": self.game, "words": ['', '', '', '', ''], "obj": self.obj[a[i - 1][0]: a[i - 1][-1]]}

        self.random_word_game()

        self.time_label = ctk.CTkLabel(
            master=self.inform_frame,
            text='15:00',
            text_color='white',
            font=('Arial', 15, 'bold')
        )
        self.time_label.place(x=220, y=10)

        def time() -> None:
            """
            Функция отсчета времени, данная функция проверяет сколько времени осталось и если время закончилось то завершает игру
            :return: None
            """
            times = d_time(0, 0, 0)
            red_time = d_time(0, 0, 30)

            time_object = datetime.strptime(self.time_label.cget('text'), '%M:%S')
            time_delta = timedelta(seconds=1)
            new_time = time_object - time_delta

            if new_time.time() == times:
                self.game = False
                self.keyboard_frame.destroy()
                self.start_game(label='Вы проиграли!', text="Время закончилось", button_text='Заново!')
                self.save_resurlt_game(status_game=False)
                self.update_score()

                for game_cell in self.obj:
                    game_cell.configure(state='disabled', border_color='#FEDE27', fg_color='#2B2B2B', text_color='white')

                self.time_label.configure(text_color='white')
            elif new_time.time() <= red_time:  # Делает текст красным если времени осталось меньше 30 сек
                self.time_label.configure(text_color='red')

            self.time_label.configure(text=str(new_time.time())[3:])
            if self.game:
                self.after(1000, time)

        self.after(1000, time)

        self.keyboard_frame = ctk.CTkFrame(master=self.keyboard_frame_1, width=280, height=120, fg_color='#2B2B2B')
        self.keyboard_frame.place(x=0, y=0)
        self.keyboard_button()

    def click_button(self, event) -> None:
        """
        Данная функция вызывается при нажатии на кнопку на клавиатуре как сенсорной так и физической и
        в игровую ячейку вставляет нажатую букву
        :param event: Принимает обьект нажатой кноки
        :return: None
        """
        if self.game:
            status = self.words[self.game_level]

            if status['game'] == True:
                for num, i in enumerate(status['words']):
                    if len(i) == 0:
                        status['words'][num] = event.cget('text')
                        status['obj'][num].configure(state='normal')
                        status['obj'][num].insert(0, f" {event.cget('text')}")
                        status['obj'][num].configure(state='disabled')
                        break

    def clear_end_symbol(self) -> None:
        """
        Данная функция удаляет последнюю букву с игровой ячейки
        :return: None
        """

        if self.game:
            status = self.words[self.game_level]
            if status['game'] == True:
                for num, i in reversed(list(enumerate(status['words']))):
                    if len(i) != 0:
                        status['words'][num] = ''
                        status['obj'][num].configure(state='normal')
                        status['obj'][num].delete(0, tk.END)
                        status['obj'][num].configure(state='disabled')
                        break

    def search_word(self) -> None:
        """
        Данная функция проверяет какое слово ввели на данном уровне, если слово найдено завершает игре,
        если нет окрашывает ячейки в нужный цвет
        :return: None
        """
        if self.game:
            status = self.words[self.game_level]
            if status['game'] == True:
                for i in status['words']:
                    if len(i) == 0:
                        return None

            self.game_level += 1

            if self.game_in_words == "".join(status['words']):
                self.game = False
                self.save_resurlt_game(status_game=True)
                self.keyboard_frame.destroy()
                self.start_game(label='Вы отгадали слово!')
            else:
                if self.game_level == 7:
                    self.game = False
                    self.save_resurlt_game(status_game=False)
                    self.keyboard_frame.destroy()
                    self.start_game(label='Вы проиграли!', text=f'Загаданное слово: {self.game_in_words}',
                                    button_text='Продолжить')
            self.update_score()
            try:
                for i, j, word, win in zip(status['obj'], self.words[self.game_level]['obj'], status['words'],
                                           list(self.game_in_words)):
                    if word == win:
                        i.configure(fg_color='#FEDE27', text_color='black')
                        self.keyboard_button_game[word].configure(fg_color='#FEDE27', text_color='black',
                                                                  border_color='#FEDE27')
                    elif word in list(self.game_in_words):
                        i.configure(fg_color='white', text_color='black', border_color='white')
                        self.keyboard_button_game[word].configure(fg_color='white', text_color='black',
                                                                  border_color='white')
                    elif word not in list(self.game_in_words):
                        i.configure(fg_color='#5F5F5F', border_color='#5F5F5F')
                        self.keyboard_button_game[word].configure(fg_color='#5F5F5F', border_color='#5F5F5F')
                        self.keyboard_button_game[word].destroy() if self.delete_mode else ...

                    i.configure(state='disabled')  # Основная строчка блокируем
                    j.configure(state='normal') if self.game else ...  # Следующее игровое поле разблокируем

                self.words[self.game_level]['game'] = True
                self.words[self.game_level - 1]['game'] = False
            except:
                for i, word, win in zip(status['obj'], status['words'], list(self.game_in_words)):
                    if word == win:
                        i.configure(fg_color='#FEDE27', text_color='black')
                    elif word in list(self.game_in_words):
                        i.configure(fg_color='white', text_color='black', border_color='white')
                    elif word not in list(self.game_in_words):
                        i.configure(fg_color='#5F5F5F', border_color='#5F5F5F')

                    i.configure(state='disabled')  # Основная строчка блокируем

                self.words[self.game_level - 1]['game'] = False

    def keyboard_button(self) -> None:
        """
        Функция создает клавиатуру для игры,
        а также обрабатывает ввод с клавиатуры
        :return: None
        """

        self.keyboard_button_1 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Й',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_1)
        )
        self.keyboard_button_1.place(x=3, y=5)
        self.bind("q", lambda a: self.click_button(self.keyboard_button_1))

        self.keyboard_button_2 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ц',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_2)
        )
        self.keyboard_button_2.place(x=26, y=5)
        self.bind("w", lambda a: self.click_button(self.keyboard_button_2))

        self.keyboard_button_3 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='У',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_3)
        )
        self.keyboard_button_3.place(x=49, y=5)
        self.bind("e", lambda a: self.click_button(self.keyboard_button_3))

        self.keyboard_button_4 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='К',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_4)
        )
        self.keyboard_button_4.place(x=72, y=5)
        self.bind("r", lambda a: self.click_button(self.keyboard_button_4))

        self.keyboard_button_5 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Е',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_5)
        )
        self.keyboard_button_5.place(x=95, y=5)
        self.bind("t", lambda a: self.click_button(self.keyboard_button_5))

        self.keyboard_button_6 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Н',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_6)
        )
        self.keyboard_button_6.place(x=118, y=5)
        self.bind("y", lambda a: self.click_button(self.keyboard_button_6))

        self.keyboard_button_7 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Г',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_7)
        )
        self.keyboard_button_7.place(x=141, y=5)
        self.bind("u", lambda a: self.click_button(self.keyboard_button_7))

        self.keyboard_button_8 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ш',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_8)
        )
        self.keyboard_button_8.place(x=164, y=5)
        self.bind("i", lambda a: self.click_button(self.keyboard_button_8))

        self.keyboard_button_9 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Щ',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_9)
        )
        self.keyboard_button_9.place(x=187, y=5)
        self.bind("o", lambda a: self.click_button(self.keyboard_button_9))

        self.keyboard_button_10 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='З',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_10)
        )
        self.keyboard_button_10.place(x=210, y=5)
        self.bind("p", lambda a: self.click_button(self.keyboard_button_10))

        self.keyboard_button_11 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Х',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_11)
        )
        self.keyboard_button_11.place(x=233, y=5)
        self.bind("[", lambda a: self.click_button(self.keyboard_button_11))

        self.keyboard_button_12 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ъ',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_12)
        )
        self.keyboard_button_12.place(x=256, y=5)
        self.bind("]", lambda a: self.click_button(self.keyboard_button_12))

        self.keyboard_button_13 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ф',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_13)
        )
        self.keyboard_button_13.place(x=13, y=42)
        self.bind("a", lambda a: self.click_button(self.keyboard_button_13))

        self.keyboard_button_14 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ы',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_14)
        )
        self.keyboard_button_14.place(x=36, y=42)
        self.bind("s", lambda a: self.click_button(self.keyboard_button_14))

        self.keyboard_button_15 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='В',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_15)
        )
        self.keyboard_button_15.place(x=59, y=42)
        self.bind("d", lambda a: self.click_button(self.keyboard_button_15))

        self.keyboard_button_16 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='А',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_16)
        )
        self.keyboard_button_16.place(x=82, y=42)
        self.bind("f", lambda a: self.click_button(self.keyboard_button_16))

        self.keyboard_button_17 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='П',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_17)
        )
        self.keyboard_button_17.place(x=105, y=42)
        self.bind("g", lambda a: self.click_button(self.keyboard_button_17))

        self.keyboard_button_18 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Р',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_18)
        )
        self.keyboard_button_18.place(x=128, y=42)
        self.bind("h", lambda a: self.click_button(self.keyboard_button_18))

        self.keyboard_button_19 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='О',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_19)
        )
        self.keyboard_button_19.place(x=151, y=42)
        self.bind("j", lambda a: self.click_button(self.keyboard_button_19))

        self.keyboard_button_20 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Л',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_20)
        )
        self.keyboard_button_20.place(x=174, y=42)
        self.bind("k", lambda a: self.click_button(self.keyboard_button_20))

        self.keyboard_button_21 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Д',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_21)
        )
        self.keyboard_button_21.place(x=197, y=42)
        self.bind("l", lambda a: self.click_button(self.keyboard_button_21))

        self.keyboard_button_22 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ж',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_22)
        )
        self.keyboard_button_22.place(x=220, y=42)
        self.bind(";", lambda a: self.click_button(self.keyboard_button_22))

        self.keyboard_button_23 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Э',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_23)
        )
        self.keyboard_button_23.place(x=246, y=42)
        self.bind("'", lambda a: self.click_button(self.keyboard_button_23))

        self.image_checkmark = ctk.CTkImage(
            Image.open('image/checkmark.png'),
            size=(12, 12))

        def color_button():
            try:
                a = True
                game = self.words[self.game_level]
                if game['game'] == True:
                    for i in game['words']:
                        if len(i) == 0:
                            a = False
                            self.keyboard_button_24.configure(fg_color='white', hover_color='#ADADAD')
                if a:
                    self.keyboard_button_24.configure(fg_color='#FEDE2B', hover_color='#B5972A')
            except:
                pass
            self.after(100, color_button)

        self.keyboard_button_24 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=30, height=35,
            text='',
            image=self.image_checkmark,
            fg_color='white',
            corner_radius=5,
            hover_color='#ADADAD',
            command=self.search_word
        )
        self.keyboard_button_24.place(x=3, y=79)
        self.bind("<Return>", lambda a: self.search_word())

        self.after(100, color_button)

        self.keyboard_button_25 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Я',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_25)
        )
        self.keyboard_button_25.place(x=36, y=79)
        self.bind("z", lambda a: self.click_button(self.keyboard_button_25))

        self.keyboard_button_26 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ч',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_26)
        )
        self.keyboard_button_26.place(x=59, y=79)
        self.bind("x", lambda a: self.click_button(self.keyboard_button_26))

        self.keyboard_button_27 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='С',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_27)
        )
        self.keyboard_button_27.place(x=82, y=79)
        self.bind("c", lambda a: self.click_button(self.keyboard_button_27))

        self.keyboard_button_28 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='М',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_28)
        )
        self.keyboard_button_28.place(x=105, y=79)
        self.bind("v", lambda a: self.click_button(self.keyboard_button_28))

        self.keyboard_button_29 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='И',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_29)
        )
        self.keyboard_button_29.place(x=128, y=79)
        self.bind("b", lambda a: self.click_button(self.keyboard_button_29))

        self.keyboard_button_30 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Т',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_30)
        )
        self.keyboard_button_30.place(x=151, y=79)
        self.bind("n", lambda a: self.click_button(self.keyboard_button_30))

        self.keyboard_button_31 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ь',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_31)
        )
        self.keyboard_button_31.place(x=174, y=79)
        self.bind("m", lambda a: self.click_button(self.keyboard_button_31))

        self.keyboard_button_32 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Б',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_32)
        )
        self.keyboard_button_32.place(x=197, y=79)
        self.bind(",", lambda a: self.click_button(self.keyboard_button_32))

        self.keyboard_button_33 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=20, height=35,
            text='Ю',
            font=('Arial', 11),
            text_color='white',
            fg_color='#2B2B2B',
            border_color='#727272',
            border_width=1,
            corner_radius=5,
            hover_color='#424242',
            command=lambda: self.click_button(self.keyboard_button_33)
        )
        self.keyboard_button_33.place(x=220, y=79)
        self.bind(".", lambda a: self.click_button(self.keyboard_button_33))

        self.image_arrow = ctk.CTkImage(
            Image.open('image/arrow-left.png'),
            size=(15, 15))

        self.keyboard_button_34 = ctk.CTkButton(
            master=self.keyboard_frame,
            width=30, height=35,
            text='',
            image=self.image_arrow,
            fg_color='white',
            corner_radius=5,
            hover_color='#ADADAD',
            command=self.clear_end_symbol
        )
        self.keyboard_button_34.place(x=246, y=79)
        self.bind("<BackSpace>", lambda a: self.clear_end_symbol())

        self.keyboard_button_game = {'Й': self.keyboard_button_1, 'Ц': self.keyboard_button_2,
                                     'У': self.keyboard_button_3, 'К': self.keyboard_button_4,
                                     'Е': self.keyboard_button_5, 'Н': self.keyboard_button_6,
                                     'Г': self.keyboard_button_7, 'Ш': self.keyboard_button_8,
                                     'Щ': self.keyboard_button_9, 'З': self.keyboard_button_10,
                                     'Х': self.keyboard_button_11, 'Ъ': self.keyboard_button_12,
                                     'Ф': self.keyboard_button_13, 'Ы': self.keyboard_button_14,
                                     'В': self.keyboard_button_15, 'А': self.keyboard_button_16,
                                     'П': self.keyboard_button_17, 'Р': self.keyboard_button_18,
                                     'О': self.keyboard_button_19, 'Л': self.keyboard_button_20,
                                     'Д': self.keyboard_button_21, 'Ж': self.keyboard_button_22,
                                     'Э': self.keyboard_button_23, 'Я': self.keyboard_button_25,
                                     'Ч': self.keyboard_button_26, 'С': self.keyboard_button_27,
                                     'М': self.keyboard_button_28, 'И': self.keyboard_button_29,
                                     'Т': self.keyboard_button_30, 'Ь': self.keyboard_button_31,
                                     'Б': self.keyboard_button_32, 'Ю': self.keyboard_button_33}


if __name__ == "__main__":
    app = App()
    app.mainloop()
