"""Multilingual OxShare referral bot handlers."""

from urllib.parse import quote

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from app.localization import LANGUAGE_NAMES, SUPPORTED_LANGUAGES, normalize_language

router = Router(name="start")

REFERRAL_URL = "https://my.oxshare.com/register?referral=019ba1ff-6ca2-70b3-9def-036b59457426"
COMMUNITY_URL = "https://t.me/ImperialEliteGoldskull"
OXSHARE_URL = "https://www.oxshare.com/"

TEXT = {
    "en": {"welcome": "🔥 Welcome! Discover OxShare and connect with the community.", "join": "🔗 Join OxShare", "community": "🖇️ Join Community", "about": "ℹ️ About OxShare", "share": "📤 Share with Friends", "language": "🌍 Language", "about_text": "Learn more about OxShare on the official website. Then use the Join button if you want to register through my referral link."},
    "ar": {"welcome": "🔥 أهلاً بك! تعرّف على OxShare وانضم إلى المجتمع.", "join": "🔗 انضم إلى OxShare", "community": "🖇️ انضم إلى المجتمع", "about": "ℹ️ عن OxShare", "share": "📤 شارك مع الأصدقاء", "language": "🌍 اللغة", "about_text": "تعرّف على OxShare عبر الموقع الرسمي، ثم استخدم زر الانضمام إذا أردت التسجيل عبر رابط الإحالة الخاص بي."},
    "fr": {"welcome": "🔥 Bienvenue ! Découvrez OxShare et rejoignez la communauté.", "join": "🔗 Rejoindre OxShare", "community": "🖇️ Rejoindre la communauté", "about": "ℹ️ À propos d’OxShare", "share": "📤 Partager", "language": "🌍 Langue", "about_text": "Découvrez OxShare sur le site officiel, puis utilisez le bouton Rejoindre si vous souhaitez vous inscrire via mon lien de parrainage."},
    "es": {"welcome": "🔥 ¡Bienvenido! Descubre OxShare y únete a la comunidad.", "join": "🔗 Unirse a OxShare", "community": "🖇️ Unirse a la comunidad", "about": "ℹ️ Sobre OxShare", "share": "📤 Compartir", "language": "🌍 Idioma", "about_text": "Conoce OxShare en el sitio oficial y usa el botón Unirse si quieres registrarte con mi enlace de referido."},
    "de": {"welcome": "🔥 Willkommen! Entdecke OxShare und tritt der Community bei.", "join": "🔗 OxShare beitreten", "community": "🖇️ Community beitreten", "about": "ℹ️ Über OxShare", "share": "📤 Teilen", "language": "🌍 Sprache", "about_text": "Mehr über OxShare findest du auf der offiziellen Website. Nutze danach den Beitreten-Button, wenn du dich über meinen Empfehlungslink registrieren möchtest."},
    "it": {"welcome": "🔥 Benvenuto! Scopri OxShare e unisciti alla community.", "join": "🔗 Unisciti a OxShare", "community": "🖇️ Unisciti alla community", "about": "ℹ️ Informazioni su OxShare", "share": "📤 Condividi", "language": "🌍 Lingua", "about_text": "Scopri OxShare sul sito ufficiale e usa il pulsante Unisciti se vuoi registrarti tramite il mio link referral."},
    "ru": {"welcome": "🔥 Добро пожаловать! Узнайте об OxShare и присоединяйтесь к сообществу.", "join": "🔗 Присоединиться к OxShare", "community": "🖇️ Войти в сообщество", "about": "ℹ️ Об OxShare", "share": "📤 Поделиться", "language": "🌍 Язык", "about_text": "Узнайте больше об OxShare на официальном сайте. Затем используйте кнопку регистрации, если хотите зарегистрироваться по моей реферальной ссылке."},
    "tr": {"welcome": "🔥 Hoş geldiniz! OxShare'i keşfedin ve topluluğa katılın.", "join": "🔗 OxShare'e Katıl", "community": "🖇️ Topluluğa Katıl", "about": "ℹ️ OxShare Hakkında", "share": "📤 Paylaş", "language": "🌍 Dil", "about_text": "OxShare hakkında resmi web sitesinden bilgi alın. Ardından tavsiye bağlantımla kayıt olmak istiyorsanız Katıl düğmesini kullanın."},
    "fa": {"welcome": "🔥 خوش آمدید! OxShare را بشناسید و به جامعه بپیوندید.", "join": "🔗 عضویت در OxShare", "community": "🖇️ عضویت در جامعه", "about": "ℹ️ درباره OxShare", "share": "📤 اشتراک‌گذاری", "language": "🌍 زبان", "about_text": "اطلاعات بیشتر درباره OxShare را در وب‌سایت رسمی ببینید و در صورت تمایل با لینک معرفی من ثبت‌نام کنید."},
    "ps": {"welcome": "🔥 ښه راغلاست! OxShare وپېژنئ او ټولنې سره یوځای شئ.", "join": "🔗 OxShare سره یوځای شئ", "community": "🖇️ ټولنې سره یوځای شئ", "about": "ℹ️ د OxShare په اړه", "share": "📤 له ملګرو سره شریکول", "language": "🌍 ژبه", "about_text": "د OxShare په اړه نور معلومات په رسمي وېب‌پاڼه کې وګورئ، او که غواړئ زما د referral لینک له لارې ثبت‌نام وکړئ."},
    "hi": {"welcome": "🔥 स्वागत है! OxShare को जानें और समुदाय से जुड़ें।", "join": "🔗 OxShare से जुड़ें", "community": "🖇️ कम्युनिटी से जुड़ें", "about": "ℹ️ OxShare के बारे में", "share": "📤 दोस्तों के साथ शेयर करें", "language": "🌍 भाषा", "about_text": "OxShare की जानकारी आधिकारिक वेबसाइट पर देखें। चाहें तो मेरे रेफरल लिंक से रजिस्टर करने के लिए Join बटन दबाएँ।"},
    "ur": {"welcome": "🔥 خوش آمدید! OxShare کو دریافت کریں اور کمیونٹی میں شامل ہوں۔", "join": "🔗 OxShare میں شامل ہوں", "community": "🖇️ کمیونٹی میں شامل ہوں", "about": "ℹ️ OxShare کے بارے میں", "share": "📤 دوستوں کے ساتھ شیئر کریں", "language": "🌍 زبان", "about_text": "OxShare کے بارے میں سرکاری ویب سائٹ پر جانیں، پھر اگر چاہیں تو میرے ریفرل لنک سے رجسٹر کریں۔"},
    "pt": {"welcome": "🔥 Bem-vindo! Conheça a OxShare e entre na comunidade.", "join": "🔗 Entrar na OxShare", "community": "🖇️ Entrar na comunidade", "about": "ℹ️ Sobre a OxShare", "share": "📤 Compartilhar", "language": "🌍 Idioma", "about_text": "Saiba mais sobre a OxShare no site oficial. Depois, use o botão Entrar se quiser se registrar pelo meu link de indicação."},
    "zh": {"welcome": "🔥 欢迎！了解 OxShare 并加入社区。", "join": "🔗 加入 OxShare", "community": "🖇️ 加入社区", "about": "ℹ️ 关于 OxShare", "share": "📤 分享给朋友", "language": "🌍 语言", "about_text": "请先在官方网站了解 OxShare，然后如需通过我的推荐链接注册，请点击加入按钮。"},
    "ja": {"welcome": "🔥 ようこそ！OxShareを確認してコミュニティに参加しましょう。", "join": "🔗 OxShareに参加", "community": "🖇️ コミュニティに参加", "about": "ℹ️ OxShareについて", "share": "📤 友達に共有", "language": "🌍 言語", "about_text": "OxShareの詳細は公式サイトで確認できます。私の紹介リンクから登録する場合は参加ボタンを押してください。"},
    "ko": {"welcome": "🔥 환영합니다! OxShare를 알아보고 커뮤니티에 참여하세요.", "join": "🔗 OxShare 가입", "community": "🖇️ 커뮤니티 참여", "about": "ℹ️ OxShare 소개", "share": "📤 친구에게 공유", "language": "🌍 언어", "about_text": "OxShare에 대한 자세한 내용은 공식 웹사이트에서 확인하세요. 제 추천 링크로 가입하려면 가입 버튼을 이용하세요."},
}


