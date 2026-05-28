def render_dashboard(data_list, is_loading=False):
    print("--- DASHBOARD APLIKASI ---")

    if is_loading:
        print("Mohon Tunggu...")
    elif not data_list:
        print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
    else:
        for item in data_list:
            print(f"- Item ID: {item['id']} | Nama: {item['name']}")
