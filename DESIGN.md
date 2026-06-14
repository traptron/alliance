# DESIGN.md — ССК «Альянс» РТУ МИРЭА

> Дизайн-спецификация для Google Stitch.  
> Студенческий спортивный клуб «Альянс» — веб-платформа турниров, команд и статистики.

---

## 1. Общее описание

**Продукт:** Сайт студенческого спортивного клуба «Альянс» на базе РТУ МИРЭА.  
**Назначение:** Турнирные таблицы, расписание матчей, статистика игроков, информация о сборных.  
**Язык интерфейса:** Русский.  
**Тема:** Светлая (light mode only).  
**Стиль:** Спортивный-минималистичный. Чистые белые карточки, глубокий синий акцент, типографика с характером. Без избыточных теней — вместо них тонкие бордеры и мягкие hover-эффекты.

---

## 2. Цветовая палитра

### Основные цвета

| Токен          | Значение                     | Назначение                          |
|----------------|------------------------------|--------------------------------------|
| `--c-bg`       | `#FFFFFF`                    | Фон страницы                        |
| `--c-surface`  | `#FFFFFF`                    | Фон полей ввода, вторичных блоков   |
| `--c-card`     | `#FFFFFF`                    | Фон карточек                        |
| `--c-primary`  | `#000D61`                    | Основной бренд-цвет (тёмно-синий)  |
| `--c-accent`   | `#074CED`                    | Акцентный синий (ссылки, hover)     |
| `--c-text`     | `#0C1133`                    | Основной текст                      |
| `--c-muted`    | `rgba(12, 17, 51, 0.6)`     | Вторичный текст, подписи            |
| `--c-white`    | `#FFFFFF`                    | Белый текст (на тёмном фоне)        |
| `--c-border`   | `rgba(7, 76, 237, 0.2)`     | Бордеры карточек и разделители      |

### Семантические цвета

| Токен        | Значение    | Назначение                       |
|--------------|-------------|----------------------------------|
| `--c-win`    | `#22C55E`   | Победа, положительные значения   |
| `--c-loss`   | `#EF4444`   | Поражение, отрицательные значения|
| `--c-draw`   | `#F59E0B`   | Ничья, ожидание, предстоящее     |
| `--c-gold`   | `#F5C518`   | 1-е место, золото                |

### Медали (ранги в таблице)

| Ранг    | Цвет      | Фон                             |
|---------|-----------|----------------------------------|
| Золото  | `#F5C518` | `rgba(245, 197, 24, 0.1)`       |
| Серебро | `#A0A8C0` | `rgba(160, 168, 192, 0.1)`      |
| Бронза  | `#CD7F32` | `rgba(205, 127, 50, 0.1)`       |

### Navbar

| Элемент      | Значение                       |
|--------------|--------------------------------|
| Фон          | `rgba(0, 13, 97, 0.96)`       |
| Backdrop     | `blur(20px)`                   |
| Текст ссылок | `rgba(255, 255, 255, 0.8)`    |
| Active ссылка| `#FFFFFF` + border-bottom      |

---

## 3. Типографика

### Шрифты

| Токен            | Семейство                                   | Назначение                          |
|------------------|---------------------------------------------|--------------------------------------|
| `--font-display` | `"Blazma Italic"`, `"Times New Roman"`, serif | Заголовки, бренд, крупные числа     |
| `--font-body`    | `"Montserrat"`, `"Arial"`, sans-serif        | Текст, кнопки, подписи, навигация   |

- **Blazma Italic** — кастомный шрифт, загружается из `static/fonts/Blazma-Italic.ttf`
- **Montserrat** — загружается с Google Fonts, weights: 400, 500, 600, 700

### Размеры текста

