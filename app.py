import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd

df = pd.read_excel("CF_new.xlsx")

questions_page2 = df.loc[0:0, "Qs"].tolist()
cf_values_page2 = df.loc[0:0, "CF"].tolist()
code_page2 = df.loc[0:0, "code"].tolist()
questions_page3 = df.loc[1:9, "Qs"].tolist()
cf_values_page3 = df.loc[1:9, "CF"].tolist()
code_page3 = df.loc[1:9, "code"].tolist()
questions_page4 = df.loc[10:21, "Qs"].tolist()
cf_values_page4 = df.loc[10:21, "CF"].tolist()
code_page4 = df.loc[10:21, "code"].tolist()
questions_page5 = df.loc[28:31, "Qs"].tolist()
cf_values_page5 = df.loc[28:31, "CF"].tolist()
code_page5 = df.loc[28:31, "code"].tolist()
questions_page6 = df.loc[22:27, "Qs"].tolist()
cf_values_page6 = df.loc[22:27, "CF"].tolist()
code_page6 = df.loc[22:27, "code"].tolist()
questions_page7 = df.loc[32:35, "Qs"].tolist()
cf_values_page7 = df.loc[32:35, "CF"].tolist()
code_page7 = df.loc[32:35, "code"].tolist()
questions_page8 = df.loc[36:40, "Qs"].tolist()
cf_values_page8 = df.loc[36:40, "CF"].tolist()
code_page8 = df.loc[36:40, "code"].tolist()
questions_page9 = df.loc[41:42, "Qs"].tolist()
cf_values_page9 = df.loc[41:42, "CF"].tolist()
code_page9 = df.loc[41:42, "code"].tolist()
questions_page10 = df.loc[43:47, "Qs"].tolist()
cf_values_page10 = df.loc[43:47, "CF"].tolist()
code_page10 = df.loc[43:47, "code"].tolist()
questions_page11 = df.loc[48:57, "Qs"].tolist()
cf_values_page11 = df.loc[48:57, "CF"].tolist()
code_page11 = df.loc[48:57, "code"].tolist()
questions_page12 = df.loc[58:67, "Qs"].tolist()
cf_values_page12 = df.loc[58:67, "CF"].tolist()
code_page12 = df.loc[58:67, "code"].tolist()
questions_page13 = df.loc[68:71, "Qs"].tolist()
cf_values_page13 = df.loc[68:71, "CF"].tolist()
code_page13 = df.loc[68:71, "code"].tolist()

# Basis Pengetahuan
knowledge_base = {
    "Banjir": [
        "W2",
        "R1",
        "R2",
        "R3",
        "R4",
        "R5",
        "R6",
        "R7",
        "R8",
        "R10",
        "L1",
        "L2",
        "L4",
        "L9",
        "L11",
        "L12",
        "J1.1J",
        "J1.2",
        "J1.3",
        "J1.4",
        "J1.5",
        "J1.6",
    ],
    "Gelombang Tinggi": [
        "C1",
        "C2",
        "C3",
        "C4",
        "R5",
        "R6",
        "L1",
        "L2",
        "L4",
        "L11",
        "J3.1",
        "J3.2",
        "J3.4",
        "J3.5",
    ],
    "Tsunami": [
        "C1",
        "C2",
        "C3",
        "C4",
        "R5",
        "R6",
        "L1",
        "L2",
        "L4",
        "L11",
        "J2.1",
        "J2.2",
        "J2.3",
        "J2.4",
        "J2.5",
    ],
    "Longsor": [
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "L6",
        "L7",
        "L8",
        "L9",
        "L10",
        "L11",
        "L12",
        "G1",
        "G2",
        "G3",
        "G4",
        "V1",
        "V2",
        "J4.1",
        "J4.2",
        "J4.3",
        "J4.4",
        "J4.5",
    ],
    "Gempa Bumi": [
        "J5.1",
        "J5.2",
        "J5.3",
        "J5.4",
        "J5.5",
        "J5.6",
        "J5.7",
        "J5.8",
        "J5.9",
        "J5.10",
    ],
    "Gunung Api Meletus": [
        "J6.1",
        "J6.2",
        "J6.3",
        "J6.4",
        "J6.5",
        "J6.6",
        "J6.7",
        "J6.8",
        "J6.9",
        "J6.10",
    ],
}

