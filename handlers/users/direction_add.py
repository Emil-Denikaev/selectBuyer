from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import cost, addstart, whyadd
from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import start_info, promotestart, whypromote
from loader import dp


@dp.callback_query_handler(info_callback.filter(item_name="add"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Настройка и ведение рекламы Яндекс Директ📊\n\n"
        f"ПРОФЕССИОНАЛЬНЫЙ ПОДХОД К НАСТРОЙКЕ КОНТЕКСТНОЙ РЕКЛАМЫ ЯНДЕКС ДИРЕКТ ОТ СЕРТИФИЦИРОВАННОГО ЯНДЕКСОМ РЕКЛАМНОГО АГЕНСТВА⚡\n\n"
        f"Контекстная реклама Яндекс Директ, при грамотной настройке и ведении, позволят получить целевые заявки с вашего сайта уже в день запуска рекламной кампании."
        f"Очень важно заказать настройку контекстной рекламы у грамотных и опытных специалистов."
        f"От этого будут зависеть затраты на рекламу и успех всей вашей кампании в целом.",
        reply_markup=whyadd)


@dp.callback_query_handler(info_callback.filter(item_name="whyouradd"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Закажите настройку у нас, потому что\n\n"
        f"Наши специалисты по настройке рекламы имеют официальные сертификаты от Яндекса, что подтверждает высокий профессионализм в области маркетинга📈\n\n"
        f"Мы предлагаем: \n"
        f"➖ Профессиональный подход к ведению рекламных кампаний\n"
        f"➖ Даем рекомендации по увеличению конверсии вашего сайта\n"
        f"➖ Профессиональное составление семантического ядра в вашей нише\n"
        f"➖ Ежедневная корректировка ставок и стоимости клика\n"
        f"➖ Составляем конверсионные заголовки объявлений для высокого CTR\n"
        f"➖ Анализируем конкурентов с целью формирования стратегии\n"
        f"➖ Настройка рекламы именно под вашу целевую аудиторию\n"
        f"➖ Понятные, человеческие отчеты 1/2/4 раза в месяц\n",
        reply_markup=addstart)


@dp.callback_query_handler(info_callback.filter(item_name="addstartinfo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Наши этапы настройки рекламной кампании🌚\n \n"
                              f"Прежде чем заказать настройку Яндекс Директ в нашей студии, нам необходимо будет провести тщательный анализ конкуренции в нише и точно спрогнозировать количество кликов за данный бюджет.\n\n"
                              f"1) Проводим аудит вашего сайта для улучшения конверсии\n"
                              f"2) Настраиваем аналитику для отслеживания эффективности\n"
                              f"3) Придумываем конверсионные оферы для объявлений\n"
                              f"4) Составляем семантическое ядро и готовим рекламные объявления\n"
                              f"5) Настраиваем рекламную компанию\n"
                              f"6) Анализируем результаты, вносим корректировки\n"
                              f"7) Оптимизируем стоимость клика, корректируем ставки\n\n"
                              f"Больше информации и примеры работ на нашем сайте: https://selection-studio.com/kontekstnaya-reklama.html\n\n "
                              f"Если хотите пообщаться с оператором, введите команду /support_call\n "
                              ,
                              reply_markup=start_info)
