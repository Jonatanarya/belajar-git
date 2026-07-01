#!/bin/bash

# ==========================================
# Script Deploy Otomatis - MVC App
# Penugasan Individu (Lanjutan Praktik)
# ==========================================

# Deteksi OS - gunakan docker.exe di Windows (Git Bash/MSYS)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    DOCKER="docker.exe"
else
    DOCKER="docker"
fi

# Konfigurasi
IMAGE="ghcr.io/jonatanarya/mvc-app:v2-prod"
CONTAINER_NAME="mvc-app"
PORT="8080:5000"

echo "=========================================="
echo "   SKRIP DEPLOY OTOMATIS - MVC App"
echo "=========================================="
echo ""

# 1. Menarik image terbaru dari GHCR
echo "[1/3] Menarik image terbaru dari GHCR..."
echo "   Image: $IMAGE"
$DOCKER pull $IMAGE
echo ""

# 2. Menghentikan dan menghapus kontainer lama
echo "[2/3] Menghentikan kontainer lama..."
$DOCKER stop $CONTAINER_NAME 2>/dev/null && echo "   Kontainer '$CONTAINER_NAME' dihentikan." || echo "   Tidak ada kontainer lama yang berjalan."
$DOCKER rm $CONTAINER_NAME 2>/dev/null && echo "   Kontainer '$CONTAINER_NAME' dihapus." || echo "   Tidak ada kontainer lama untuk dihapus."
echo ""

# 3. Menjalankan kontainer baru
echo "[3/3] Menjalankan kontainer baru..."
$DOCKER run -d --name $CONTAINER_NAME -p $PORT $IMAGE
echo ""

echo "=========================================="
echo "   DEPLOY SELESAI!"
echo "=========================================="
echo "Aplikasi berjalan di: http://localhost:8080"
echo ""
echo "Status kontainer:"
$DOCKER ps --filter "name=$CONTAINER_NAME" --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
echo ""
