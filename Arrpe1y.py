import asyncio
import aiogram
import random
from aiogram import types
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile,URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot=Bot(token ='7944744667:AAGBGdep93Wzu_LJ29rFZiIm7x4ltDDT9EY')
dp=Dispatcher()
router=Router()
expressions = ["Да, возможно сегодня не самый твой удачный день, да, возможно таких дней будет ещё много. Но если бы все дни были чудесными, то можно было бы назвать это жизнью? Неудачи случаются и это нормально. Именно поэтому то, что у нас есть сейчас, очень ценно. Да и после крупных неудач, победы кажется ещё слаще) Не бывает радуги без дождя! Все поступки, все исходы, все победы и все неудачи-это наш собственный опыт, который обязательно пригодится нам. Ничего не бывает просто так, главное продолжай верить в себя и стремись к лучшему!"  , "Знай, что ты самое яркое солнышко! Ты согреваешь своим присутствием даже проходящих мимо людей. Ты как глоток свежего воздуха после дня в душной комнате, ты как горячий чай после прогулки на морозе, ты как выходной, после сложной рабочей недели. Я очень рада, что ты есть в этом мире, спасибо тебе большое", "Никогда ничего не упущено. Поезда приходят и уходят каждые несколько минут, так и с жизнью. Если ищешь возможность, то всегда её найдешь. Пусть твой сердце пылает, а ум будет ясен. Иди к своей мечте, ищи своё призвание, ошибайся, находи верный ответ, протаптывай одну и ту же дорогу бесконечное количество раз, если это потребуется. Главное иди", "Ты любим. Пусть эти слова станут для тебя опорой, в столь нелегкий этап жизни.", "Ты всегда можешь на меня положиться, пиши, звони, заглядывай, если чувствуешь, что хочешь этого. Я буду ждать"]
images=["love.jpg","1.jpg","2.jpg"]
@router.message(Command('start'))
@router.message(F.text.lower() == "вернуться назад")
async def send_welcome(message: Message):
    kb=[
        [
            types.KeyboardButton(text='Эмоции'),
            types.KeyboardButton(text='Тык'),
            types.KeyboardButton(text='Подкасты'),
            types.KeyboardButton(text='Литература'),
            types.KeyboardButton(text='Поддержка')
        ],
    ]
    keyboard=types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Привет! Я персональный помощник по определению и контролю твоих эмоций, вот что я умею <3", reply_markup=keyboard)

@router.message(F.text.lower() == "поддержка")
async def random_expression(message: types.Message):
    expression = random.choice(expressions)
    await message.answer(expression)

@router.message(F.text.lower() == "тык")
async def random_expression(message: types.Message):
    file_path = random.choice(images)
    photo = FSInputFile(file_path)
    await message.answer_photo(photo)

@router.message(F.text.lower() == "подкасты")
async def random_expression(message: types.Message):
    await send_audio(message)
async def send_audio(message: types.Message):
    audio1 = FSInputFile('podcast.mp3', 'Как помочь себе?')
    audio2 = FSInputFile('21.mp3', 'Делай это в течение 21 дня')
    audio3 = FSInputFile('Выгорание.mp3', 'Выгорание')
    await message.answer_audio(audio1, caption="подкаст")
    await message.answer_audio(audio2, caption="подкаст")
    await message.answer_audio(audio3, caption="подкаст")


