# проект Word Game

## Описание
Word Game - это игра для Windows.

<image src="C:\Users\maksi\Pictures\Screenshots\Game.png" alt="Режим игры">

Игра "Отгадай слово" предлагает вам отгадать слово, состоящее из 5 букв, за 6 
попыток. В поле для ввода можно вписать 6 слов, состоящих из 5 букв, как попытки 
отгадать слово. Принимаются только существительные в единственном числе.

После ввода слова появляется "статус букв", где каждая буква подсвечивается 
своим цветом:
1. Желтая - буква есть в слове и находится на своем месте.
2. Белая - буква есть в слове, но находится в другом месте.
3. Серая - буквы нет в данном слове.

Слова можно вводить с клавиатуры на английской раскладке или использовать экранную 
клавиатуру.

В игре есть два режима:
1. "Обычный" - вы просто играете в игру, отгадывая слово.
2. "Выбывание" - вы отгадываете слова, и буквы, которых нет в слове,
пропадают с клавиатуры.

Чтобы активировать режим игры "Выбывание", нажмите на кнопку "В" в названии игры.

<image src="C:\Users\maksi\Pictures\Screenshots\Button game.png" alt="Режим игры">

В игре присутствует статистика ваших игр, количество игр, количество отгаданных слов
и процент отгадывания слов

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение 
3. Установите зависимости `pip install -r requirements.txt`
4. Запустите игру командой `python3 game.py`

## Запуск игры

В данном проекте вас уже ждет готовая игра под windows в папке Word Game ->
Word Game.exe

## Используемые материалы

1. Иконки игры - <https:/www.flaticon.com>
2. Слова - <https://slovopoisk.ru>