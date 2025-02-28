<div style="display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 10px;">
                <img alt="Logo" class="logo flex-item" src="templates/images/Logo.svg" width="150" height="150"/>
                <h1 style="font-size: 5rem; font-weight: bold;">ВебКНБ</h1>
            </div>
<br><br>
<div align="center">

[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url]

[contributors-shield]: https://img.shields.io/github/contributors/GigaGitCoder/web_knb.svg?style=for-the-badge
[contributors-url]: https://github.com/GigaGitCoder/web_knb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/GigaGitCoder/web_knb.svg?style=for-the-badge
[forks-url]: https://github.com/GigaGitCoder/web_knb/network/members
[stars-shield]: https://img.shields.io/github/stars/GigaGitCoder/web_knb.svg?style=for-the-badge
[stars-url]: https://github.com/GigaGitCoder/web_knb/stargazers
[issues-shield]: https://img.shields.io/github/issues/GigaGitCoder/web_knb.svg?style=for-the-badge
[issues-url]: https://github.com/GigaGitCoder/web_knb/issues
[license-shield]: https://img.shields.io/github/license/GigaGitCoder/web_knb.svg?style=for-the-badge
[license-url]: https://github.com/GigaGitCoder/web_knb/blob/master/LICENSE

</div>

Веб-приложение для игры в "Камень, ножницы, бумага" с использованием компьютерного зрения для распознавания жестов.

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

4. Создайте файл .env в корневой директории проекта:
```
SECRET_KEY=your-secret-key-here
```

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
- Регистрация новых пользователей с уникальным логином и email
- Безопасное хранение паролей с использованием хеширования
- Авторизация существующих пользователей
- Персональная статистика игр для каждого пользователя

### Игровой процесс
- Распознавание жестов в реальном времени через веб-камеру
- Автоматическое определение жеста игрока (камень/ножницы/бумага)
- Случайный выбор жеста компьютером
- Мгновенное определение победителя
- Подсчет очков в текущей сессии

### Таблица лидеров
- Отслеживание статистики всех игроков
- Рейтинг по количеству побед
- Процент выигрышных партий
- История последних игр
- Еженедельное и ежемесячное обновление рейтинга

### Безопасность
- Защита от несанкционированного доступа
- Безопасное хранение пользовательских данных
- Защита от спама и ботов при регистрации
- Возможность восстановления доступа к аккаунту

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
      <img src="https://github.com/Malanhei.png" width="100" height="100" style="border-radius: 50%;"><br />
      <b>Владимир Цызов</b><br />
      GitHub: <a href="https://github.com/Malanhei">@Malanhei</a><br />
      Telegram: <a href="https://t.me/malanhei">@malanhei</a>
    </td>
  </tr>
</table>

## 📄 Лицензия

MIT License - подробности в файле [LICENSE](LICENSE)
