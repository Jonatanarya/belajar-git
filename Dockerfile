# STAGE 1: Builder
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# STAGE 2: Production (Final)
# Menggunakan slim (bukan alpine) untuk kompatibilitas Flask
FROM python:3.9-slim
WORKDIR /app

# Hanya menyalin hasil install dari stage builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Menentukan nilai default untuk variabel lingkungan
ENV APP_USER="Developer Mahasiswa"
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