| Элемент              | Шрифт     | Размер | Вес  | Letter-spacing | Стиль          |
|----------------------|-----------|--------|------|----------------|----------------|
| Заголовок секции     | display   | 36px   | —    | 2px            | italic         |
| Название турнира     | display   | 28px   | —    | 2px            | italic         |
| Название карточки    | display   | 22px   | —    | 1px            | italic         |
| Название команды (матч)| display | 18px   | —    | 1px            | italic         |
| Счёт матча           | display   | 30px   | —    | 3px            | italic         |
| Имя игрока           | display   | 20px   | —    | 1px            | italic         |
| Число голов          | display   | 32px   | —    | —              | italic         |
| Бренд navbar         | display   | 20px   | —    | 1.5px          | italic         |
| Логин-заголовок      | display   | 32px   | —    | 2px            | italic         |
| Кнопка логин         | display   | 18px   | —    | 2px            | italic         |
| Основной текст       | body      | 16px   | 500  | —              | —              |
| Подпись карточки      | body      | 14px   | 500  | —              | —              |
| Ссылки navbar        | body      | 13px   | 500  | 0.6px          | —              |
| Кнопки nav           | body      | 13px   | 600  | 0.5px          | —              |
| Табличный заголовок  | body      | 10px   | 500  | 2px            | uppercase      |
| Лейбл формы          | body      | 10px   | 500  | 2px            | uppercase      |
| Pill/badge           | body      | 11px   | 500  | 0.5px          | —              |
| Статус матча         | body      | 10px   | —    | 1px            | uppercase      |
| Подпись бренда       | body      | 9px    | —    | 1.5px          | uppercase      |
| Подпись голов         | body      | 9px    | —    | 1.5px          | uppercase      |

---

## 4. Скругления и отступы

### Border radius

| Токен      | Значение | Применение                      |
|------------|----------|---------------------------------|
| `--r-card` | `16px`   | Карточки, таблицы, бар турниров |
| `--r-btn`  | `8px`    | Кнопки, инпуты, селекты        |
| —          | `18px`   | Hero-блок, brand-strip          |
| —          | `20px`   | Pill-баджи                      |
| —          | `20px`   | Login-card                      |
| —          | `10px`   | Score-display, player rank badge|
| —          | `14px`   | Login logo icon                 |

### Внутренние отступы (padding)

| Компонент        | Padding                     |
|------------------|-----------------------------|
| Карточка         | `20px 22px`                 |
| Таблица (ячейка) | `14px 24px`                 |
| Tournament bar   | `20px 24px`                 |
| Hero             | `48px 32px` (desktop)       |
| Hero             | `28px 16px` (mobile ≤720px) |
| Login card       | `40px`                      |
| Input            | `12px 16px`                 |
| Кнопка nav       | `8px 18px`                  |
| Pill             | `4px 12px`                  |
| Points badge     | `3px 10px`                  |
| Page content     | `40px 24px 120px`           |

### Пробелы между секциями

| Между чем                 | Значение    |
|---------------------------|-------------|
| Секции (margin-bottom)    | `40px`      |
| Section header → контент  | `24px`      |
| Карточки в grid (gap)     | `16px`      |
| Divider (margin)          | `40px 0`    |

---

## 5. Компоненты

### 5.1 Navbar (`alliance-navbar`)

- **Позиция:** sticky top, z-index 1000
- **Высота:** 64px
- **Фон:** `rgba(0, 13, 97, 0.96)` + `backdrop-filter: blur(20px)`
- **Контент:** max-width 1200px, центрирован
- **Бренд:** Лого (44×44px) + текст (название + подпись)
- **Ссылки:** горизонтально, `space-evenly`, active — белая нижняя граница
- **Действия:** кнопки Admin (outline) и Выход/Авторизация (solid)
- **Mobile (≤1200px):** hamburger → fullscreen overlay панель

### 5.2 Hero-блок (`home-hero`)

- **Фон:** `rgba(7, 76, 237, 0.08)` + border `rgba(7, 76, 237, 0.2)`
- **Скругление:** 18px
- **Layout:** grid, center-aligned
- **Логотип:** `min(520px, 80vw)` ширина
- **Подпись:** 18px, цвет `rgba(12, 17, 51, 0.7)`

### 5.3 Brand Strip (`brand-strip`)

- **Фон:** `rgba(7, 76, 237, 0.06)` + border
- **Layout:** flex column, centered
- **Логотип:** `min(420px, 70vw)` ширина
- **Используется на:** странице турниров

### 5.4 Tournament Bar (`tournament-bar`)

