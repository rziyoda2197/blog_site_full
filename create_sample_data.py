"""
Sample data script for the blog.
Run: python manage.py shell < create_sample_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Tag, Post

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser yaratildi: admin / admin123")

# Categories
categories_data = [
    ('Texnologiya', 'texnologiya', 'Zamonaviy texnologiyalar haqida maqolalar'),
    ('Dasturlash', 'dasturlash', 'Dasturlash tillari va frameworklar'),
    ('Sayohat', 'sayohat', "O'zbekiston va dunyo bo'ylab sayohatlar"),
    ('Hayot', 'hayot', 'Kundalik hayot va foydali maslahatlar'),
    ('Kitoblar', 'kitoblar', "Kitob sharhlari va tavsiyalar"),
]

for name, slug, desc in categories_data:
    Category.objects.get_or_create(name=name, slug=slug, defaults={'description': desc})
print(f"{Category.objects.count()} ta kategoriya yaratildi")

# Tags
tags_data = [
    ('python', 'python'), ('django', 'django'), ('javascript', 'javascript'),
    ('web', 'web'), ('linux', 'linux'), ('git', 'git'),
    ('api', 'api'), ('database', 'database'), ('css', 'css'), ('html', 'html'),
]

for name, slug in tags_data:
    Tag.objects.get_or_create(name=name, slug=slug)
print(f"{Tag.objects.count()} ta teg yaratildi")

# Posts
posts_data = [
    {
        'title': "Django bilan veb dasturlashni boshlash",
        'slug': 'django-bilan-veb-dasturlashni-boshlash',
        'excerpt': "Django — Python dasturlash tilida yozilgan eng mashhur veb framework. Bu maqolada Django bilan tanishamiz.",
        'content': """Django — bu Python dasturlash tilida yozilgan bepul va ochiq kodli veb framework. U 2005-yilda yaratilgan bo'lib, bugungi kunda dunyoning eng ko'p ishlatiladigan veb frameworklaridan biridir.

Django nima uchun mashhur?

Django "batteries included" falsafasiga amal qiladi. Bu shuni anglatadiki, siz loyihani boshlash uchun kerak bo'lgan deyarli barcha narsalar allaqachon framework tarkibida mavjud:

- Admin panel avtomatik yaratiladi
- ORM (Object-Relational Mapping) orqali ma'lumotlar bazasi bilan ishlash
- URL routing tizimi
- Template engine
- Xavfsizlik himoyalari (CSRF, XSS, SQL injection)

Django loyiha tuzilishi

Yangi Django loyiha quyidagi tuzilishga ega bo'ladi:

myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py

Har bir fayl o'z vazifasiga ega. settings.py — loyiha sozlamalari, urls.py — URL marshrutlari, wsgi.py — serverga ulash uchun.

Xulosa