solution = {
    "Banjir": "1. Pastikan adanya sistem drainase yang baik dan terawat.\n2. Membangun tanggul dan penampungan air untuk mengurangi risiko banjir.\n3. Lakukan reboisasi di daerah hulu sungai untuk menjaga keseimbangan ekosistem.\n4. Evakuasi ke daerah yang lebih tinggi saat banjir terjadi.\n5. Simpan makanan dan air bersih dalam kemasan kedap udara.\n6. Hindari mengkonsumsi makanan dan air yang terkontaminasi setelah banjir.\n7. Laporkan kerusakan dan kebutuhan bantuan kepada otoritas setempat.",
    "Gelombang Tinggi": "1. Pasang peringatan dini untuk masyarakat pesisir terkait potensi gelombang tinggi.\n2. Membangun infrastruktur yang tahan gelombang tinggi, seperti penahan gelombang.\n3. Evakuasi ke tempat yang lebih aman saat gelombang tinggi terjadi.\n4. Hindari berada di dekat pantai atau tepi laut saat peringatan diberikan.\n5. Ikuti instruksi dari otoritas lokal terkait keamanan dan evakuasi.\n6. Lakukan penilaian kerusakan dan bantu masyarakat yang terdampak setelah gelombang surut.\n7. Siapkan peralatan darurat dan perlengkapan evakuasi untuk setiap keluarga.",
    "Tsunami": "1. Membangun sistem peringatan dini tsunami di daerah rawan.\n2. Identifikasi dan buat rencana evakuasi untuk komunitas pesisir.\n3. Segera evakuasi ke daerah tinggi saat ada peringatan tsunami.\n4. Jangan kembali ke pantai sampai diberitahu aman oleh pihak berwenang.\n5. Lindungi diri dari debu dan kontaminasi setelah tsunami.\n6. Laporkan kerusakan infrastruktur dan kebutuhan bantuan kepada pihak berwenang.\n7. Berikan dukungan kepada komunitas yang terdampak untuk proses pemulihan.",
    "Longsor": "1. Membangun tembok penahan dan drainase untuk mencegah longsor.\n2. Melakukan survei geologi untuk mengidentifikasi daerah rawan longsor.\n3. Evakuasi segera jika ada tanda-tanda longsor (retakan tanah, suara gemuruh).\n4. Hindari area di bawah lereng yang curam saat hujan deras.\n5. Laporkan kerusakan ke otoritas setempat setelah longsor terjadi.\n6. Berikan informasi kepada masyarakat tentang cara mengenali tanda-tanda longsor.\n7. Siapkan rencana evakuasi yang jelas untuk daerah yang berisiko longsor.",
    "Gempa Bumi": "1. Mengembangkan bangunan tahan gempa sesuai dengan standar yang ditetapkan.\n2. Melakukan latihan evakuasi secara berkala untuk masyarakat.\n3. Berlindung di bawah meja atau struktur yang kuat saat gempa terjadi.\n4. Jangan menggunakan lift dan menjauh dari jendela saat gempa.\n5. Periksa diri dan orang di sekitar untuk cedera setelah gempa.\n6. Laporkan kerusakan dan kebutuhan bantuan kepada pihak berwenang.\n7. Siapkan kit darurat yang mencakup makanan, air, dan perlengkapan pertolongan pertama.",
    "Gunung Api Meletus": "1. Memantau aktivitas gunung berapi melalui lembaga geologi secara berkala.\n2. Mengembangkan rencana evakuasi untuk masyarakat sekitar gunung berapi.\n3. Ikuti instruksi evakuasi dan pergi ke tempat yang aman saat letusan terjadi.\n4. Lindungi pernapasan dari abu vulkanik dengan masker atau kain.\n5. Hindari mengonsumsi makanan yang terkontaminasi debu vulkanik setelah letusan.\n6. Laporkan kerusakan dan kebutuhan bantuan kepada pihak berwenang.\n7. Berikan dukungan kepada masyarakat yang terkena dampak dalam proses pemulihan.",
}