- **Стиль:** белая карточка с border
- **Layout:** flex, `space-between`, wrap
- **Содержимое:**
  - Левая часть: название турнира (display font 28px) + pills (сезон, статус)
  - Правая часть: два select-dropdown (турнир + вид спорта)
- **Pills:** rounded badge (`border-radius: 20px`), цветные strong-значения

### 5.5 Карточки (`alliance-card`)

- **Фон:** white, border `rgba(7, 76, 237, 0.2)`, radius 16px
- **Hover:** `translateY(-2px)` + усиленный border + gradient-line сверху (2px, accent, появляется через opacity)
- **Состав:** sport-tag (маленький badge) → title (display 22px) → subtitle (body 14px, muted)
- **Grid:** `repeat(auto-fill, minmax(280px, 1fr))`, gap 16px

### 5.6 Match Card (`match-card`)

- **Layout:** grid `1fr auto 1fr` для команд
- **Счёт:** display font 30px, на фоне `rgba(7, 76, 237, 0.08)`, border, radius 10px
- **Мета:** дата (11px muted) + статус badge
- **Статус finished:** зелёный badge (`rgba(34, 197, 94, 0.1)`)
- **Статус upcoming:** жёлтый badge (`rgba(245, 158, 11, 0.1)`)

### 5.7 Player Card (`player-card`)

- **Layout:** flex row — rank badge + info + stat value
- **Rank badge:** 40×40px, radius 10px, display font 20px
  - 1-е место: gold background + gold text
  - 2-е место: silver
  - 3-е место: bronze
- **Stat value:** display font 32px, accent color
- **Подпись:** 9px uppercase

### 5.8 League Table (`alliance-table`)

- **Обёртка:** white card с overflow hidden
- **Заголовки:** 10px uppercase, muted, letter-spacing 2px
- **Строки:** hover `rgba(7, 76, 237, 0.05)`
- **Ранг:** 12px muted
- **Команда:** logo (32×32) + name (600 weight)
- **Points badge:** primary bg, white text, radius 6px

### 5.9 Login Page

- **Полностраничный layout:** centered flex, min-height 100vh
- **Card:** max-width 400px, radius 20px, gradient-line сверху (3px, primary→accent)
- **Logo:** 56×56 квадрат, primary bg, display font "A", radius 14px
- **Inputs:** white bg, muted placeholder, focus ring `rgba(7, 76, 237, 0.15)`
- **Кнопка:** full-width, primary bg, display font 18px, hover→accent, active→scale(0.98)

### 5.10 Section Card (заглушка)

- **Стиль:** белая карточка с border, radius 16px, padding 24px
- **Текст:** body font, стандартный цвет
- **Назначение:** placeholder для страниц в разработке

### 5.11 Footer (`site-footer`)

- **Позиция:** fixed bottom, скрыт по умолчанию (`translateY(100%)`)
- **Появляется:** когда пользователь прокрутил до конца (class `footer-visible`)
- **Содержимое:** бренд (display 16px, muted) + год (body 12px, muted)
- **Transition:** `transform 0.2s ease`

### 5.12 Кнопки

| Вариант           | Фон             | Border                 | Текст    | Hover                              |
|-------------------|-----------------|------------------------|----------|--------------------------------------|
| `nav-btn--solid`  | `--c-primary`   | `--c-primary`          | white    | bg→accent, border→accent             |
| `nav-btn--outline`| transparent     | `rgba(255,255,255,0.35)`| white    | bg→`rgba(255,255,255,0.12)`          |
| `nav-btn--frame`  | transparent     | none (SVG frame)       | white    | `translateY(-1px)`, brightness(1.08) |
| `btn-primary-brand`| `--c-primary`  | `--c-primary`          | white    | bg→accent                            |
| `btn-login`       | `--c-primary`   | none                   | white    | bg→accent, active→scale(0.98)        |

### 5.13 Select (`form-select-dark`)

- **Стиль:** custom appearance, white bg, muted border
- **Arrow:** inline SVG chevron через `background-image`
- **Focus:** border→accent + box-shadow ring `rgba(7, 76, 237, 0.15)`

---

## 6. Layout и сетка