@router.message(F.text.lower() == "литература")
async def send_help(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Е.Е Соколова "Введение в психологию"',
        url="https://docs.yandex.ru/docs/view?tm=1729453669&tld=ru&lang=ru&name=Sokolova_Vvedenie.pdf&text=соколова%20введение%20в%20психологию&url=https%3A%2F%2Fwww.ebbinghaus.ru%2Fwp-content%2Fuploads%2F2015%2F01%2FSokolova_Vvedenie.pdf&lr=214&mime=pdf&l10n=ru&sign=2880a77ac1698e4468c1906006e72060&keyno=0&nosw=1&serpParams=tm%3D1729453669%26tld%3Dru%26lang%3Dru%26name%3DSokolova_Vvedenie.pdf%26text%3D%25D1%2581%25D0%25BE%25D0%25BA%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25B2%25D0%25B0%2B%25D0%25B2%25D0%25B2%25D0%25B5%25D0%25B4%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5%2B%25D0%25B2%2B%25D0%25BF%25D1%2581%25D0%25B8%25D1%2585%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25B3%25D0%25B8%25D1%258E%26url%3Dhttps%253A%2F%2Fwww.ebbinghaus.ru%2Fwp-content%2Fuploads%2F2015%2F01%2FSokolova_Vvedenie.pdf%26lr%3D214%26mime%3Dpdf%26l10n%3Dru%26sign%3D2880a77ac1698e4468c1906006e72060%26keyno%3D0%26nosw%3D1"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Ю.Гиппенрейтер "Введение в общую психологию: курс лекций"',
        url="https://docs.yandex.ru/docs/view?tm=1729453730&tld=ru&lang=ru&name=Ю.Б.%20Гиппенрейтер%20Введение%20в%20общую%20психологию.pdf&text=гиппенрейтер%20введение%20в%20общую%20психологию&url=https%3A%2F%2Fwww.eduportal44.ru%2FKostroma_EDU%2Fkos_mdou_27%2FSiteAssets%2FSitePages%2F%25D0%25B1%25D0%25B8%25D0%25B1%25D0%25BB%25D0%25B8%25D0%25BE%25D1%2582%25D0%25B5%25D0%25BA%25D0%25B0%2520%25D0%25BF%25D1%2581%25D0%25B8%25D1%2585%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25B3%25D0%25B0%2F%25D0%25AE.%25D0%2591.%2520%25D0%2593%25D0%25B8%25D0%25BF%25D0%25BF%25D0%25B5%25D0%25BD%25D1%2580%25D0%25B5%25D0%25B9%25D1%2582%25D0%25B5%25D1%2580%2520%25D0%2592%25D0%25B2%25D0%25B5%25D0%25B4%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5%2520%25D0%25B2%2520%25D0%25BE%25D0%25B1%25D1%2589%25D1%2583%25D1%258E%2520%25D0%25BF%25D1%2581%25D0%25B8%25D1%2585%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25B3%25D0%25B8%25D1%258E.pdf&lr=214&mime=pdf&l10n=ru&sign=b40af05891226d94647ffc37c4fe2f9b&keyno=0&nosw=1&serpParams=tm%3D1729453730%26tld%3Dru%26lang%3Dru%26name%3D%25D0%25AE.%25D0%2591.%2520%25D0%2593%25D0%25B8%25D0%25BF%25D0%25BF%25D0%25B5%25D0%25BD%25D1%2580%25D0%25B5%25D0%25B9%25D1%2582%25D0%25B5%25D1%2580%2520%25D0%2592%25D0%25B2%25D0%25B5%25D0%25B4%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5%2520%25D0%25B2%2520%25D0%25BE%25D0%25B1%25D1%2589%25D1%2583%25D1%258E%2520%25D0%25BF%25D1%2581%25D0%25B8%25D1%2585%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25B3%25D0%25B8%25D1%258E.pdf%26text%3D%25D0%25B3%25D0%25B8%25D0%25BF%25D0%25BF%25D0%25B5%25D0%25BD%25D1%2580%25D0%25B5%25D0%25B9%25D1%2582%25D0%25B5%25D1%2580%2B%25D0%25B2%25D0%25B2%25D0%25B5%25D0%25B4%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5%2B%25D0%25B2%2B%25D0%25BE%25D0%25B1%25D1%2589%25D1%2583%25D1%258E%2B%25D0%25BF%25D1%2581%25D0%25B8%25D1%2585%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25B3%25D0%25B8%25D1%258E%26url%3Dhttps%253A%2F%2Fwww.eduportal44.ru%2FKostroma_EDU%2Fkos_mdou_27%2FSiteAssets%2FSitePages%2F%2525D0%2525B1%2525D0%2525B8%2525D0%2525B1%2525D0%2525BB%2525D0%2525B8%2525D0%2525BE%2525D1%252582%2525D0%2525B5%2525D0%2525BA%2525D0%2525B0%252520%2525D0%2525BF%2525D1%252581%2525D0%2525B8%2525D1%252585%2525D0%2525BE%2525D0%2525BB%2525D0%2525BE%2525D0%2525B3%2525D0%2525B0%2F%2525D0%2525AE.%2525D0%252591.%252520%2525D0%252593%2525D0%2525B8%2525D0%2525BF%2525D0%2525BF%2525D0%2525B5%2525D0%2525BD%2525D1%252580%2525D0%2525B5%2525D0%2525B9%2525D1%252582%2525D0%2525B5%2525D1%252580%252520%2525D0%252592%2525D0%2525B2%2525D0%2525B5%2525D0%2525B4%2525D0%2525B5%2525D0%2525BD%2525D0%2525B8%2525D0%2525B5%252520%2525D0%2525B2%252520%2525D0%2525BE%2525D0%2525B1%2525D1%252589%2525D1%252583%2525D1%25258E%252520%2525D0%2525BF%2525D1%252581%2525D0%2525B8%2525D1%252585%2525D0%2525BE%2525D0%2525BB%2525D0%2525BE%2525D0%2525B3%2525D0%2525B8%2525D1%25258E.pdf%26lr%3D214%26mime%3Dpdf%26l10n%3Dru%26sign%3Db40af05891226d94647ffc37c4fe2f9b%26keyno%3D0%26nosw%3D1"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Л.С.Выготский А.Р. Лурия "Этюды по истории поведения"',
        url="https://docs.yandex.ru/docs/view?tm=1729453851&tld=ru&lang=ru&name=0_publication_123_1.pdf&text=выготский%20лурия%20этюды%20по%20истории%20поведения&url=http%3A%2F%2Feureka.international%2Fres_ru%2F0_publication_123_1.pdf&lr=214&mime=pdf&l10n=ru&sign=0f5447e489cbffde256d3f9844e59bde&keyno=0&nosw=1&serpParams=tm%3D1729453851%26tld%3Dru%26lang%3Dru%26name%3D0_publication_123_1.pdf%26text%3D%25D0%25B2%25D1%258B%25D0%25B3%25D0%25BE%25D1%2582%25D1%2581%25D0%25BA%25D0%25B8%25D0%25B9%2B%25D0%25BB%25D1%2583%25D1%2580%25D0%25B8%25D1%258F%2B%25D1%258D%25D1%2582%25D1%258E%25D0%25B4%25D1%258B%2B%25D0%25BF%25D0%25BE%2B%25D0%25B8%25D1%2581%25D1%2582%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B8%2B%25D0%25BF%25D0%25BE%25D0%25B2%25D0%25B5%25D0%25B4%25D0%25B5%25D0%25BD%25D0%25B8%25D1%258F%26url%3Dhttp%253A%2F%2Feureka.international%2Fres_ru%2F0_publication_123_1.pdf%26lr%3D214%26mime%3Dpdf%26l10n%3Dru%26sign%3D0f5447e489cbffde256d3f9844e59bde%26keyno%3D0%26nosw%3D1"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Общий файл со всеми произведениями',
        url="https://disk.yandex.ru/d/N8eD6rNXvUMrLA/Литература"
    ))
    await message.answer("Эта литература поможет тебе в усвоении психологии. Вперед, солнце! ", reply_markup=builder.as_markup())

