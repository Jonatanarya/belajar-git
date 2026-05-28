def render_dashboard(data_list):
print("--- DASHBOARD APLIKASI ---")
if not data_list:
print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
else:
for item in data_list:
print(f"- Item ID: {item['id']} | Nama: {item['name']}")