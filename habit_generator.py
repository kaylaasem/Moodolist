import random
from datetime import datetime

class HabitGenerator:
    """Kelas untuk mengelola Random Habit Generator"""
    
    def __init__(self):
        self.habits = [
            'Minum 8 gelas air',
            'Olahraga 20 menit',
            'Membaca 10 halaman buku',
            'Meditasi 5 menit',
            'Berjalan kaki 15 menit',
            'Menulis jurnal',
            'Belajar hal baru 30 menit',
            'Bebersih ruangan',
            'Menghubungi teman/keluarga',
            'Peregangan tubuh',
            'Tidur 8 jam',
            'Makan sayur dan buah',
            'Mendengarkan musik',
            'Berlatih gratitude'
        ]
        self.daily_habits = []
        self.last_generated = None
        self.next_id = 1000
    
    def add_habit(self, habit_text):
        """Tambah habit baru ke daftar"""
        habit_text = habit_text.strip()
        if not habit_text or habit_text in self.habits:
            return False
        self.habits.append(habit_text)
        return True
    
    def edit_habit(self, old_habit, new_habit):
        """Edit habit yang ada"""
        new_habit = new_habit.strip()
        if not new_habit or new_habit in self.habits:
            return False
        if old_habit in self.habits:
            index = self.habits.index(old_habit)
            self.habits[index] = new_habit
            return True
        return False
    
    def delete_habit(self, habit_text):
        """Hapus habit dari daftar"""
        if habit_text in self.habits:
            self.habits.remove(habit_text)
            return True
        return False
    
    def generate_daily_habits(self, force=False):
        """Generate 1-3 habit acak untuk hari ini"""
        today = datetime.now().date()
        
        if not force and self.last_generated == today and self.daily_habits:
            return self.daily_habits
        
        if len(self.habits) == 0:
            self.daily_habits = []
            return []
        
        count = random.randint(1, min(3, len(self.habits)))
        selected_habits = random.sample(self.habits, count)
        
        self.daily_habits = []
        for habit in selected_habits:
            habit_item = {
                'id': self.next_id,
                'text': habit,
                'completed': False,
                'is_habit': True
            }
            self.daily_habits.append(habit_item)
            self.next_id += 1
        
        self.last_generated = today
        return self.daily_habits
    
    def get_habits_list(self):
        """Ambil daftar semua habit yang tersedia"""
        return self.habits.copy()
    
    def get_daily_habits(self):
        """Ambil habit yang sudah di-generate untuk hari ini"""
        return self.daily_habits.copy()
    
    def toggle_daily_habit(self, habit_id):
        """Toggle status habit hari ini"""
        for habit in self.daily_habits:
            if habit['id'] == habit_id:
                habit['completed'] = not habit['completed']
                return True
        return False
    
    def check_and_generate(self):
        """Cek tanggal dan auto-generate jika hari baru"""
        today = datetime.now().date()
        if self.last_generated != today:
            return self.generate_daily_habits()
        return self.daily_habits