@router.message(F.text.lower() == "эмоции")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text='Грусть'),
            types.KeyboardButton(text='Наслаждение'),
            types.KeyboardButton(text='Гнев'),
            types.KeyboardButton(text='Удивление'),
            types.KeyboardButton(text='Страх'),
            types.KeyboardButton(text='Отвращение')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Что ты сейчас чувствуешь?", reply_markup=keyboard)

@router.message(F.text.lower() == "грусть")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text="чувство вины"),
            types.KeyboardButton(text="тревога"),
            types.KeyboardButton(text="ненависть к себе"),
            types.KeyboardButton(text="подавленность"),
            types.KeyboardButton(text="скучание по человеку"),
            types.KeyboardButton(text="вернуться назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Какую именно эмоцию ты испытываешь?", reply_markup=keyboard)

@router.message(F.text.lower() == 'чувство вины')
async def re_text1(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", чувство вины — это негативное эмоциональное состояние, вызванное осознанием того, что человек совершил что-то, противоречащее его личным моральным убеждениям или социальным нормам. Оно связано с самообвинением и переживанием из-за реального или воображаемого нарушения. Чувство вины может стимулировать человека к исправлению ошибок и восстановлению социальных связей. Однако в избыточной форме может привести к хроническому стрессу и психологическим проблемам. Такая вина будет уже токсичной. Чтобы избавиться от чувства вины стоит попробовать признать свою вину, разобраться с причиной возникновения этой эмоции, простить себя. Солнце, у тебя всё получится, я в тебя верю")
@router.message(F.text.lower() == 'тревога')
async def re_text1(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", тревога — это эмоциональное состояние, которое характеризуется внутренним беспокойством, неопределённостью и ощущением опасности. Она представляет собой расплывчатый, длительный и смутный страх по поводу будущих событий. Возникает в ситуациях, когда ещё нет реальной опасности для человека, но он ждёт её, причём пока неясно представляет, как с ней справиться. Тревога может быть нормальной реакцией на вызовы повседневной жизни, но когда она становится чрезмерной и мешает нормальному функционированию, то в этом случае может рассматриваться как тревожное расстройство. Как справиться с тревогой? Попробуй обсудить свои страхи с близким человеком, изложи свои мысли на бумаге, не седи без дела, не зацикливайся на прошлом. Солнышко, давай вместе глубоко вдохнём и выдохнем")
@router.message(F.text.lower() == 'ненависть к себе')
async def re_text1(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", ненависть к себе — это крайняя критика самого себя, чувство, которое носит более яркий негативный оттенок, чем низкая самооценка или недостаток уверенности в себе. На глубинном уровне это убеждение, что человек «плохой», «недостойный», «таким быть нельзя», «отвратительный или ущербный в своей сути», «во мне нет ценности» и это обязательно узнают другие. Некоторые советы, которые могут помочь справиться с этим чувством: проанализируй отношение к себе, признай, что человек не идеален, проведи инвентаризацию сильных сторон, практикуй прощение. Солнышко, ненависть к себе никак не пойдет к тебе напользу, я уверена, что ты очень хороший человек, иначе и быть не может! Пожалуйста, люби и береги себя")
@router.message(F.text.lower() == 'подавленность')
async def re_text1(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", подавленность — это эмоциональное состояние, которое характеризуется пониженным настроением, утратой интереса к окружающему миру, снижением активности и энергии. Несколько советов как избавиться от подавленности: признать свои эмоции, выразить эмоции, забоиться о своём теле, найти время для удовольствия, отнестись к себе с терпением и пониманием, обратиться за поддрежкой")
@router.message(F.text.lower() == 'скучание по человеку')
async def re_text1(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", чувство скучания по человеку — это сложный процесс, который включает в себя физиологические, эмоциональные и социальные аспекты. Когда мы устанавливаем близкие отношения с кем-то, возникает эмоциональная привязанность. Этот вид связи даёт нам чувство безопасности, уюта и понимания. Потеря этих связей может вызвать глубокие эмоциональные травмы, поскольку привычные источники поддержки и радости иссякают. Нередко мы тоскуем не по самому человеку, а по тем моментам, которые с ним связаны. Например, счастливые студенческие годы, путешествия, совместные вечеринки и общие увлечения. Скука по людям также связана с ощущением одиночества. Даже если в нашей жизни есть другие люди, отсутствие тех, кто значит для нас особенно много, может вызвать чувство пустоты и одиночества. Я понимаю, как порой тяжело не видеть человека неделями, месяцами, а может даже и годами. То, что вы скучаете по кому-то-совершенно нормально. Мы живем, а значит мы ощущаем. Солнце, главное помни, что не один. Всё будет так, как надо")

