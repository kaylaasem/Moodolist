class DailyBoard:
    """Kelas untuk menggabungkan To-Do List dan Habit Generator"""
    
    def __init__(self, todo_list, habit_generator):
        self.todo_list = todo_list
        self.habit_generator = habit_generator
    
    def get_all_tasks(self):
        """Gabungkan to-do dan habit untuk ditampilkan"""
        todos = self.todo_list.get_all_todos()
        daily_habits = self.habit_generator.get_daily_habits()
        return todos + daily_habits
    
    def get_progress(self):
        """Hitung progress penyelesaian task"""
        all_tasks = self.get_all_tasks()
        
        if not all_tasks:
            return 0, 0, 0.0
        
        total = len(all_tasks)
        completed = sum(1 for task in all_tasks if task['completed'])
        percentage = (completed / total * 100) if total > 0 else 0.0
        
        return completed, total, percentage
    
    def toggle_task(self, task_id):
        """Toggle status task (otomatis deteksi to-do atau habit)"""
        if self.todo_list.toggle_todo(task_id):
            return True
        if self.habit_generator.toggle_daily_habit(task_id):
            return True
        return False
    
    def get_task_summary(self):
        """Ringkasan task hari ini"""
        completed, total, percentage = self.get_progress()
        all_tasks = self.get_all_tasks()
        
        todos = [t for t in all_tasks if not t['is_habit']]
        habits = [t for t in all_tasks if t['is_habit']]
        
        return {
            'total_tasks': total,
            'completed_tasks': completed,
            'percentage': percentage,
            'total_todos': len(todos),
            'total_habits': len(habits),
            'completed_todos': sum(1 for t in todos if t['completed']),
            'completed_habits': sum(1 for t in habits if t['completed'])
        }
    
    def get_tasks_by_category(self):
        """Ambil task yang dikelompokkan berdasarkan kategori"""
        all_tasks = self.get_all_tasks()
        
        todos = [t for t in all_tasks if not t['is_habit']]
        habits = [t for t in all_tasks if t['is_habit']]
        
        return {
            'todos': todos,
            'habits': habits
        }