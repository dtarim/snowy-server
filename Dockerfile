# 1. Temel Python imajını kullanıyoruz
FROM python:3.9-slim

# 2. Çalışma dizinini /app olarak belirliyoruz
WORKDIR /app

# 3. Gereksinim dosyasını (requirements.txt) konteynere kopyalıyoruz
COPY requirements.txt .

# 4. Python bağımlılıklarını yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Uygulama dosyalarını konteynere kopyalıyoruz
COPY . .

# 6. Flask uygulamasının dinleyeceği portu açıyoruz (default 5000)
EXPOSE 15000

# 7. Uygulamayı başlatıyoruz
CMD ["python", "app.py"]
