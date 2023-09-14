import sqlite3

connection = sqlite3.connect('todo.db', check_same_thread=False)

cursor = connection.cursor()

def create_table():
	cursor.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT, task_status TEXT, task_due_date DATE)')

def add_data(task, task_status, task_due_date):
	cursor.execute('INSERT INTO taskstable(task, task_status, task_due_date) VALUES (?,?,?)', (task, task_status, task_due_date))
	connection.commit()

def view_all_data():
	cursor.execute('SELECT * FROM taskstable')
	result = cursor.fetchall()
	return result

def view_all_task_names():
	cursor.execute('SELECT DISTINCT task FROM taskstable')
	result = cursor.fetchall()
	return result

def get_task(task):
	cursor.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
	result = cursor.fetchall()
	return result

def get_task_by_status(task_status):
	cursor.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
	result = cursor.fetchall()

def edit_task_data(new_task, new_task_status, new_task_date, task,task_status, task_due_date):
	cursor.execute("UPDATE taskstable SET task =?, task_status=?, task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",
                (new_task, new_task_status, new_task_date, task, task_status, task_due_date))
	connection.commit()
	result = cursor.fetchall()
	return result

def delete_data(task):
	cursor.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
	connection.commit()