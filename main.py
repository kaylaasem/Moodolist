from Todo_list import TodoList
from habit_generator import HabitGenerator
from daily_board import DailyBoard

def show_menu():
    print("\n==========================")
    print("       DAILY BOARD")
    print("==========================")
    print("1. Tambah To-Do")
    print("2. Lihat Semua Task")
    print("3. Toggle Task (Selesai/Belum)")
    print("4. Generate Daily Habits")
    print("5. Lihat Ringkasan")
    print("6. Hapus To-Do")
    print("7. Edit To-Do")
    print("0. Keluar")
    print("==========================")

def main():
    todo_list = TodoList()
    habit_gen = HabitGenerator()
    board = DailyBoard(todo_list, habit_gen)

    while True:
        show_menu()
        choice = input("Pilih menu: ")

        # =======================
        # 1. Tambah To-Do
        # =======================
        if choice == "1":
            text = input("Masukkan tugas: ").strip()
            todo = todo_list.add_todo(text)
            if todo:
                print("✔ Tugas ditambahkan!")
            else:
                print("✖ Gagal menambah tugas.")

        # =======================
        # 2. Lihat Semua Task
        # =======================
        elif choice == "2":
            tasks = board.get_all_tasks()
            if not tasks:
                print("Belum ada task.")
            else:
                print("\n--- ALL TASKS TODAY ---")
                for t in tasks:
                    status = "✔" if t['completed'] else "✘"
                    jenis = "(Habit)" if t['is_habit'] else "(To-Do)"
                    print(f"{t['id']}. {t['text']} {jenis} [{status}]")

        # =======================
        # 3. Toggle Task
        # =======================
        elif choice == "3":
            try:
                task_id = int(input("Masukkan ID task: "))
                if board.toggle_task(task_id):
                    print("✔ Status berhasil diubah.")
                else:
                    print("✖ Task tidak ditemukan.")
            except ValueError:
                print("ID harus angka.")

        # =======================
        # 4. Generate Daily Habits
        # =======================
        elif choice == "4":
            habits = habit_gen.generate_daily_habits(force=True)
            print("\n✔ Generated Daily Habits:")
            for h in habits:
                print(f"{h['id']}. {h['text']}")

        # =======================
        # 5. Ringkasan
        # =======================
        elif choice == "5":
            summary = board.get_task_summary()
            print("\n--- TASK SUMMARY ---")
            print(f"Total tasks       : {summary['total_tasks']}")
            print(f"Completed         : {summary['completed_tasks']}")
            print(f"Progress          : {summary['percentage']:.2f}%")
            print("\nTo-Do: {}/{}".format(summary['completed_todos'], summary['total_todos']))
            print("Habit: {}/{}".format(summary['completed_habits'], summary['total_habits']))

        # =======================
        # 6. Hapus To-Do
        # =======================
        elif choice == "6":
            try:
                task_id = int(input("Masukkan ID To-Do: "))
                if todo_list.delete_todo(task_id):
                    print("✔ To-Do dihapus.")
                else:
                    print("✖ To-Do tidak ditemukan.")
            except ValueError:
                print("ID harus angka.")

        # =======================
        # 7. Edit To-Do
        # =======================
        elif choice == "7":
            try:
                task_id = int(input("Masukkan ID To-Do: "))
                new_text = input("Masukkan teks baru: ").strip()
                if todo_list.edit_todo(task_id, new_text):
                    print("✔ To-Do berhasil diedit.")
                else:
                    print("✖ Gagal mengedit To-Do.")
            except ValueError:
                print("ID harus angka.")

        # =======================
        # 0. Keluar
        # =======================
        elif choice == "0":
            print("Keluar...")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