@router.message(F.text.lower() == "страх")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text="паника"),
            types.KeyboardButton(text="ужас"),
            types.KeyboardButton(text="тревога"),
            types.KeyboardButton(text="вернуться назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Какую именно эмоцию ты испытываешь?", reply_markup=keyboard)

@router.message(F.text.lower() == 'тревога')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", тревога — это эмоциональное состояние, которое характеризуется внутренним беспокойством, неопределённостью и ощущением опасности. Она представляет собой расплывчатый, длительный и смутный страх по поводу будущих событий. Возникает в ситуациях, когда ещё нет реальной опасности для человека, но он ждёт её, причём пока неясно представляет, как с ней справиться. Тревога может быть нормальной реакцией на вызовы повседневной жизни, но когда она становится чрезмерной и мешает нормальному функционированию, то в этом случае может рассматриваться как тревожное расстройство. Как справиться с тревогой? Попробуй обсудить свои страхи с близким человеком, изложи свои мысли на бумаге, не седи без дела, не зацикливайся на прошлом. Солнышко, давай вместе глубоко вдохнём и выдохнем")
@router.message(F.text.lower() == 'паника')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", паника — это негативно окрашенное эмоциональное состояние крайнего страха, ужаса, дезориентирующее и не поддающееся сознательному контролю. Она возникает как реакция на нечто необычное, пугающее, к чему человек абсолютно не готов. Ощущение ужаса настолько сильно, что заслоняет собой всё, не давая мыслить логически. Разум отключается, и включаются животные инстинкты: «бей, беги, замри» Если приступ страха возникает спонтанно, либо повторяется при определённых событиях, ситуациях, то подобное состояние именуется в психиатрии «панические атаки». Они возникают внезапно, сопровождаются тяжёлыми физическими проявлениями: сердцебиение, удушье, головокружение, слабость. Как справиться с паникой: нормализовать дыхание. активизировать органы чувств,контролировать движение и тело, переключить внимание на внешнюю среду")
@router.message(F.text.lower() == 'ужас')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", ужас — состояние человека под влиянием сильного страха (испуга), отличительной чертой которого является подавленность (оцепенение), иногда дрожь, в общем, отсутствие активной реакции по устранению источника страха. Как справиться с ужасом? Оцени ситуацию, создай ощущение физического комфорта, вознагради себя за дальнейшую смелость")

