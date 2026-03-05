import sqlite3

DB_NAME = 'tasks.db'

def get_db_connection():
    """Создаёт соединение с базой данных и настраивает возврат строк как словари."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Создаёт таблицу tasks, если она ещё не существует."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def get_all_tasks():
    """Возвращает все задачи из базы."""
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return tasks

def add_task(task_text):
    """Добавляет новую задачу."""
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (task) VALUES (?)', (task_text,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Удаляет задачу по ID."""
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def toggle_task(task_id):
    """Переключает статус выполнения задачи."""
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = NOT completed WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, new_text):
    """Обновляет текст задачи."""
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_text, task_id))
    conn.commit()
    conn.close()