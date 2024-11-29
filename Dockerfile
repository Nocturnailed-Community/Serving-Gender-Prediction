# Gunakan Python resmi sebagai base image
FROM python:3.10-slim

# Set working directory di container
WORKDIR /app

# Salin semua file dari direktori lokal ke dalam container
COPY . /app

# Install pip dan dependensi dari requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Ekspose port 8000 (port default untuk FastAPI)
EXPOSE 8000

# Jalankan aplikasi FastAPI menggunakan uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]