@router.message(F.text.lower() == "гнев")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text="раздражение"),
            types.KeyboardButton(text="презрение"),
            types.KeyboardButton(text="ненависть"),
            types.KeyboardButton(text="вернуться назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Какую именно эмоцию ты испытываешь?", reply_markup=keyboard)

@router.message(F.text.lower() == 'раздражение')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", в психологии раздражение — это эмоция, которая возникает в результате столкновения с чем-то неприятным и неожиданным для человека. Оно возникает, когда в жизни что-то идёт не так, как хочется, когда человек не может контролировать ситуацию или других людей, и это мешает достижению его целей.")
@router.message(F.text.lower() == 'презрение')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", презрение — это базовая эмоция, которая выражает отрицательное отношение к другому человеку или объекту, рассматривая его как недостойного уважения. Оно часто сопровождается чувством превосходства и презрительного отношения к тому, на кого направлена эта эмоция. Презрение может возникать в ответ на поведение или характеристики другого человека, которые считаются нежелательными, морально неправильными, низкими или недостойными.")
@router.message(F.text.lower() == 'ненависть')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", ненависть — интенсивное, отрицательно окрашенное деструктивное чувство, отражающее неприятие, отвращение и враждебность к объекту ненависти (человеку, группе лиц, неодушевлённому предмету, явлению). Ненависть может вызываться как какими-либо действиями объекта, так и присущими ему качествами. Она может связываться с желанием зла и намерением причинить вред объекту эмоции. Как бороться с чувством ненависти: понять, что ненависть разрушит вас самого, не держать ненависть, а отпустить её, прекратить общение с объектом ненависти,выплескивать ненависть физически через спорт")

@router.message(F.text.lower() == "наслаждение")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text="радость"),
            types.KeyboardButton(text="благодарность"),
            types.KeyboardButton(text="сексуальное удовольствие"),
            types.KeyboardButton(text="преданность"),
            types.KeyboardButton(text="доверие"),
            types.KeyboardButton(text="вернуться назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Какую именно эмоцию ты испытываешь?", reply_markup=keyboard)


@router.message(F.text.lower() == 'радость')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", радость — состояние удовлетворения, удовольствия, весёлого настроения и счастья. Это одна из основных положительных эмоций человека, которая является положительной внутренней мотивацией. Аж самой хорошо на душе стало, что ты испытываешь столь восхитительные эмоции <3")
@router.message(F.text.lower() == 'благодарность')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", благодарность — чувство признательности за совершённое добро (это может быть внимание, действие, подарок). Это эмоция, которую можно испытывать не только к конкретным людям, но и к событиям, миру и жизни в целом.")
@router.message(F.text.lower() == 'сексуальное удовольствие')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", сексуальное удовольствие — это спектр ощущений, которые начинаются с интереса, желания, эротической любви, страсти, оргазма и экстаза. Также сексуальное удовольствие может рассматриваться как состояние полной расслабленности и доверия своему телу во время полового акта. Важно помнить, что понятие сексуального удовольствия индивидуально и может отличаться у разных людей.")
@router.message(F.text.lower() == 'преданность')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", преданность — это глубокое чувство привязанности, лояльности, приверженности, предпочтения к человеку, идее или ценностям. Это означает, что человек готов отдать свои силы, время или ресурсы во имя этой привязанности. Преданность подразумевает полное отсутствие измены, искреннее побуждение следовать и поддерживать определённые принципы или отношения в течение длительного времени. Преданный человек готов пожертвовать своими интересами или желаниями ради тех, кому он предан.")
@router.message(F.text.lower() == 'доверие')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", доверие — это чувство или субъективная убеждённость в том, что в тех или иных отношениях человек получит поддержку, честность, искренность, принятие. Поведение того, кому доверяют, в какой-то степени становится для доверяющего предсказуемым. Он верит, что человек выполнит обещание, будет соблюдать договорённости, не предаст и не подведёт. В результате доверяющий получает базовую безопасность, которая помогает уверенно идти вперёд, сводя к минимуму сложные чувства тревоги и страха.")

