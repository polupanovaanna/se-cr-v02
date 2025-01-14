## Casino

![Alt text](photo.jpg?raw=true "casino")

1. [cli-launch](#cli-launch)
2. [gui-launch](#gui-launch)
3. [documentation](#documentation)

## cli-launch
Берете такие хопа и `python3 app_cli.py`, и вот у вас запустилось казино 
на компе, даже зависимостей нет. 
Взаимодействие такое: вводите имя игрока, после этого его ставку из списка
`VoisinsDeZero`, `Tier`, `Orphelins`, `Parity 1`, `Parity 0`, `Color R`, `Color G`, `Color B`.
Если хотите играть с диллером, то просто в какой-то момент вводите имя диллер (он сам себе выберет ставку). В конце надо ввести `No new players`, игра закончится, выведется число выпавшее 
на колесе и кто выйграл/проиграл ставку. Вот красочный пример, показывающий всю суть игры в казино:
![Alt text](example.jpg?raw=true "Good Game")

## gui-launch
Достаточно запустить непосредственно файл `app_gui.py` с помощью команды `python3 app_gui.py`. После этого весь 
функционал приложения будет доступен через графический интерфейс

![Alt text](example2.png?raw=true "Good Game")

## documentation
Если вдруг вам захотелось использовать невероятно удобный интерфейс для создания нового казино, 
то вот инструкция. Все лежит в модуле [main.py](/main.py), там есть `RateType` -- описывает все возможные типы ставок в казино. Есть просто `Rate` -- хранит тип ставки и еще ее значение (например цвет/четность), а его метод `is_matching_number` проверяет, что при данном числе на колесе ставка выйгрышная. Дальше просто `RoundResult` хранит число на колесе + список кто выйграл/проиграл. `get_random_game_result` иммитурет случайную игру. `convert_string_to_rate` конвертирует строку в `Rate`.

