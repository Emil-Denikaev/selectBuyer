from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.choice_buttons import start_info
from loader import dp, bot
from app import BotDB


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if (not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
    await bot.send_photo(chat_id=message.chat.id, photo=open("photos/robot_photo.png", "rb"), caption=(
        f"Привет, {message.from_user.full_name}! \n"
        f"Спасибо, что установили именно наш чат-бот❤\n \n"
        f"Мы cоздаем продукт, помогающий развивать бизнес: \n\n"
        f"➖ В основе нашего подхода — глубокий анализ каждого проекта. \n"
        f"➖ Мы изучаем компанию и потребности бизнес-задач наших клиентов. \n"
        f"➖ Прогнозируем результаты и прибыль клиентов еще на старте сотрудничества. \n"
        f"➖ Решаем задачи продвижения бизнеса в интернете. Помогаем выстраивать успешные коммуникации с потребителями и партнерами в digital-среде.\n"
        f"➖ В зависимости от ваших потребностей можем реализовать стратегию продвижения с нуля или выполнить отдельные работы в рамках уже утвержденной стратегии. \n\n"
        f"У нас ты сможешь узнать подробнее о разрабке сайтов и создании ботов🤖"))

    await message.answer(text="Какая отрасль интересна?",
                         reply_markup=start_info)