@router.message(F.text.lower() == "удивление")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text="изумление"),
            types.KeyboardButton(text="сомнение"),
            types.KeyboardButton(text="недоумение"),
            types.KeyboardButton(text="непосредственно удивление"),
            types.KeyboardButton(text="вернуться назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Какую именно эмоцию ты испытываешь?", reply_markup=keyboard)

@router.message(F.text.lower() == 'сомнение')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", сомнение-это неуверенность в истинности, возможности чего-либо, отсуствие твердой веры в кого-либо или что-либо, опасание,, подозрение, колебание, затруднение, неясность, возникающие при разрешении какого-либо вопроса")
@router.message(F.text.lower() == 'изумление')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", изумление — это очень большое удивление, состояние поражённости чем-то неожиданным, необычным. Проявления изумления во многом совпадают с проявлениями удивления.")
@router.message(F.text.lower() == 'недоумение')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", недоумение — это состояние нерешимости, сомнение, колебание вследствие непонимания, неясности.")
@router.message(F.text.lower() == 'непосредственно удивление')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", удивление — это внезапная эмоциональная реакция на неожиданное событие или информацию, которая прерывает текущее состояние и привлекает внимание к новому стимулу. Оно возникает мгновенно и может привести к целому ряду реакций, таких как страх, радость, облегчение, гнев, отвращение и многое другое — в зависимости от ситуации. Вызвать удивление могут самые разные внешние факторы: неожиданные звуки, внезапные изменения в процессе, неожиданные действия других людей или удивительные новости. Удивление играет важную роль в обучении и адаптации, помогает обратить внимание на новые аспекты окружающего мира. Оно стимулирует любознательность и интерес, способствует когнитивному развитию, креативности.")

@router.message(F.text.lower() == "отвращение")
async def all_sad(message:Message):
    kb = [
        [
            types.KeyboardButton(text="к патогенам"),
            types.KeyboardButton(text="сексуальное отвращение"),
            types.KeyboardButton(text="моральное"),
            types.KeyboardButton(text="вернуться назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard = True
    )
    await message.answer("Какую именно эмоцию ты испытываешь?", reply_markup=keyboard)

@router.message(F.text.lower() == 'к патогенам')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", отвращение к патогенам — это защитный механизм, который заставляет человека избегать контакта с болезнетворными микроорганизмами, больными, увечными и бродягами, некоторыми животными — переносчиками заболеваний, продуктами жизнедеятельности организма и телесными жидкостями. Отвращение инициирует и физиологические иммунные реакции — чтобы подготовить организм к потенциальной инфекции.")
@router.message(F.text.lower() == 'сексуальное отвращение')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", сексуальное отвращение (сексуальная аверсия) — это состояние, при котором человек испытывает сильное нежелание или антипатию к сексуальным актам или интимным контактам. Проявляется в стойком и длительном отсутствии интереса к сексу или чувством дискомфорта и антипатии при попытках сексуальной близости. Некоторые причины сексуальное аверсии: травмы или нарушения в прошлом, конфликты в отношениях, медицинские причины, психологические факторы, культурные и религиозные факторы, негативный опыт сексуальных отношений")
@router.message(F.text.lower() == 'моральное')
async def re_text2(message: Message):
    username=message.from_user.first_name
    await message.answer(username +", моральное отвращение- это реакция на более абстрактные предметы или на людей, нарушающих моральные и общественные нормы, например, лживых политиков, продажных чиновников. Эмоция отвращения — это отрицательно окрашенное чувство, проявления сильной формы неприятия. Оно является важным защитником человеческих границ")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