# Fungsi untuk membuat checkbox
def create_checkbuttons(root, questions, variable_list):
    checkbuttons = []
    for i, question in enumerate(questions):
        var = tk.BooleanVar()
        variable_list.append(var)
        checkbutton = tk.Checkbutton(
            root,
            text=question,
            variable=var,
            font=("Arial", 14, "bold"),
            bg="#f0f0f5" if len(variable_list) == 4 else "#e6f2ff",
            fg="#333",
            activebackground="#d9d9f2" if len(variable_list) == 4 else "#b3daff",
            activeforeground="#000",
            selectcolor="#99ccff",
            width=100,
            padx=10,
            pady=2,
            relief="ridge",
            bd=2,
            anchor="w",
        )
        checkbuttons.append(checkbutton)
    return checkbuttons


def calculate_certainty_factor(selected_codes):
    disaster_cf = {}

    # Mengambil daftar CF dari DataFrame
    cf_values = df["CF"].tolist()  # Ambil seluruh daftar CF dari DataFrame

    for disaster, codes in knowledge_base.items():
        cf_total = 0

        for code in codes:
            if code in selected_codes:
                # Ambil index kode dalam daftar
                index = codes.index(code)

                # Pastikan index tidak keluar dari rentang cf_values
                if index < len(cf_values):
                    if cf_total == 0:
                        cf_total = cf_values[index]  # Inisialisasi CF total
                    else:
                        # Perhitungan CF baru
                        cf_total = cf_total + cf_values[index] * (1 - cf_total)

        # Pastikan CF total valid sebelum menyimpannya
        if cf_total > 0:
            disaster_cf[disaster] = cf_total * 100  # Ubah ke persen

    return disaster_cf


# Fungsi untuk memeriksa hasil dan menampilkan di halaman terakhir
def show_results():
    selected_codes = set()  # Menggunakan set untuk menghindari duplikasi
    for i, var in enumerate(check_vars_page2):
        if var.get():
            selected_codes.add(code_page2[i])
    for i, var in enumerate(check_vars_page3):
        if var.get():
            selected_codes.add(code_page3[i])
    for i, var in enumerate(check_vars_page4):
        if var.get():
            selected_codes.add(code_page4[i])
    for i, var in enumerate(check_vars_page5):
        if var.get():
            selected_codes.add(code_page5[i])
    for i, var in enumerate(check_vars_page6):
        if var.get():
            selected_codes.add(code_page6[i])
    for i, var in enumerate(check_vars_page7):
        if var.get():
            selected_codes.add(code_page7[i])
    for i, var in enumerate(check_vars_page8):
        if var.get():
            selected_codes.add(code_page8[i])
    for i, var in enumerate(check_vars_page9):
        if var.get():
            selected_codes.add(code_page9[i])
    for i, var in enumerate(check_vars_page10):
        if var.get():
            selected_codes.add(code_page10[i])
    for i, var in enumerate(check_vars_page11):
        if var.get():
            selected_codes.add(code_page11[i])
    for i, var in enumerate(check_vars_page12):
        if var.get():
            selected_codes.add(code_page12[i])
    for i, var in enumerate(check_vars_page13):
        if var.get():
            selected_codes.add(code_page13[i])

    disaster_cf = calculate_certainty_factor(selected_codes)

    results_text = "Kemungkinan bencana dan persentase:\n"
    solutions_text = ""
    if disaster_cf:
        for disaster, cf in disaster_cf.items():
            results_text += (
                f"{disaster}: {cf:.2f}%\n"  # Tampilkan CF terpisah per bencana
            )

            # Menambahkan solusi untuk setiap bencana yang terdeteksi
            if disaster in solution:
                solutions_text += f"Solusi untuk {disaster}:\n{solution[disaster]}\n\n"
    else:
        results_text += "Tidak ada bencana yang terdeteksi."
        solutions_text = (
            "Solusi tidak tersedia karena tidak ada bencana yang terdeteksi."
        )

    results_label.config(text=results_text, anchor="ne", justify="left")

    solutions_label.config(text=solutions_text, anchor="nw", justify="left")


