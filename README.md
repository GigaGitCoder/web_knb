<div align="center" style="display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 10px;">
                <img alt="Logo" class="logo flex-item" src="templates/images/Logo.svg" width="150" height="150"/>
</div>
<div align="center">
<h1>ВебКНБ (Web Rock Paper Scissors)</h1>
  
![Contributors](https://img.shields.io/github/contributors/GigaGitCoder/web_knb)
![Issues](https://img.shields.io/github/issues/GigaGitCoder/web_knb)
![MIT License](https://img.shields.io/github/license/GigaGitCoder/web_knb)
![Forks](https://img.shields.io/github/forks/GigaGitCoder/web_knb)
![Stars](https://img.shields.io/github/stars/GigaGitCoder/web_knb)

</div>
 
> 🏆 Этот проект был разработан в рамках хакатона DevHack #5 (26 февраля - 2 марта 2024) <br>
> <img src="https://img.icons8.com/fluency/48/000000/microsoft-powerpoint-2019.png" width="20" height="20"/> **[Презентация проекта](ВебКНБ.pptx)** 

>DevHack #5 - юбилейный хакатон для начинающих IT-специалистов в возрасте от 13 до 18 лет, проходивший в Центре цифрового образования детей «IT-Куб» (Ростов-на-Дону). Мероприятие организовано при поддержке ЮФУ, РГЭУ (РИНХ), РГУПС и Сбербанка.

## 🛠 Технологии

- <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="13" height="13"/> Python 3.8+
- <img src="https://static.djangoproject.com/img/icon-touch.e4872c4da341.png" width="13" height="13"/> Django 5.1.6 
- <img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" width="13" height="13"/> OpenCV
- <img src="https://res.cloudinary.com/startup-grind/image/upload/c_fill,dpr_2.0,f_auto,g_center,h_1080,q_100,w_1080/v1/gcs/platform-data-goog/events/mediapipe_icon.png" width="13" height="13"/> MediaPipe
- <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="13" height="13"/> HTML5
- <img src="https://upload.wikimedia.org/wikipedia/commons/6/62/CSS3_logo.svg" width="13" height="13"/> CSS3
- <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg" width="13" height="13"/> JavaScript
- <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg" width="13" height="13"/> Figma - [Концепт дизайна](https://www.figma.com/design/lCKHElk9uNNpPP2NIwRQRY/RPS?node-id=2-16&t=ZbWSBUOP4rnJ4vNp-1)

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/GigaGitCoder/web_knb.git
cd web_knb
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv\Scripts\activate # Linux/MacOS
venv\Scripts\activate # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. ⚠️ ВАЖНО ДЛЯ ОРГАНИЗАТОРОВ ХАКАТОНА:<br>
   Создайте файл `.env` в папке `web_knb` со следующим содержимым:
```
SECRET_KEY = 'django-insecure-a5!l+qxdu4k)keesvrm!5=ro0glbduk3#q5hqmk)3i_@7x7a2w'
```
   Примечание: Данный ключ оставлен в документации намеренно для упрощения процесса оценки проекта.

5. Примените миграции:
```bash
python manage.py migrate
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

## 📝 Использование

1. Откройте браузер и перейдите по адресу `http://localhost:8000`
2. Зарегистрируйтесь или войдите в систему
3. Перейдите в раздел "Игра"
4. Разрешите доступ к камере
5. Покажите жест (камень/ножницы/бумага) перед камерой
6. Наслаждайтесь игрой!

## 🎮 Функционал

### <img src="https://img.icons8.com/color/48/000000/user-credentials.png" width="24" height="24"/> Система аккаунтов
<table>
<tr>
<td width="400px">
<img src="media/log-reg-system-github.gif" width="400px">
</td>
<td width="500px">
<div align="left" style="min-height: 200px;">
<b>Полноценная система авторизации и аутентификации пользователей с персональными профилями и статистикой.</b>
<hr style="border: 1px solid #555; margin: 10px 0;">
<ul>
  <li>Регистрация новых пользователей с уникальным логином и email</li>
  <li>Безопасное хранение паролей с использованием хеширования</li>
  <li>Авторизация существующих пользователей</li>
  <li>Персональная статистика игр для каждого пользователя</li>
</ul>
</div>
</td>
</tr>
</table>

### <img src="https://img.icons8.com/color/48/000000/hand.png" width="24" height="24"/> Игровой процесс
<table>
<tr>
<td width="400px">
<img src="media/game-system-github.gif" width="400px">
</td>
<td width="500px">
<div align="left" style="min-height: 200px;">
<b>Инновационный способ игры в "Камень-Ножницы-Бумага" с использованием компьютерного зрения для распознавания жестов.</b>
<hr style="border: 1px solid #555; margin: 10px 0;">
<ul>
  <li>Распознавание жестов через веб-камеру по истечению таймера</li>
  <li>Автоматическое определение жеста игрока (камень/ножницы/бумага)</li>
  <li>Случайный выбор жеста компьютером</li>
  <li>Мгновенное определение победителя</li>
  <li>Сохранение результатов в профиле игрока</li>
</ul>
</div>
</td>
</tr>
</table>

### <img src="https://img.icons8.com/color/48/000000/leaderboard.png" width="24" height="24"/> Таблица лидеров
<table>
<tr>
<td width="400px">
<img src="media/leader-board-system-github.gif" width="400px">
</td>
<td width="500px">
<div align="left" style="min-height: 200px;">
<b>Система рейтинга игроков, позволяющая отслеживать успехи и сравнивать результаты с другими участниками.</b>
<hr style="border: 1px solid #555; margin: 10px 0;">
<ul>
  <li>Отслеживание общей статистики всех игроков</li>
  <li>Рейтинг по количеству побед</li>
  <li>Отображение процента выигрышных партий</li>
  <li>Общее количество сыгранных игр</li>
</ul>
</div>
</td>
</tr>
</table>

## 👥 Команда разработчиков

<table>
  <tr>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/GigaGitCoder.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Егор Холкин</b><br />
      <sub><i>Тимлид, Full-stack разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Backend/Frontend разработка<br />
      • Дизайн проекта<br />
      • Работа с базами данных<br />
      • Распознавание жестов
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/GigaGitCoder">GitHub</a> • <a href="https://t.me/IgorXmel">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/Anton2442.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Антон Михайличенко</b><br />
      <sub><i>Backend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Backend разработка<br />
      • Работа с базами данных<br />
      • Распознавание жестов
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/Anton2442">GitHub</a> • <a href="https://t.me/Kish242">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/dencraz.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Даниил Сапронов</b><br />
      <sub><i>Frontend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Frontend разработка<br />
      • Концепт-арты<br />
      • UI/UX дизайн
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/dencraz">GitHub</a> • <a href="https://t.me/dencraz">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/Xqyat.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Роман Колесников</b><br />
      <sub><i>Frontend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Frontend разработка<br />
      • Концепт-арты<br />
      • UI/UX дизайн
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/Xqyat">GitHub</a> • <a href="https://t.me/Forliot">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://sun2-18.userapi.com/s/v1/ig2/QOHM-ftoEZrQ7RfJuFUrKSX-xDVxbAP48ON55c7lWRZQ-5tMwn_j6DT18RVM-ct6oDko6IQG_nAe4BHedSZeLGXN.jpg?quality=95&crop=311,5,476,476&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360&ava=1&u=mBJJIJHalMwlaWdHGeWQx12WYbz1vqaL3H3KEiae26o&cs=200x200" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Цызов Владимир</b><br />
      <sub><i>Computer Vision разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Распознавание жестов<br />
      • Подготовка презентации
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/Malanhei">GitHub</a> • <a href="https://t.me/malanhei">Telegram</a>
      </div>
    </td>
  </tr>
</table>

## 📄 Лицензия

MIT License - подробности в файле [LICENSE](LICENSE)
  
