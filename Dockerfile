# Используем официальный образ Python
FROM python:3.9-slim
WORKDIR /app
# Копируем файл с зависимостями (requirements.txt) в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Указываем порт, который будет слушать приложение
EXPOSE 5000

# Запускаем приложение
CMD ["python", "main.py"]