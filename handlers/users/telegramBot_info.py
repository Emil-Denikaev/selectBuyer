from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import botInfo, technology, cost, examples, connect
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(info_callback.filter(item_name="develop"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Чат-бот — это автоматизированный многофункциональный помощник, который может показывать информацию подписчикам и собирать информацию по запросу согласно заранее подготовленным сценариям. \n\n"
        f"Основные преимущества чат-ботов: \n"
        f"⏰ Мгновенные ответы на сообщения  \n"
        f"🌎 Доступность с любых устройств по всему миру  \n"
        f"🌚 Конфиденциальность сообщений  \n"
        f"💰 Автоматизация всех процессов, в том числе оплаты ",
        reply_markup=technology)


@dp.callback_query_handler(info_callback.filter(item_name="botPluses"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(

        reply_markup=technology)


@dp.callback_query_handler(info_callback.filter(item_name="techno"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Существуют готовые конструкторы для создания ботов, но их эффективность оставляет желать лучшего ⚠ \n\n"
        f"Наша команда подходит индивидуально к каждому проекту, подбирая технологии под конкретные задачи и НЕ работает с готовыми решениями ❌\n\n"
        f"Чаще всего в процессе разработки мы используем Python - один из самых популярных и востребованных языков в мире \n"
        f"Используем библиотеку aiogram для работы с действительно большими проектами, так как верим, что с помощью наших ботов Вы сможете в разы увеличить количество продаж или вовлеченность аудитории 💯 \n\n"
        f"Именно поэтому, даже если Ваш проект не самый большой, мы заранее подготавливаем почту для дальнейшего роста, так как уверены что телеграм боты необхоимо даже для маленьких компаний 🗿 \n\n"
        f"В результате наши продукты будут просты в поддержке и использовании, а также на долгое время останутся актуальными ‼️\n"
        ,
        reply_markup=examples)


@dp.callback_query_handler(info_callback.filter(item_name="examples"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"⚡️Бот для оптимизации продаж \n"
        f"⚡️Для рассылки сообщений \n"
        f"⚡️Учета доходов, расходов и аналитики \n"
        f"⚡️Добавление в группу/беседу и практически все, что может прийти в голову",
        reply_markup=cost)


@dp.callback_query_handler(info_callback.filter(item_name="price"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Стоимость разработки Telegram бота от 23.990 рублей. \n"
        f"Все будет зависеть от сложности и сроков, в которые необходимо выполнить. \n"
        f"Эта цена окупит себя уже через несколько месяцев, так как оптимизирует работу менеджеров, администраторов, бухгалтеров и других.",
        reply_markup=connect)


@dp.callback_query_handler(info_callback.filter(item_name="promo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Введите промокод:")
