from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import start_info, promotestart, whypromote
from loader import dp


@dp.callback_query_handler(info_callback.filter(item_name="promote"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Продвижение сайтов в самых конкурентных тематиках🔥\n\n"
        f"Продвигаем сайты с гарантией результата⚡\n\n"
        f"Нашими клиентами являются компании и частные лица, успех которых связан с потоком клиентов и местом в поисковой выдаче."
        f"Их успех зависит от грамотно выбранной стратегии сео продвижения сайта.\n"
        f"Работы выполняют сео специалисты, каждый из которых обладает багажом знаний в данной сфере."
        f"Вы можете быть уверенным, что ваш сайт точно попадет в топ поиска по Вашим, желаемым ключевым фразам.",
        reply_markup=whypromote)


@dp.callback_query_handler(info_callback.filter(item_name="whyourpromote"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Доверьте продвижение своего сайта профессионалам\n\n"
        f"Мы постоянно тестируем и выявляем самые эффективные методики сео продвижения сайта, в самых популярных поисковиках России - Яндекс и Google📈\n"
        f"Мы предлагаем: \n"
        f"➖ У нас нет новичков. Все сео - специалисты имеют опыт минимум 5 лет\n"
        f"➖ Штатный копирайтер для написания уникального контента на сайт\n"
        f"➖ Проверенные методы продвижения, которые уже доказали свою эффективность\n"
        f"➖ В каждый пакет по продвижению включены работы над сайтом\n"
        f"➖ Отлаженный процесс закупки ссылочной массы для сайта\n"
        f"➖ Быстрый результат продвижения в Яндексе, 2-3 месяца\n"
        f"➖ Успешно продвигаем как молодые, так и возрастные сайты\n"
        f"➖ Подробный отчет по продвижению сайта в конце каждого месяца\n",
        reply_markup=promotestart)


@dp.callback_query_handler(info_callback.filter(item_name="promotestartinfo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"С чего начать сео продвижение сайта?🌚\n \n"
                              f"Сео продвижение это не какая то магия, есть определенный список мероприятий для успешного вывода сайта в ТОП."
                              f"Все мероприятия по продвижению делятся на этапы, соблюдая которые Вы получаете результат.\n\n"
                              f"1) Заключаем договор на продвижение ключевых фраз\n"
                              f"2) Аудит вашего текстового контента\n"
                              f"3) Аудит программного кода сайта\n"
                              f"4) Оптимизация всего контента под поиск\n"
                              f"5) Создание новых страниц и разделов, если необходимо\n"
                              f"6) Копирайтинг / рерайтинг контента под уникальность\n"
                              f"7) Работа с внешними факторами продвижения - ссылки\n"
                              f"8) Работа с поведенческими факторами, конверсией, отказами\n\n"
                              f"Больше информации и примеры работ на нашем сайте: https://selection-studio.com/prodvizhenie-saytov.html\n\n "
                              f"Если хотите пообщаться с оператором, введите команду /support_call\n "
                              ,
                              reply_markup=start_info)
