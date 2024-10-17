Change language to: [![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/dozzky/telegram_bot/blob/main/ReadMe.md)


## Telegram bot template (poorly written) for generating images

The aiogram library is used for the bot and diffusers with models from huggingface (You will need to download them locally - the first time you run from_pretrained, the download should happen automatically).

### Command list:

|Name|Description|Parameters on launch|
|:-:|:-:|:-:|
|/draw [Your_Prompt]|Command for drawing images|-|
|/params|Command to show model hyper parameters|-|
|/param_guide [Number]|Change parameter 'Guidance_scale'|8|
|/param_width [Number]|Change parameter 'Image width'|1024|
|/param_height [Number]|Change parameter 'Image height'|1024|
|/param_negative [Neg_prompt]|Change parameter 'Negative prompt'|None|
|/param_steps [Number]|Change parameter 'Number of steps'|50|

If you want to change parameters on launch - just change their value in telegram_bot.py

### Prompting Tips:

|Light|Resolution|Style|Styles via sites|Styles via authors|Material|
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

### Additionally:

I also wanted to run the language model, but I couldn't fit it into the gpu memory (the code is commented out). If you want to enable it, you will also need to download the language model and the tokenizer (in the case of the latter, I used my own tokenizer in the code, but I advise you to rewrite it so that it is taken from huggingface using .from_pretrained).