# Fungsi untuk beralih ke halaman berikutnya
def next_page():
    global current_page
    if current_page == 12:  # Jika sudah di halaman sebelum terakhir, tampilkan hasil
        show_results()
    current_page += 1
    if current_page > 13:
        current_page = 13
    update_page()


# Fungsi untuk beralih ke halaman sebelumnya
def previous_page():
    global current_page
    current_page -= 1
    if current_page < 0:
        current_page = 0
    update_page()


# Fungsi untuk memperbarui tampilan halaman
def update_page():
    canvas.itemconfig(bg_image, image=background_images[current_page])

    if current_page == 1:  # Page 2
        question_label_page2.place(x=720, y=160, anchor="center")
        for i, cb in enumerate(check_buttons_page2):
            cb.place(x=720, y=220 + i * 40, anchor="center")
    else:
        question_label_page2.place_forget()
        for cb in check_buttons_page2:
            cb.place_forget()

    if current_page == 2:  # Page 3
        question_label_page3.place(x=720, y=160, anchor="center")
        for i, cb in enumerate(check_buttons_page3):
            cb.place(x=720, y=220 + i * 40, anchor="center")
    else:
        question_label_page3.place_forget()
        for cb in check_buttons_page3:
            cb.place_forget()

    if current_page == 3:  # Page 4
        question_label_page4.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page4):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page4.place_forget()
        for cb in check_buttons_page4:
            cb.place_forget()

    if current_page == 4:  # Page 4
        question_label_page5.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page5):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page5.place_forget()
        for cb in check_buttons_page5:
            cb.place_forget()

    if current_page == 5:  # Page 4
        question_label_page6.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page6):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page6.place_forget()
        for cb in check_buttons_page6:
            cb.place_forget()

    if current_page == 6:  # Page 4
        question_label_page7.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page7):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page7.place_forget()
        for cb in check_buttons_page7:
            cb.place_forget()

    if current_page == 7:  # Page 4
        question_label_page8.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page8):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page8.place_forget()
        for cb in check_buttons_page8:
            cb.place_forget()

    if current_page == 8:  # Page 4
        question_label_page9.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page9):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page9.place_forget()
        for cb in check_buttons_page9:
            cb.place_forget()

    if current_page == 9:  # Page 4
        question_label_page10.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page10):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page10.place_forget()
        for cb in check_buttons_page10:
            cb.place_forget()

    if current_page == 10:  # Page 4
        question_label_page11.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page11):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page11.place_forget()
        for cb in check_buttons_page11:
            cb.place_forget()

    if current_page == 11:  # Page 4
        question_label_page12.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page12):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page12.place_forget()
        for cb in check_buttons_page12:
            cb.place_forget()

    if current_page == 12:  # Page 4
        question_label_page13.place(x=720, y=100, anchor="center")
        for i, cb in enumerate(check_buttons_page13):
            cb.place(x=720, y=160 + i * 40, anchor="center")
    else:
        question_label_page13.place_forget()
        for cb in check_buttons_page13:
            cb.place_forget()

    if current_page == 13:  # Halaman terakhir
        results_label.place(x=100, y=110, anchor="nw")
        solutions_label.place(x=490, y=110, anchor="nw")
    else:
        results_label.place_forget()
        solutions_label.place_forget()


# Inisialisasi aplikasi
root = tk.Tk()
root.geometry("1440x760")
root.title("Multi-page Application")

# Load background images
background_images = []
for i in range(1, 15):  # Loop untuk memuat 7 gambar background yang berbeda
    image = Image.open(f"bg_{i}.png")
    image = image.resize((1440, 760))
    background_image = ImageTk.PhotoImage(image)
    background_images.append(background_image)

# Canvas untuk menampilkan gambar background
canvas = tk.Canvas(root, width=1440, height=760)
canvas.pack(fill="both", expand=True)

