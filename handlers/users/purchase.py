from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback, start_callback
from keyboards.inline.choice_buttons import siteToBot, start_info, sitestart
from loader import dp, bot
from app import BotDB

SITE_LINK = "https://selection-studio.com/"


@dp.callback_query_handler(info_callback.filter(item_name="menu"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Здесь ты сможешь найти основные раздела бота☺"
        ,
        reply_markup=start_info)


@dp.callback_query_handler(info_callback.filter(item_name="site"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Крутой сайт для крутой компании🌚\n \n"
                              f"Создаем корпоративные сайты для компаний с самым продвинутым функционалом и современным дизайном🌞\n\n"
                              f"Проект будет выполнен в короткие сроки, без задержек. Протестирован на всевозможные ошибки и сдан готовым к работе на все 100%👍 ",
                              reply_markup=siteToBot)


@dp.callback_query_handler(info_callback.filter(item_name="advantages"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(
        f"При создании корпоративного сайта, также разрабатывается панель управления строго под каждый проект, на системе ModX.\n\n"
        f"В результате у вас будут только необходимые поля для каждой страницы, которые нужно будет заполнить.\n"
        f"Такой подход позволяет не иметь в штате веб-мастера для обслуживания сайта.\n"
        f"Изменить и добавить контент сможет любой ваш сотрудник\n\n"
        f"Кроме того:\n"
        f"➖ Нет ограничений на масштабирование разделов сайта в будущем\n"
        f"➖ Только уникальный контент написанный штатными копирайтерами\n"
        f"➖ Заранее все просчитываем и всегда соблюдаем сроки сдачи сайта\n"
        f"➖ Все наши сайты имеют качественную адаптацию под все устройства\n"
        f"➖ Бесплатная техническая поддержка сайта в течение 3 месяцев\n"
        f"➖ Лучшая система ModX для качественного продвижения сайта\n"
        f"➖ Молниеносная работа и загрузка вашего корпоративного сайта\n"
        f"➖ Профессиональный подход ко всем этапам создания вашего сайта",
        reply_markup=sitestart)


@dp.callback_query_handler(info_callback.filter(item_name="fromstart"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Как создать классный сайт за 8 шагов🌚\n \n"
                              f"1) Заполнение брифа на создание сайта\n"
                              f"2) Утверждение ТЗ и бюджета\n"
                              f"3) Заключение договора и внесение предоплаты\n"
                              f"4) Создание и утверждение дизайна будущего сайта\n"
                              f"5) Верстка и программирование сайта\n"
                              f"6) Наполнение сайта контентом\n"
                              f"7) Тестирование, поиск и исправление ошибок\n"
                              f"8) Запуск сайта на вашем хостинге и сдача проекта\n\n "
                              f"Больше информации и примеры работ на нашем сайте: https://selection-studio.com/sayt-dlia-kompanii.html\n\n "
                              f"Если хотите пообщаться с оператором, введите команду /support_call\n "
                              ,
                              reply_markup=start_info)


@dp.callback_query_handler(info_callback.filter(item_name="contacts"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer("Спасибо, наш представитель скоро свяжется с Вами", show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Вы отменили получение информации", show_alert=True)
    await call.message.edit_reply_markup()
