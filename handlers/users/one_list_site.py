from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import start_info, whylanding, landingstart
from loader import dp


@dp.callback_query_handler(info_callback.filter(item_name="onepage"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"СОЗДАДИМ, ЗАПУСТИМ, НАСТРОИМ РЕКЛАМУ НА ВАШ ОДНОСТРАНИЧНЫЙ САЙТ LANDING PAGE, ПОД КЛЮЧ ЗА 10 ДНЕЙ\n\n"
        f"Сделаем крутой лендинг быстро и качественно⚡\n\n"
        f"Одностраничный сайт - Landing Page позволит в кратчайшие сроки протестировать спрос на товар или услугу, запустить акцию, а также получить клиентов уже в первый день запуска!"
        f"Наши лендинги отличаются высокой конверсией, продуманной маркетинговой структурой и вызывающим дизайном!",
        reply_markup=whylanding)


@dp.callback_query_handler(info_callback.filter(item_name="whyourlanding"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Преимущества наших лендингов🌸\n\n"
        f"Мы не делаем сайты, которые лежат мертвым грузом на просторах интернета!\n"
        f"Все наши сайты визитки - продающие, это позволит вам в несколько раз увеличить количество заявок и клиентов.\n\n"
        f"Мы предлагаем: \n"
        f"➖ Качественная адаптация под смартфоны\n"
        f"➖ Полноценная система управления ModX вместо конструктора\n"
        f"➖ Вёрстка на Bootstrap 4 вместо конструктора Tilda\n"
        f"➖ Высокое качество изображений и контента\n"
        f"➖ Всегда соблюдаем сроки сдачи проекта\n"
        f"➖ Штатный маркетолог для написания текстов\n"
        f"➖ Сразу настраиваем цели для рекламы в метрике\n"
        f"➖ Высокая скорость загрузки\n",
        reply_markup=landingstart)


@dp.callback_query_handler(info_callback.filter(item_name="landingstartinfo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Как создать классный лендинг за 7 шагов🌚\n \n"
                              f"1) Заполнение брифа на разработку лендинга\n"
                              f"2) Составление минимального технического задания\n"
                              f"3) Утверждение бюджета и заключение договора\n"
                              f"4) Отрисовка и утверждение дизайна\n"
                              f"5) Верстка, программирование и наполнение макета\n"
                              f"6) Перенос макета в систему управления ModX\n"
                              f"7) Сдача Landing Page через 10-15 дней\n\n"
                              f"Больше информации и примеры работ на нашем сайте: https://selection-studio.com/landing-page.html\n\n "
                              f"Если хотите пообщаться с оператором, введите команду /support_call\n "
                              ,
                              reply_markup=start_info)
