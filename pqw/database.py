import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
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