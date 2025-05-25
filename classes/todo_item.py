import pyodbc

task_dict = {}

class todo_manager:

    @staticmethod
    def complete(id):
        with pyodbc.connect('DSN=tododb') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", id)
            conn.commit()

    @staticmethod
    def create(task: str):
        with pyodbc.connect('DSN=tododb') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
            conn.commit()

    @staticmethod
    def delete_all():
        with pyodbc.connect('DSN=tododb') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks")
            conn.commit()


    @staticmethod
    def get_all():
        with pyodbc.connect('DSN=tododb') as conn:
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