# Menambahkan gambar background ke setiap page
bg_image = canvas.create_image(0, 0, anchor="nw", image=background_images[0])

# Load images for buttons with transparency
next_image = Image.open("next_btn.png").convert("RGBA")
next_image = next_image.resize((90, 50))
next_photo = ImageTk.PhotoImage(next_image)

prev_image = Image.open("back_btn.png").convert("RGBA")
prev_image = prev_image.resize((90, 50))
prev_photo = ImageTk.PhotoImage(prev_image)

# Button navigasi
next_button = tk.Button(root, image=next_photo, command=next_page, bg="#f0f0f5", bd=0)
next_button.place(x=1300, y=700)

prev_button = tk.Button(
    root, image=prev_photo, command=previous_page, bg="#f0f0f5", bd=0
)
prev_button.place(x=1200, y=700)

# Konten untuk Page 2 (pertanyaan dan checkbox)
question_label_page2 = tk.Label(
    root, text="Cuaca dan Musim", font=("Arial", 18), bg="#f0f0f5", fg="#333"
)
check_vars_page2 = []
check_buttons_page2 = create_checkbuttons(root, questions_page2, check_vars_page2)

# Konten untuk Page 3 (pertanyaan dan checkbox)
question_label_page3 = tk.Label(
    root,
    text="Karakteristik Geografis Sungai dan Ngarai",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page3 = []
check_buttons_page3 = create_checkbuttons(root, questions_page3, check_vars_page3)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page4 = tk.Label(
    root,
    text="Karakteristik Lahan dan Lereng",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page4 = []
check_buttons_page4 = create_checkbuttons(root, questions_page4, check_vars_page4)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page5 = tk.Label(
    root,
    text="Karakteristik Pantai dan Wilayah Pesisir",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page5 = []
check_buttons_page5 = create_checkbuttons(root, questions_page5, check_vars_page5)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page6 = tk.Label(
    root,
    text="Bentukan Lahan dan Morfologi Wilayah",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page6 = []
check_buttons_page6 = create_checkbuttons(root, questions_page6, check_vars_page6)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page7 = tk.Label(
    root,
    text="Risiko Ekstrem",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page7 = []
check_buttons_page7 = create_checkbuttons(root, questions_page7, check_vars_page7)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page8 = tk.Label(
    root,
    text="Ancaman Tsunami dan Infrastruktur",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page8 = []
check_buttons_page8 = create_checkbuttons(root, questions_page8, check_vars_page8)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page9 = tk.Label(
    root,
    text="Kondisi Vegetasi dan Penggunaan Lahan",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page9 = []
check_buttons_page9 = create_checkbuttons(root, questions_page9, check_vars_page9)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page10 = tk.Label(
    root,
    text="Risiko Longsor dan Kestabilan Lereng",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page10 = []
check_buttons_page10 = create_checkbuttons(root, questions_page10, check_vars_page10)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page11 = tk.Label(
    root,
    text="Risiko Seismik dan Gempa Bumi",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page11 = []
check_buttons_page11 = create_checkbuttons(root, questions_page11, check_vars_page11)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page12 = tk.Label(
    root,
    text="Aktivitas Vulkanik",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page12 = []
check_buttons_page12 = create_checkbuttons(root, questions_page12, check_vars_page12)

# Konten untuk Page 4 (pertanyaan dan checkbox)
question_label_page13 = tk.Label(
    root,
    text="Klasifikasi Geologi dan Struktur Tanah",
    font=("Arial", 18),
    bg="#f0f0f5",
    fg="#333",
)
check_vars_page13 = []
check_buttons_page13 = create_checkbuttons(root, questions_page13, check_vars_page13)

results_label = tk.Label(root, text="", font=("Arial", 14), bg="#e6f2ff", fg="#333")
solutions_label = tk.Label(root, text="", font=("Arial", 14), bg="#e6f2ff", fg="#333")

# Variabel untuk melacak halaman saat ini
current_page = 0

# Menampilkan halaman pertama
update_page()

# Menjalankan aplikasi
root.mainloop()
