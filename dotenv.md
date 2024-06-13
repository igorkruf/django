#### Устанавливаем пакет для считывания переменных окружения из файла
```
pip install python-dotenv
```
#### Создаём файл .env в корне проекта(на одном уровне с файлом manage.py) добавляем в начало файла settings.py. Проверяем на существование 
файла .env 
```
import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path =  BASE_DIR / '.env'
if dotenv_path.exists():
    load_dotenv(dotenv_path)
```
