from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import cost, addstart, whyadd, whysupportsite, supportsitestart
from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import start_info, promotestart, whypromote
from loader import dp


@dp.callback_query_handler(info_callback.filter(item_name="supportsite"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Поддержка и сопровождение сайтов на Битриксе и Modx⚡\n\n"
        f"ПОДДЕРЖКА САЙТОВ НА СИСТЕМАХ: 1С БИТРИКС И MODX. РЕШИМ ВСЕ ПОСТАВЛЕННЫЕ ЗАДАЧИ ПО ПОДДЕРЖКЕ И СОПРОВОЖДЕНИЮ ВАШЕГО САЙТА🎈\n\n"
        f"Качественная техническая поддержка сайта."
        f"Чтобы сайт всегда был доступен для посетителей, в нём работал весь заложенный при разработке функционал."
        f"Чтобы поисковые системы положительно относились к вашему сайту при его продвижении, должна оказываться своевременная техническая поддержка.",
        reply_markup=whysupportsite)


@dp.callback_query_handler(info_callback.filter(item_name="whyoursupportsite"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Только лучшие и опытные специалисты📌\n\n"
        f"Представьте, что в один прекрасный момент на вашем сайте перестал работать какой-либо функционал, или на сайт проник вирус."
        f"А написанием нового контента вообще никто не занимается. Такие сайты быстро погружаются в мир 'мертвых', никому не нужных сайтов.\n\n"
        f"Мы предлагаем: \n"
        f"➖ Всегда доступны по телефону или почте\n"
        f"➖ Штатный копирайтер, который напишет новый контент\n"
        f"➖ Молниеносная реакция на ошибки и поломки сайта\n"
        f"➖ Поддержка интернет-магазинов\n"
        f"➖ Поддержка корпоративного сайта компании\n"
        f"➖ Выполняем любые работы которые вам необходимы\n"
        f"➖ Ежемесячные отчеты о проделанной работе\n",
        reply_markup=supportsitestart)


@dp.callback_query_handler(info_callback.filter(item_name="supportsitestartinfo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Возможные работы при поддержке сайта🌚\n \n"
                              f"Прежде чем приступить к поддержке вашего сайта, мы заранее обговариваем все работы которые будут применимы к Вашему сайту.\n\n"
                              f"1) Заключение договора на поддержку сайта\n"
                              f"2) Определение перечня работ на период поддержки\n"
                              f"3) Исправление накопившихся ошибок на сайте\n"
                              f"4) Обработка и подготовка новых изображений\n"
                              f"5) Написание и публикация нового контента\n"
                              f"6) Работа с каталогом товаров/услуг\n\n"
                              f"Больше информации и примеры работ на нашем сайте: https://selection-studio.com/podderzhka-sajtov.html\n\n "
                              f"Если хотите пообщаться с оператором, введите команду /support_call\n "
                              ,
                              reply_markup=start_info)
