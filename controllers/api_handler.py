import random

# Simulasikan data dari database
users = [{"id": 1, "name": "Admin"}, {"id": 2, "name": "User"}]

def get_users():
    # Simulasi: 30% kemungkinan server sibuk
    if random.random() < 0.3:
        return {"status": "error", "code": "SERVER_BUSY", "message": "Server sedang sibuk. Coba lagi nanti."}
    
    # Simulasi: 10% kemungkinan timeout
    if random.random() < 0.1:
        return {"status": "error", "code": "TIMEOUT", "message": "Koneksi timeout. Periksa jaringan Anda."}
    
    # 60% kesuksesan
    return {"status": "success", "data": users}