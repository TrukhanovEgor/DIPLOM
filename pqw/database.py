import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Создание таблицы users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    ''')

    # Создание таблицы workouts
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        workout_name TEXT NOT NULL,
        exercise_name TEXT NOT NULL,
        sets_count INTEGER,
        reps_count INTEGER,
        muscle_group TEXT
    )
    ''')

    # Проверка схемы таблицы measurements
    cursor.execute("PRAGMA table_info(measurements)")
    columns = [info[1] for info in cursor.fetchall()]

    if 'body_part' in columns:
        # Создаем временную таблицу с правильной схемой
        cursor.execute('''
        CREATE TABLE measurements_temp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            parameter TEXT NOT NULL,
            date TEXT NOT NULL,
            value REAL NOT NULL,
            FOREIGN KEY (username) REFERENCES users (username)
        )
        ''')

        # Переносим данные из старой таблицы, используя parameter вместо body_part
        cursor.execute('''
        INSERT INTO measurements_temp (id, username, parameter, date, value)
        SELECT id, username, body_part, date, value FROM measurements
        ''')

        # Удаляем старую таблицу
        cursor.execute('DROP TABLE measurements')

        # Переименовываем временную таблицу
        cursor.execute('ALTER TABLE measurements_temp RENAME TO measurements')

    else:
        # Создаем таблицу measurements, если она еще не существует
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            parameter TEXT NOT NULL,
            date TEXT NOT NULL,
            value REAL NOT NULL,
            FOREIGN KEY (username) REFERENCES users (username)
        )
        ''')

    conn.commit()
    conn.close()

def register_user(username, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def user_exists(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def save_workout(username, workout_name, exercise_name, sets_count, reps_count, muscle_group):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO workouts (username, workout_name, exercise_name, sets_count, reps_count, muscle_group) VALUES (?, ?, ?, ?, ?, ?)",
        (username, workout_name, exercise_name, sets_count, reps_count, muscle_group)
    )
    conn.commit()
    conn.close()

def get_user_workouts(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT workout_name, exercise_name, sets_count, reps_count, muscle_group FROM workouts WHERE username = ?", (username,))
    workouts = cursor.fetchall()
    conn.close()
    return workouts

def get_user_statistics(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(DISTINCT workout_name),
               COUNT(*),
               SUM(sets_count)
        FROM workouts
        WHERE username = ?
    """, (username,))
    result = cursor.fetchone()
    conn.close()
    workout_count = result[0] or 0
    exercise_count = result[1] or 0
    total_sets = result[2] or 0
    return workout_count, exercise_count, total_sets

def save_measurement(username, parameter, date, value):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO measurements (username, parameter, date, value) VALUES (?, ?, ?, ?)",
        (username, parameter, date, value)
    )
    conn.commit()
    conn.close()

def get_user_measurements(username, parameter):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT date, value FROM measurements WHERE username = ? AND parameter = ? ORDER BY date",
            (username, parameter)
        )
        measurements = cursor.fetchall()
        conn.close()
        return measurements
    except sqlite3.OperationalError as e:
        print(f"Ошибка базы данных: {e}")
        return []