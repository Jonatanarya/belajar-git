def render_dashboard(data_list, is_loading=False):
    print("--- DASHBOARD APLIKASI ---")

    if is_loading:
        print("Mohon Tunggu...")
    elif not data_list:
        print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
    else:
        for item in data_list:
            print(f"- Item ID: {item['id']} | Nama: {item['name']}")


def fetch_data_from_api(api_function):
    print("[System] Mencoba menghubungkan ke API...")
    try:
        response = api_function()
        if response["status"] == "success":
            print("[Success] Data berhasil diambil dari API")
            return response["data"]
        else:
            error_code = response.get("code", "UNKNOWN")
            error_msg = response.get("message", "Terjadi kesalahan tidak diketahui")
            raise Exception(f"[{error_code}] {error_msg}")
    except Exception as e:
        print(f"[Error] Gagal Integrasi: {e}")
        return None