| Параметр              | Значение      |
|-----------------------|---------------|
| Max-width контента    | `1200px`      |
| Padding страницы      | `40px 24px 120px` |
| Cards grid            | `auto-fill, minmax(280px, 1fr)`, gap 16px |
| Navbar height         | `64px`        |
| Mobile breakpoint     | `1200px` (навигация) |
| Hero breakpoint       | `720px`       |

---

## 7. Анимации

### Fade-up (появление карточек)

```css
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
```

- Длительность: `0.4s ease both`
- Staggered: +50ms на каждый дочерний элемент (до 5-ти)

### Hover-эффекты

| Компонент   | Эффект                                              |
|-------------|-----------------------------------------------------|
| Карточки    | `translateY(-2px)` + gradient-line top (opacity 0→1)|
| Матч-карты  | `translateY(-2px)` + усиление border                |
| Кнопки      | Смена фона (`primary→accent`), transition `0.2s`    |
| Ссылки nav  | Цвет `0.8→1.0` opacity                              |
| Строки таблицы | Лёгкая подсветка `rgba(7, 76, 237, 0.05)`        |
| Footer      | `translateY(100%→0)` при прокрутке до конца         |

---

## 8. Фоновый паттерн

- **Элемент:** `.bg-grid` — fixed fullscreen overlay
- **Изображение:** `pattern-font.png` (tiled), размер тайла 360px
- **Opacity:** `0.12`
- **z-index:** `0` (под контентом)
- **pointer-events:** none

---

## 9. Иконки и ассеты

| Ассет                       | Путь                                     | Назначение                   |
|-----------------------------|------------------------------------------|------------------------------|
| Логотип (navbar)            | `img/logos/alliance-big-mono.png`        | Монохромный лого 44×44       |
| Сублого (hero/strip)        | `img/logos/alliance-sublogo.png`         | Большой логотип для секций   |
| Меню-иконка                 | `img/icons/menu.svg`                     | Hamburger 30×30              |
| Frame (кнопка авторизации)  | `img/frames/frame-2.svg`                 | Декоративная рамка кнопки    |
| Фоновый паттерн             | `img/patterns/pattern-font.png`          | Текстурный паттерн на фон    |
| Шрифт Blazma                | `fonts/Blazma-Italic.ttf`               | Display-шрифт                |

---

## 10. Навигация (страницы)

| Страница     | URL            | Описание                              |
|--------------|----------------|---------------------------------------|
| Главная      | `/`            | Hero + ближайшие турниры + новости    |
| Турниры      | `/tournaments` | Таблица, матчи, игроки, выбор турнира |
| Сборные      | `/teams`       | Список сборных команд (заглушка)      |
| Расписание   | `/schedule`    | Расписание матчей (заглушка)          |
| Медиа        | `/media`       | Фото и видео (заглушка)              |
| О проекте    | `/about`       | Описание клуба                        |
| Логин        | `/login`       | Форма авторизации администратора      |
| Админ-панель | `/admin`       | Flask-Admin (только is_admin=True)    |

---

## 11. Адаптивность

### Breakpoints

| Точка    | Что меняется                                    |
|----------|-------------------------------------------------|
| ≤1200px  | Навигация → fullscreen hamburger overlay        |
| ≤720px   | Hero padding уменьшается, лого `min(360px, 92vw)` |

### Мобильная навигация

- Кнопка hamburger (40×40, SVG-иконка)
- Полноэкранный overlay (`rgba(0, 13, 97, 0.98)`)
- Ссылки стековые с разделителями + arrows `›`
- Кнопка закрытия (X из двух css-линий)

---

## 12. Ключевые принципы дизайна

1. **Белое пространство:** Чистый белый фон, минимум визуального шума
2. **Акцент через цвет:** Глубокий синий `#000D61` как primary, яркий `#074CED` как accent
3. **Характерная типографика:** Italic display-шрифт Blazma для заголовков — спортивный характер
4. **Тонкие бордеры вместо теней:** Все карточки используют `1px solid` с полупрозрачным синим
5. **Минимальные hover-эффекты:** `translateY(-2px)` + gradient line top на карточках
6. **Мягкий фоновый паттерн:** Тонкая текстура (12% opacity) добавляет глубину без перегрузки
7. **Спортивная семантика:** Gold/Silver/Bronze для рангов, Win/Loss/Draw цвета для статистики
