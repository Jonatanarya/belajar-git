import os
from flask import Flask

app = Flask(__name__)

# Membaca variabel lingkungan
user_name = os.getenv('APP_USER', 'Guest')
app_env = os.getenv('APP_ENV', 'development')
app_version = os.getenv('APP_VERSION', 'v2-prod')

HTML_PAGE = f'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MVC App - Versi 2.0</title>
    <style>
        body {{
            background-color: #f5f7fb;
            color: #1f2937;
            font-family: 'Segoe UI', Arial, sans-serif;
            text-align: center;
            padding: 60px 20px;
            margin: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .dashboard-title {{
            color: #2563eb;
            font-size: 28px;
            margin-bottom: 20px;
        }}
        .version-badge {{
            background-color: #2563eb;
            color: white;
            padding: 12px 28px;
            border-radius: 8px;
            display: inline-block;
            font-size: 22px;
            font-weight: bold;
            margin: 20px 0;
        }}
        .info {{
            margin-top: 20px;
            font-size: 16px;
            line-height: 1.8;
        }}
        .item-row {{
            color: #047857;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="dashboard-title">Halo, {user_name}!</h1>
        <div class="version-badge">Versi 2.0 - Stabil</div>
        <div class="info">
            <p>Aplikasi MVC berjalan di dalam kontainer Docker.</p>
            <p class="item-row"><strong>Lingkungan:</strong> {app_env}</p>
            <p class="item-row"><strong>Versi:</strong> {app_version}</p>
        </div>
    </div>
</body>
</html>'''


@app.route('/')
def home():
    return HTML_PAGE


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