Django o'rganish uchun ajoyib framework. U tez, xavfsiz va kengaytiriladigan veb ilovalar yaratish imkonini beradi. Keyingi maqolalarda Django modellarini va view'larni batafsil ko'rib chiqamiz.""",
        'category_slug': 'dasturlash',
        'tags': ['python', 'django', 'web'],
        'status': 'published',
        'is_pinned': True,
    },
    {
        'title': "Python o'rganish uchun 5 ta foydali resurs",
        'slug': 'python-organish-uchun-5-ta-foydali-resurs',
        'excerpt': "Python dasturlash tilini o'rganmoqchimisiz? Bu maqolada eng yaxshi resurslarni ko'rib chiqamiz.",
        'content': """Python — bugungi kunda eng mashhur va ko'p o'rganiladigan dasturlash tillaridan biri. Agar siz ham Python o'rganmoqchi bo'lsangiz, quyidagi resurslar sizga yordam beradi.

1. Python rasmiy dokumentatsiyasi

Python.org sayti — eng ishonchli manba. Bu yerda tilning barcha xususiyatlari batafsil yozilgan.

2. Real Python

realpython.com — Python bo'yicha eng sifatli maqolalar va video darsliklar to'plami. Boshlovchilar uchun ham, tajribali dasturchilar uchun ham foydali.

3. Automate the Boring Stuff

Bu kitob Python orqali kundalik vazifalarni avtomatlashtirish haqida. Bepul onlayn versiyasi mavjud.

4. LeetCode va HackerRank

Algoritmik masalalar yechish orqali Python ko'nikmalaringizni mustahkamlang.

5. YouTube kanallari

"Corey Schafer" va "Tech With Tim" kanallari Python bo'yicha ajoyib video darsliklar taqdim etadi.

Xulosa

Python o'rganish maroqli va foydali! Muhimi — har kuni amaliyot qiling va haqiqiy loyihalar ustida ishlang.""",
        'category_slug': 'dasturlash',
        'tags': ['python'],
        'status': 'published',
    },
    {
        'title': "Git va GitHub: boshlovchilar uchun qo'llanma",
        'slug': 'git-va-github-boshlash',
        'excerpt': "Git versiyalarni boshqarish tizimi va GitHub platformasi haqida to'liq qo'llanma.",
        'content': """Git — bu dasturchilar uchun yaratilgan versiyalarni boshqarish tizimi. GitHub esa Git repozitoriylarini onlayn saqlash va hamkorlikda ishlash platformasidir.

Git nima uchun kerak?

Tasavvur qiling, siz katta loyiha ustida ishlayapsiz. Bir nechta kishi bir vaqtda turli xil fayllarni o'zgartiradi. Git quyidagilarga yordam beradi:

- Har bir o'zgarishni kuzatish
- Xato bo'lganda oldingi versiyaga qaytish
- Bir nechta odam bir vaqtda ishlash
- Turli xususiyatlarni alohida ishlab chiqish (branch)

Asosiy Git buyruqlari

git init — yangi repozitoriya yaratish
git add . — o'zgarishlarni qo'shish
git commit -m "xabar" — o'zgarishlarni saqlash
git push — servarga yuklash
git pull — serverdan yuklab olish

GitHub nima?

GitHub — bu Git repozitoriylarini bulutda saqlash xizmati. U qo'shimcha imkoniyatlar beradi: pull request, issue tracking, GitHub Actions va boshqalar.

Xulosa

Git va GitHub zamonaviy dasturlashning ajralmas qismidir. Ularni o'rganish har bir dasturchi uchun muhimdir.""",
        'category_slug': 'texnologiya',
        'tags': ['git'],
        'status': 'published',
    },
    {
        'title': "Zamonaviy CSS: Flexbox va Grid haqida",
        'slug': 'zamonaviy-css-flexbox-va-grid',
        'excerpt': "CSS Flexbox va Grid layout tizimlari haqida amaliy qo'llanma.",
        'content': """CSS Flexbox va Grid — zamonaviy veb sahifalar yaratishning asosiy vositalari. Bu maqolada ikkala texnologiyani taqqoslaymiz va amaliy misollar ko'rsatamiz.

Flexbox — bir o'lchamli layout

Flexbox elementlarni bir yo'nalishda (gorizontal yoki vertikal) joylashtirishda ajoyib ishlaydi.

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
}

CSS Grid — ikki o'lchamli layout

Grid esa satrlarda ham, ustunlarda ham elementlarni joylashtirish imkonini beradi.

.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

Qachon qaysi birini ishlatish kerak?

- Flexbox: navigatsiya, kartalar qatori, form elementlari
- Grid: butun sahifa layout, murakkab grid tizimlar, galereya

Ikkalasini birgalikda ishlatish eng yaxshi natija beradi!""",
        'category_slug': 'dasturlash',
        'tags': ['css', 'html', 'web'],
        'status': 'published',
    },
    {
        'title': "Linux asoslari: terminal buyruqlari",
        'slug': 'linux-asoslari-terminal-buyruqlari',
        'excerpt': "Linux terminalida ishlash uchun eng zarur buyruqlar to'plami va ularning tushuntirishlari.",
        'content': """Linux terminali — dasturchilar uchun eng kuchli vosita. Bu maqolada eng ko'p ishlatiladigan buyruqlarni ko'rib chiqamiz.

Fayl va papkalar bilan ishlash:
ls — fayllar ro'yxatini ko'rish
cd — papkaga o'tish
mkdir — yangi papka yaratish
rm — faylni o'chirish
cp — nusxa olish
mv — ko'chirish yoki nom o'zgartirish

Matn bilan ishlash:
cat — fayl mazmunini ko'rish
grep — matn qidirish
head/tail — fayl boshi/oxirini ko'rish

Tizim buyruqlari:
top — jarayonlarni kuzatish
df — disk hajmini ko'rish
chmod — ruxsatlarni o'zgartirish

Linux terminali bilan ishlash ko'nikmasi har qanday dasturchi uchun juda muhim.""",
        'category_slug': 'texnologiya',
        'tags': ['linux'],
        'status': 'published',
    },
    {
        'title': "REST API nima va qanday ishlaydi?",
        'slug': 'rest-api-nima-va-qanday-ishlaydi',
        'excerpt': "REST API arxitekturasi, HTTP metodlari va amaliy misollar bilan tushuntirish.",
        'content': """REST (Representational State Transfer) API — zamonaviy veb ilovalarning asosiy aloqa usuli. Bu maqolada REST API qanday ishlashini tushuntiramiz.

REST API asosiy tamoyillari:
1. Client-Server arxitektura
2. Stateless — har bir so'rov mustaqil
3. HTTP metodlaridan foydalanish

HTTP metodlari:
GET — ma'lumot olish
POST — yangi ma'lumot yaratish
PUT — mavjud ma'lumotni yangilash
DELETE — ma'lumotni o'chirish

API javob formatlari:
Ko'pincha JSON formatida javob qaytariladi. JSON oson o'qiladi va barcha dasturlash tillari tomonidan qo'llab-quvvatlanadi.

Django REST Framework orqali Python dasturchilar tez va qulay API yarata olishadi.""",
        'category_slug': 'dasturlash',
        'tags': ['api', 'python', 'django', 'web'],
        'status': 'published',
    },
]

for post_data in posts_data:
    cat = Category.objects.get(slug=post_data['category_slug'])
    post, created = Post.objects.get_or_create(
        slug=post_data['slug'],
        defaults={
            'title': post_data['title'],
            'content': post_data['content'],
            'excerpt': post_data['excerpt'],
            'category': cat,
            'status': post_data['status'],
            'is_pinned': post_data.get('is_pinned', False),
        }
    )
    if created:
        for tag_slug in post_data['tags']:
            tag = Tag.objects.get(slug=tag_slug)
            post.tags.add(tag)

print(f"{Post.objects.count()} ta maqola yaratildi")
print("\nTayyor! Serverni ishga tushiring: python manage.py runserver")
