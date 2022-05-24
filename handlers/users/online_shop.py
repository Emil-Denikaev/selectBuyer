from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import whyoursite, shopstart, start_info
from loader import dp


@dp.callback_query_handler(info_callback.filter(item_name="onlineshop"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Мы создадим интернет-магазин который будет продавать💰\n\n"
        f"Одним из основных направлений деятельности нашей веб-студии является создание интернет-магазинов под ключ.\n"
        f"Стоимость разработки, или цена на интернет-магазин, будет зависеть от технического задания и пожеланий заказчика при его создании."
        f"Также на цену влияет функционал, который будет разработан для вашего проекта, с учётом ваших пожеланий и потребностей посетителей будущего сайта.",
        reply_markup=whyoursite)


@dp.callback_query_handler(info_callback.filter(item_name="whyshop"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Закажите интернет-магазин У НАС, потому что\n\n"
        f"Мы способны реализовать абсолютно любой функционал, любую идею, которые необходимы для работы как маленького, так и большого интернет-магазина."
        f"От синхронизации с 1С до мультивалютности, мультиязычности и личного кабинета покупателя."
        f"Ваши посетители останутся довольны вашим сайтом!\n\n"
        f"Мы предлагаем: \n"
        f"➖ 2 отличные системы на выбор 1С Битрикс и ModX\n"
        f"➖ Уникальный, детально проработанный дизайн\n"
        f"➖ Качественная адаптация под все устройства\n"
        f"➖ Лучшие модули для интернет-магазина\n"
        f"➖ Удобное администрирование заказов\n"
        f"➖ Высокая скорость загрузки и работы сайта\n"
        f"➖ Профессиональный подход ко всем этапам создания сайта\n"
        f"➖ Всегда соблюдаем сроки разработки интернет-магазинов\n",
        reply_markup=shopstart)


@dp.callback_query_handler(info_callback.filter(item_name="shopstartinfo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Как создать классный интернет магазин за 8 шагов🌚\n \n"
                              f"1) Заполнение брифа на создание сайта\n"
                              f"2) Изучение ТЗ или помощь в его написании\n"
                              f"3) Прогнозирование и утверждение бюджета\n"
                              f"4) Отрисовка и утверждение будущего дизайна\n"
                              f"5) Верстка и программирование сайта\n"
                              f"6) Интеграция с 1С и настройка онлайн оплаты\n"
                              f"7) Тестирование и поиск ошибок в работе сайта\n"
                              f"8) Сдача и запуск вашего интернет-магазина\n\n "
                              f"Больше информации и примеры работ на нашем сайте: https://selection-studio.com/sozdanie-internet-magazina.html\n\n "
                              f"Если хотите пообщаться с оператором, введите команду /support_call\n "
                              ,
                              reply_markup=start_info)
