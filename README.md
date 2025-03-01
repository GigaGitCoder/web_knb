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
 
> 🏆 Этот проект был разработан в рамках хакатона DevHack #5 (26 февраля - 2 марта 2024)

>DevHack #5 - юбилейный хакатон для начинающих IT-специалистов в возрасте от 13 до 18 лет, проходивший в Центре цифрового образования детей «IT-Куб» (Ростов-на-Дону). Мероприятие организовано при поддержке ЮФУ, РГЭУ (РИНХ), РГУПС и Сбербанка.

## 🛠 Технологии

- Python 3.8+
- Django 5.1.6 
- OpenCV
- MediaPipe
- HTML5/CSS3
- JavaScript
- TailwindCSS

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/web_knb.git
cd web_knb
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
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

### Система аккаунтов
<table>
<tr>
<td width="400px">
<img src="media/log-reg-system-github.gif" width="400px">
</td>
<td>
<ul>
  <li>Регистрация новых пользователей с уникальным логином и email</li>
  <li>Безопасное хранение паролей с использованием хеширования</li>
  <li>Авторизация существующих пользователей</li>
  <li>Персональная статистика игр для каждого пользователя</li>
</ul>
</td>
</tr>
</table>

### Игровой процесс
<table>
<tr>
<td width="400px">
<img src="media/game-system.gif" width="400px">
</td>
<td>
<ul>
  <li>Распознавание жестов в реальном времени через веб-камеру</li>
  <li>Автоматическое определение жеста игрока (камень/ножницы/бумага)</li>
  <li>Случайный выбор жеста компьютером</li>
  <li>Мгновенное определение победителя</li>
  <li>Подсчет очков в текущей сессии</li>
</ul>
</td>
</tr>
</table>

### Таблица лидеров
<table>
<tr>
<td width="400px">
<img src="media/leader-board-system.gif" width="400px">
</td>
<td>
<ul>
  <li>Отслеживание статистики всех игроков</li>
  <li>Рейтинг по количеству побед</li>
  <li>Процент выигрышных партий</li>
  <li>История последних игр</li>
  <li>Еженедельное и ежемесячное обновление рейтинга</li>
</ul>
</td>
</tr>
</table>

## 👥 Команда разработчиков

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/GigaGitCoder.png" width="100" height="100" style="border-radius: 50%;"><br />
      <b>Егор Холкин</b><br />
      GitHub: <a href="https://github.com/GigaGitCoder">@GigaGitCoder</a><br />
      Telegram: <a href="https://t.me/IgorXmel">@IgorXmel</a>
    </td>
    <td align="center">
      <img src="https://github.com/Anton2442.png" width="100" height="100" style="border-radius: 50%;"><br />
      <b>Антон Михайличенко</b><br />
      GitHub: <a href="https://github.com/Anton2442">@Anton2442</a><br />
      Telegram: <a href="https://t.me/Kish242">@Kish242</a>
    </td>
    <td align="center">
      <img src="https://github.com/dencraz.png" width="100" height="100" style="border-radius: 50%;"><br />
      <b>Даниил Сапронов</b><br />
      GitHub: <a href="https://github.com/dencraz">@dencraz</a><br />
      Telegram: <a href="https://t.me/dencraz">@dencraz</a>
    </td>
    <td align="center">
      <img src="https://github.com/Xqyat.png" width="100" height="100" style="border-radius: 50%;"><br />
      <b>Роман Колесников</b><br />
      GitHub: <a href="https://github.com/Xqyat">@Xqyat</a><br />
      Telegram: <a href="https://t.me/Forliot">@Forliot</a>
    </td>
    <td align="center">
      <img src="https://sun2-18.userapi.com/s/v1/ig2/QOHM-ftoEZrQ7RfJuFUrKSX-xDVxbAP48ON55c7lWRZQ-5tMwn_j6DT18RVM-ct6oDko6IQG_nAe4BHedSZeLGXN.jpg?quality=95&crop=311,5,476,476&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360&ava=1&u=mBJJIJHalMwlaWdHGeWQx12WYbz1vqaL3H3KEiae26o&cs=200x200" width="100" height="100" style="border-radius: 50%;"><br />
      <b>Цызов Владимир</b><br />
      GitHub: <a href="https://github.com/Malanhei">@Malanhei</a><br />
      Telegram: <a href="https://t.me/malanhei">@malanhei</a>
    </td>
  </tr>
</table>

## 📄 Лицензия

MIT License - подробности в файле [LICENSE](LICENSE)
  
