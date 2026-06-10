import os
# Membaca variabel 'APP_USER', defaultnya adalah 'Guest'
user_name = os.getenv('APP_USER', 'Guest')
# Membaca variabel 'APP_ENV', defaultnya adalah 'development'
app_env = os.getenv('APP_ENV', 'development')
if __name__ == "__main__":
    print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.")
    print(f"Lingkungan: {app_env}")