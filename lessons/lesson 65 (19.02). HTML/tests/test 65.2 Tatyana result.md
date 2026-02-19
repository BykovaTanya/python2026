Вопросы с выбором варианта: 56/78%  
# Вопрос 1. Блок 3. Текстовый контент, ссылки, списки, изображения
  
### Содержание и вопросы

- Как сделать ссылку и какие бывают `href`?
- Чем `ul` отличается от `ol`?
- Зачем нужен `alt` у изображения?
- Как структурировать “карточку” проекта только HTML-ом?

### Материал (лаконично)

- Ссылка это тег `a`. Внутри должен быть текст, по которому понятно, куда ведет ссылка.
- `href` может быть:
  - обычным адресом сайта
  - якорем внутри страницы
  - `mailto:` для письма
- Списки:
  - `ul` когда порядок не важен, например “навыки”
  - `ol` когда это шаги, порядок важен
- Картинка это `img`. `alt` обязателен. Если картинка не загрузится, текст `alt` подскажет, что там должно быть.
- “Карточка” проекта это просто блок. Обычно внутри: заголовок, текст, ссылка.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 3)
  
### Условия

Добавь контент в `index.html` пошагово:

1. В одной из секций добавь заголовок и под ним список.
2. Заполни список из 5 пунктов.
3. В секции с проектами создай контейнер для карточек.
4. Создай минимум 3 карточки. В каждой карточке сделай:
   - заголовок карточки
   - короткий текст-описание
   - ссылку
5. В шапке добавь изображение-аватар.
6. В подвале сделай блок контактов и добавь минимум 3 ссылки.
7. Проверь, что у всех `img` есть `alt`, а у всех `a` есть `href`.

Проверка:

- Все ссылки кликабельны.
- Все изображения имеют `alt`.

### Псевдокод решения

```text
IN SECTION_B
  CREATE LIST
    ADD LIST_ITEM (REPEAT 5 TIMES)

IN SECTION_C
  CREATE CARDS_CONTAINER
    REPEAT 3 TIMES
      CREATE CARD
        ADD CARD_TITLE
        ADD CARD_TEXT
        ADD CARD_LINK

IN HEADER
  ADD IMAGE_WITH_ALT

IN FOOTER
  CREATE CONTACTS_LIST
    ADD LINK_ITEM (REPEAT 3 TIMES)
END
```

### Если использовал ИИ, обязательные изменения вручную

- Замени один тип списка на другой (например, `ul` на `ol` или наоборот) и объясни почему это подходит.
- Добавь еще одну ссылку с другим типом `href` (например, `mailto:`).

---

**Вставь решение в комментарий ниже:**
  
### Ответ
<!DOCTYPE html>  
<html lang="ru">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Моя Визитка</title>  
    <link rel="stylesheet" href="styles.css">  
</head>  
<body>  
  
    <header>  
        <img src="Багирка1.jpg" alt="Татьяна" width="130">  
	<h1>Введение в HTML</h1>  
        <p>Короткое описание.</p>  
    </header>  
  
    <main>  
        <section>  
            <h2>О проекте</h2>  
            <!-- Здесь будет ваш текст -->  
        </section>  
  
        <section>  
            <h2>Наши услуги</h2>  
            <ul>  
                <li>Создаем</li>  
                <li>Адаптируем</li>  
                <li>Дополняем</li>  
                <li>Разрабатываем</li>  
                <li>Оптимизируем</li>  
            </ul>  
        </section>  
  
	<section>  
            <h2>Проекты</h2>  
            <div class="cards-container">  
                <article class="card">  
                    <h3>Создаем</h3>  
                    <p>Как подключить CSS к HTML: три способа связывания стилей с кодом.</p>  
                    <a href="https://sky.pro/wiki/html/kak-podklyuchit-css-k-html-dokumentu/?ysclid=mltij9j3d7931471483">Смотреть проект</a>  
                </article>  
  
                <article class="card">  
                    <h3>Дополняем</h3>  
                    <p>Тег a в HTML: как создать идеальные гиперссылки для сайта.</p>  
                    <a href="https://sky.pro/wiki/html/tegi-ssylok-v-html-lessagreater/?ysclid=mltjos3hdv763178007">Смотреть проект</a>  
                </article>  
  
               <article class="card">  
                    <h3>Оптимизируем</h3>  
                    <p>Alt-тексты для изображений: невидимый герой SEO-оптимизации.</p>  
                    <a href="https://sky.pro/wiki/lifestyle/alternativnyj-tekst-izobrazhenij-kak-on-pomogaet-seo/">Смотреть проект</a>  
                </article>  
            </div>  
        </section>  
        <section>  
            <h2>Контакты</h2>  
            <!-- Здесь будет ваш текст -->  
        </section>  
    </main>  
  
    <footer>  
        <p>&copy; Татьяна </p>  
	<div class="contacts">  
            <a href="https://top-academy.site/us3e6zi9btnrlgugrk8rwphll5lpaawj/">Email</a> |  
            <a href="https://top-academy.site/3z0pe00eewyjnmhpgk3b9kjrzalckhil/">Telegram</a> |  
            <a href="https://github.com/Pau1R/python2026/blob/main/lessons/lesson%2063%20(16.02).%20%D0%9A%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%2C%20HTML/lesson%2063%20(16.02).%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20HTML.md" target="_blank">GitHub</a>  
        </div>  
    </footer>  
  
</body>  
</html>  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Какой HTML-тег используется для создания обычной ссылки на другую страницу?
  
  
Варианты ответов:
1) `div`
2) ✅ `a`
3) `span`
4) `p`
5) `img`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Какой тип списка лучше подходит для раздела “навыки”, где порядок элементов не имеет значения?
  
  
Варианты ответов:
1) `nav`
2) `form`
3) `table`
4) `ol`
5) ✅ `ul`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Зачем нужен атрибут `alt` у тега изображения `img`?
  
  
Варианты ответов:
1) Для создания отступов
2) ❌ Для изменения размера картинки
3) Для выравнивания текста
4) Для подключения CSS
5) Для текстового описания картинки
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Какое значение атрибута `href` используется для создания ссылки, которая открывает почтовую программу?
  
  
Варианты ответов:
1) `mailto:`
2) `file:`
3) `css:`
4) ❌ `http:`
5) `ftp:`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Какие элементы обычно должны быть внутри “карточки проекта” на странице-визитке?
  
  
Варианты ответов:
1) Только `meta` теги
2) Только таблица с данными
3) Только картинка без текста
4) Только `script` код
5) ✅ Заголовок, текст, ссылка
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что нужно проверить после добавления ссылок и изображений на страницу?
  
  
Варианты ответов:
1) ✅ Что все ссылки имеют `href`
2) Что нет `section`
3) Что `head` пустой
4) Что нет `main`
5) Что нет `footer`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Какое главное требование к тексту внутри ссылки для удобства пользователей?
  
  
Варианты ответов:
1) Чтобы он был на одной букве
2) Чтобы он был только цифрами
3) Чтобы он был скрыт стилями
4) Чтобы он был пустым
5) ✅ Чтобы он был понятным
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