def keyboard(lang: str) -> InlineKeyboardMarkup:
    t = TEXT[lang]
    share_url = "https://t.me/share/url?url=" + quote(REFERRAL_URL) + "&text=" + quote(t["welcome"])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["join"], url=REFERRAL_URL)],
        [InlineKeyboardButton(text=t["community"], url=COMMUNITY_URL)],
        [InlineKeyboardButton(text=t["about"], callback_data=f"about:{lang}"), InlineKeyboardButton(text=t["language"], callback_data="languages")],
        [InlineKeyboardButton(text=t["share"], url=share_url)],
    ])


def language_keyboard() -> InlineKeyboardMarkup:
    rows = []
    items = list(SUPPORTED_LANGUAGES)
    for i in range(0, len(items), 2):
        rows.append([InlineKeyboardButton(text=LANGUAGE_NAMES[x], callback_data=f"lang:{x}") for x in items[i:i + 2]])
    return InlineKeyboardMarkup(inline_keyboard=rows)


async def send_home(message: Message, lang: str) -> None:
    await message.answer(TEXT[lang]["welcome"], reply_markup=keyboard(lang))


@router.message(CommandStart())
async def start(message: Message) -> None:
    lang = normalize_language(message.from_user.language_code if message.from_user else None)
    await send_home(message, lang)


@router.message(Command("help"))
async def help_command(message: Message) -> None:
    lang = normalize_language(message.from_user.language_code if message.from_user else None)
    await send_home(message, lang)


@router.callback_query(F.data == "languages")
async def languages(callback: CallbackQuery) -> None:
    await callback.message.edit_text("🌍 Choose your language:", reply_markup=language_keyboard())
    await callback.answer()


@router.callback_query(F.data.startswith("lang:"))
async def set_language(callback: CallbackQuery) -> None:
    lang = normalize_language(callback.data.split(":", 1)[1])
    await callback.message.edit_text(TEXT[lang]["welcome"], reply_markup=keyboard(lang))
    await callback.answer()


@router.callback_query(F.data.startswith("about:"))
async def about(callback: CallbackQuery) -> None:
    lang = normalize_language(callback.data.split(":", 1)[1])
    await callback.message.edit_text(TEXT[lang]["about_text"], reply_markup=keyboard(lang))
    await callback.answer()


@router.message(Command("menu"))
async def menu(message: Message) -> None:
    lang = normalize_language(message.from_user.language_code if message.from_user else None)
    await send_home(message, lang)
