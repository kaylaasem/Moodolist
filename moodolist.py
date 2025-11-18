import json
import os
import random
from datetime import datetime

DATA_FILE = 'moodolist_data.json'
DEFAULT_HABITS = [
    'Minum 8 gelas air', 'Olahraga 15 menit', 'Membaca buku 20 halaman',
    'Meditasi 10 menit', 'Menulis jurnal', 'Stretching pagi',
    'Belajar hal baru 30 menit', 'Telepon teman/keluarga',
    'Bersih-bersih ruangan', 'Tidur sebelum jam 11'
]

class Moodolist:
    def __init__(self):
        self.todos = []
        self.habits = DEFAULT_HABITS.copy()
        self.daily_habits = []
        self.last_date = ''
        self.load_data()
        self.refresh_daily_habits()

    # ------------------ DATA HANDLING ------------------
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.todos = data.get('todos', [])
                self.habits = data.get('habits', DEFAULT_HABITS.copy())
                self.daily_habits = data.get('daily_habits', [])
                self.last_date = data.get('last_date', '')

    def save_data(self):
        data = {
            'todos': self.todos,
            'habits': self.habits,
            'daily_habits': self.daily_habits,
            'last_date': self.last_date
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # ------------------ HABIT SYSTEM ------------------
    def refresh_daily_habits(self):
        today = datetime.now().strftime('%Y-%m-%d')
        if self.last_date != today:
            self.daily_habits = [{'text': h, 'completed': False} for h in random.sample(self.habits, 3)]
            self.last_date = today
            self.save_data()

    def toggle_item(self, items, title):
        self.show_list(items, title)
        if not items:
            input('Tekan Enter untuk lanjut...')
            return
        try:
            idx = int(input('Pilih nomor (0 untuk batal): ')) - 1
            if 0 <= idx < len(items):
                items[idx]['completed'] = not items[idx]['completed']
                self.save_data()
                print('Berhasil diubah!')
        except:
            print('Input tidak valid!')
        input('Tekan Enter untuk lanjut...')

    # ------------------ DISPLAY ------------------
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_header(self):
        self.clear()
        print('=' * 50)
        print('✨         MOODOLIST - Wujudkan Hari Terbaikmu!         ✨')
        print('=' * 50, '\n')

    def show_list(self, items, title):
        print(title)
        print('-' * 50)
        if items:
            for i, item in enumerate(items, 1):
                status = '✅' if item.get('completed') else '⬜'
                print(f'{i}. {status} {item["text"]}')
        else:
            print('Belum ada data.')
        print()

    def show_progress(self):
        total_items = self.todos + self.daily_habits
        if not total_items:
            print('Belum ada tugas. Tambahkan tugas pertamamu!\n')
            return
        completed = sum(1 for x in total_items if x['completed'])
        total = len(total_items)
        progress = int((completed / total) * 100)
        print(f'Progress: {completed}/{total} ({progress}%)')
        bar = int(30 * progress / 100)
        print('[' + '█' * bar + '░' * (30 - bar) + ']\n')

    # ------------------ TODO FUNCTIONS ------------------
    def add_todo(self):
        text = input('Masukkan tugas baru: ').strip()
        if text:
            self.todos.append({'text': text, 'completed': False})
            self.save_data()
            print('Tugas ditambahkan!')
        else:
            print('Teks tidak boleh kosong!')
        input('Tekan Enter untuk lanjut...')

    def edit_todo(self):
        self.show_list(self.todos, 'Edit Tugas')
        try:
            idx = int(input('Pilih nomor (0 untuk batal): ')) - 1
            if 0 <= idx < len(self.todos):
                new = input('Teks baru: ').strip()
                if new:
                    self.todos[idx]['text'] = new
                    self.save_data()
                    print('Tugas diperbarui!')
        except:
            print('Input tidak valid!')
        input('Tekan Enter untuk lanjut...')

    def delete_todo(self):
        self.show_list(self.todos, 'Hapus Tugas')
        try:
            idx = int(input('Pilih nomor (0 untuk batal): ')) - 1
            if 0 <= idx < len(self.todos):
                print(f'Menghapus: {self.todos[idx]["text"]}')
                self.todos.pop(idx)
                self.save_data()
        except:
            print('Input tidak valid!')
        input('Tekan Enter untuk lanjut...')

    # ------------------ HABIT MANAGEMENT ------------------
    def manage_habits(self):
        while True:
            self.show_header()
            self.show_list([{"text": h} for h in self.habits], 'Daftar Habit')
            print('1. Tambah habit')
            print('2. Edit habit')
            print('3. Hapus habit')
            
            print('0. Kembali')
            choice = input('Pilih menu: ').strip()

            if choice == '1':
                text = input('Habit baru: ').strip()
                if text:
                    self.habits.append(text)
                    self.save_data()
            elif choice == '2':
                try:
                    idx = int(input('Nomor habit: ')) - 1
                    new = input('Teks baru: ').strip()
                    if 0 <= idx < len(self.habits) and new:
                        self.habits[idx] = new
                        self.save_data()
                except: pass
            elif choice == '3':
                try:
                    idx = int(input('Nomor habit: ')) - 1
                    if 0 <= idx < len(self.habits):
                        self.habits.pop(idx)
                        self.save_data()
                except: pass
            
            elif choice == '0':
                break

    # ------------------ MAIN LOOP ------------------
    def run(self):
        while True:
            self.show_header()
            self.show_progress()
            self.show_list(self.daily_habits, 'Habit Harian')
            self.show_list(self.todos, 'To-Do List')

            print('1. Toggle habit harian')
            print('2. Tambah tugas')
            print('3. Toggle tugas')
            print('4. Edit tugas')
            print('5. Hapus tugas')
            print('6. Kelola habit')
            print('0. Keluar')

            choice = input('Pilih menu: ').strip()

            if choice == '1': self.toggle_item(self.daily_habits, 'Habit Harian')
            elif choice == '2': self.add_todo()
            elif choice == '3': self.toggle_item(self.todos, 'To-Do List')
            elif choice == '4': self.edit_todo()
            elif choice == '5': self.delete_todo()
            elif choice == '6': self.manage_habits()
            elif choice == '0': break

if __name__ == '__main__':
    Moodolist().run()