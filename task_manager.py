# CT_SD_03 - Task Manager CRUD Application
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        print("\n--- Add New Task ---")
        title = input("Title: ").strip()
        description = input("Description: ").strip()
        due_date = input("Due Date (DD-MM-YYYY): ").strip()
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        print(f"✅ Task '{title}' added successfully!")
    
    def view_tasks(self):
        print("\n--- All Tasks ---")
        if not self.tasks:
            print("No tasks found.")
            return
        
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"{task['id']}. [{status}] {task['title']} (Due: {task['due_date']})")
            print(f"   Description: {task['description']}\n")
    
    def update_task(self):
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to update: ")) - 1
            if 0 <= task_id < len(self.tasks):
                print(f"\nUpdating Task {task_id + 1}:")
                self.tasks[task_id]["title"] = input(f"Title [{self.tasks[task_id]['title']}]: ") or self.tasks[task_id]["title"]
                self.tasks[task_id]["description"] = input(f"Description [{self.tasks[task_id]['description']}]: ") or self.tasks[task_id]["description"]
                self.tasks[task_id]["due_date"] = input(f"Due Date [{self.tasks[task_id]['due_date']}]: ") or self.tasks[task_id]["due_date"]
                self.tasks[task_id]["completed"] = input("Completed? (y/n): ").lower() == 'y'
                print("✅ Task updated successfully!")
            else:
                print("❌ Invalid task ID!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def delete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to delete: ")) - 1
            if 0 <= task_id < len(self.tasks):
                deleted_title = self.tasks[task_id]["title"]
                self.tasks.pop(task_id)
                # Reassign IDs
                for idx, task in enumerate(self.tasks, 1):
                    task["id"] = idx
                print(f"✅ Task '{deleted_title}' deleted successfully!")
            else:
                print("❌ Invalid task ID!")
        except ValueError:
            print("❌ Please enter a valid number!")

def main():
    manager = TaskManager()
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nSelect operation (1-5): ")
        
        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5")

if __name__ == "__main__":
    main()