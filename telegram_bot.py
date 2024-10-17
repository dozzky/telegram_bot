# Импорт библиотек для телеграм бота
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, FSInputFile
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import State, StatesGroup
# Импорт библиотек для модели
from diffusers import DiffusionPipeline, EulerDiscreteScheduler
import torch
from transformers import TorchAoConfig
from transformers import LlamaForCausalLM
from tokenizer import Tokenizer
# Импорты остальных библиотек
import asyncio
import logging
import sys
import os

# Загрузка токена и создание бота
TOKEN = 'YOUR_TOKEN'
dp = Dispatcher()
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Гиперпараметры при инициализации для модели изображений
negative_prompt = None
num_inference_steps = 50
height = 1024
width = 1024
guidance_scale = 8

# Приветик
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

# Команда создания изображений
@dp.message(Command("draw"))
async def any_message(msg: types.Message):
    prompt = msg.text[6:]

    await msg.reply("Принято, подождите немножко...")

    generator = torch.Generator("cuda").manual_seed(0)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)
    
    images = pipe(prompt=prompt, generator=generator, num_inference_steps=num_inference_steps,
                  height=height, width=width, guidance_scale=guidance_scale, negative_prompt=negative_prompt).images[0]
    
    image_path = 'last.jpg'
    images.save(image_path)
    if os.path.exists('last.jpg'):
        photo = FSInputFile(image_path)
        await msg.answer_photo(photo)
    else:
        await msg.reply("Ошибка: файл не был создан.")

# Команды изменения гиперпараметров
@dp.message(Command("param_steps"))
async def any_message(msg: types.Message):

    global num_inference_steps 
    num_inference_steps = int(msg.text[13:])
    await msg.answer("Количество шагов изменено")

@dp.message(Command("param_negative"))
async def any_message(msg: types.Message):

    global negative_prompt
    negative_prompt = str(msg.text[16:])
    await msg.answer("Негативный промпт изменен")

@dp.message(Command("param_height")) 
async def any_message(msg: types.Message):

    global height
    height = int(msg.text[14:])
    await msg.answer("Высота изображения изменена")

@dp.message(Command("param_width"))
async def any_message(msg: types.Message):

    global width
    width = int(msg.text[13:])
    await msg.answer("Ширина изображения изменена")

@dp.message(Command("param_guide"))
async def any_message(msg: types.Message):

    global guidance_scale
    guidance_scale = int(msg.text[13:])
    await msg.answer("Стремление к промпту изменено")

# Команда для отображения актуальных гиперпараметров
@dp.message(Command("params"))
async def any_message(msg: types.Message):
    await msg.reply("--------Параметры--------")
    p = str(num_inference_steps)
    await msg.answer("Шаги: "+ p)
    p = str(negative_prompt)
    await msg.answer("Негативный промпт: "+ p)
    p = str(height)
    await msg.answer("Высота изображения: "+ p)
    p = str(width)
    await msg.answer("Ширина изображения: "+ p)
    p = str(guidance_scale)
    await msg.answer("Стремление к промпту: "+ p)

# Языковая модель
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

# Основной цикл считывания сообщений/команд
async def main() -> None:
    await dp.start_polling(bot)

# Инициализация
if __name__ == "__main__":
    # Загрузка модели изображений
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")
    # Загрузка языковой модели
    #tokenizer = Tokenizer('tokenizer/l11_regex_llama3_v0.0.2.model')
    #quantization_config = TorchAoConfig("int4_weight_only", group_size=32)
    #hf_model = LlamaForCausalLM.from_pretrained('./hf_type_model_1', quantization_config=quantization_config, torch_dtype=torch.bfloat16, device_map='cuda')

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
