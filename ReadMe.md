[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/dozzky/telegram_bot/blob/main/ReadMe_english.md)

## Шаблон (написанный на коленке) телеграм бота для генерации изображений

Используется библиотека aiogram для бота и diffusers с моделями из huggingface (Нужно будет их скачать локально - при первом запуске from_pretrained загрузка должна произойти автоматически).

### Список команд:

|Название|Описание|Параметры при загрузке|
|:-:|:-:|:-:|
|/draw [Ваш_Промпт]|Команда создания изображений|-|
|/params|Команда для отображения актуальных гиперпараметров|-|
|/param_guide [Число]|Изменение параметра 'Стремление к промпту'|8|
|/param_width [Число]|Изменение параметра 'Ширина изображения'|1024|
|/param_height [Число]|Изменение параметра 'Высота изображения'|1024|
|/param_negative [Нег_Промпт]|Изменение параметра 'Негативный промпт'|None|
|/param_steps [Число]|Изменение параметра 'Количество шагов'|50|

Если хотите изменить параметры при загрузке - просто измените их значения в telegram_bot.py

### Советы при промптинге:

|Свет|Разрешение|Стиль|Стили через сайты|Стили через авторов|Материал|
|:-:|:-:|:-:|:-:|:-:|:-:|
|cinematic lighting|unreal engine|hyperrealistic|pixiv — стиль японских аниме|Stanley Artgerm Lau|portrait|
|illumination|sharp focus|pop-art|pixabay — коммерческие стоковые фотографий|John Singer Sargen|digital painting|
|dark|8k|modernist|artstation — современная иллюстрация, фэнтези|John Collier|concept art|
|god rays|vray|art nouveau|deviant art — сообщество художников общего типа|Frida Kahlo|ultra realistic illustration|
|atmospheric|highly detailed|fantasy||Alphonse Mucha|underwater portrait|
|sunlight|sharp focus|surrealist||Van Gogh|photograph|
|backlight||steampunk|||oil painting|
|||photorealisic||||
|||sci-fi||||

### Дополнительно:

Также хотел запустить языковую модель, но не смог уместить его в памяти видеокарты (код закомментирован). Если хотите его включить, надо будет скачать также языковую модель и токенизатор (в случае последнего в коде у меня использовался свой собственный токенизатор, вам же советую его переписать, чтобы он брался с huggingface с помощью .from_pretrained).
