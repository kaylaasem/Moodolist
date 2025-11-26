class TodoList:
    """Kelas untuk mengelola To-Do List"""
    
    def __init__(self):
        self.todos = []
        self.next_id = 1
    
    def add_todo(self, text):
        """Tambah tugas baru"""
        if not text.strip():
            return None
        
        todo = {
            'id': self.next_id,
            'text': text.strip(),
            'completed': False,
            'is_habit': False
        }
        self.todos.append(todo)
        self.next_id += 1
        return todo
    
    def delete_todo(self, todo_id):
        """Hapus tugas berdasarkan ID"""
        original_length = len(self.todos)
        self.todos = [t for t in self.todos if t['id'] != todo_id]
        return len(self.todos) < original_length
    
    def edit_todo(self, todo_id, new_text):
        """Edit tugas berdasarkan ID"""
        if not new_text.strip():
            return False
        
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['text'] = new_text.strip()
                return True
        return False
    
    def toggle_todo(self, todo_id):
        """Toggle status selesai/belum selesai"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = not todo['completed']
                return True
        return False
    
    def get_all_todos(self):
        """Ambil semua tugas"""
        return self.todos.copy()
    
    def get_todo_by_id(self, todo_id):
        """Ambil tugas berdasarkan ID"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                return todo
        return None