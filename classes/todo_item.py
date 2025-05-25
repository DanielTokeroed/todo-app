import pyodbc

task_dict = {}

class todo_manager:

    @staticmethod
    def complete(id):
        with pyodbc.connect('DSN=paginationdb') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", id)
            conn.commit()

    @staticmethod
    def create(task: str|None, id: int|None):
        with pyodbc.connect('DSN=paginationdb') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task, id) VALUES (?, ?)", task, id)
            conn.commit()

    @staticmethod
    def delete_all():
        with pyodbc.connect('DSN=paginationdb') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks")
            conn.commit()


    @staticmethod
    def get_all():
        with pyodbc.connect('DSN=paginationdb') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks t")
            rows = cursor.fetchall()

            for row in rows:
                task_item = {
                'id': row.id,
                'task': row.task
                }
                task_dict.append(task_item)
            return task_dict



