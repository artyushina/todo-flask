from flask import Flask, render_template, request, redirect, url_for
import database

# Инициализируем приложение Flask
app = Flask(__name__)

# Создаём таблицу при запуске (если ещё нет)
database.init_db()

@app.route('/')
def index():
    """Главная страница: отображает все задачи."""
    tasks = database.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    """Добавляет новую задачу."""
    task_text = request.form.get('task')
    if task_text and task_text.strip():
        database.add_task(task_text.strip())
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    """Удаляет задачу."""
    database.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    """Переключает статус задачи."""
    database.toggle_task(task_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    """Редактирует текст задачи (приходит из формы)."""
    new_text = request.form.get('task')
    if new_text and new_text.strip():
        database.update_task(task_id, new_text.strip())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)