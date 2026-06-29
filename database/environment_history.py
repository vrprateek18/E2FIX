# ==========================================================
# ENVIRONMENT HISTORY DATABASE
# ==========================================================

import sqlite3
from datetime import datetime

# ==========================================================
# DATABASE CONNECTION
# ==========================================================

DB_PATH = "db/environment_history.db"


def get_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn

# ==========================================================
# CREATE TABLE
# ==========================================================

def init_environment_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS environment_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        location TEXT,

        latitude REAL,

        longitude REAL,

        aqi INTEGER,
        
        temperature REAL,

        humidity REAL,

        wind REAL,

        green TEXT,

        noise TEXT,

        water TEXT,

        waste TEXT,

        heat TEXT,

        environmental_score REAL,

        projected_score REAL,

        carbon_saved REAL,

        carbon_credits REAL,

        recovery_bonus REAL,

        created_at TEXT

    )
    """)

    conn.commit()

    conn.close()

# ==========================================================
# SAVE RECORD
# ==========================================================

def save_environment_record(data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO environment_history(

        location,

        latitude,

        longitude,

        aqi,
        
        temperature,

        humidity,

        wind,

        green,

        noise,

        water,

        waste,

        heat,

        environmental_score,

        projected_score,

        carbon_saved,

        carbon_credits,

        recovery_bonus,

        created_at

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    """,(

        data["location"],

        data["latitude"],

        data["longitude"],

        data["aqi"],
        
        data["temperature"],

        data["humidity"],

        data["wind"],

        data["green"],

        data["noise"],

        data["water"],

        data["waste"],

        data["heat"],

        data["environmental_score"],

        data["projected_score"],

        data["carbon_saved"],

        data["carbon_credits"],

        data["recovery_bonus"],

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    conn.commit()

    conn.close()


# ==========================================================
# GET HISTORY
# ==========================================================

def get_environment_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM environment_history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

# ==========================================================
# LATEST RECORD
# ==========================================================

def latest_environment():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM environment_history

    ORDER BY id DESC

    LIMIT 1

    """)

    row = cursor.fetchone()

    conn.close()

    return row


# ==========================================================
# GET LATEST RECORD ID
# ==========================================================

def get_latest_record():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM environment_history

        ORDER BY id DESC

        LIMIT 1

    """)

    row = cursor.fetchone()

    conn.close()

    return row

# ==========================================================
# LOCATION HISTORY
# ==========================================================

def location_history(location):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM environment_history

    WHERE location=?

    ORDER BY id DESC

    """,(location,))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================================
# UPDATE RECOVERY DATA
# ==========================================================

def update_recovery(

    record_id,

    carbon_saved,

    carbon_credits,

    recovery_bonus,

    projected_score

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE environment_history

        SET

            carbon_saved=?,

            carbon_credits=?,

            recovery_bonus=?,

            projected_score=?

        WHERE id=?

    """,(

        carbon_saved,

        carbon_credits,

        recovery_bonus,

        projected_score,

        record_id

    ))

    conn.commit()

    conn.close()

# ==========================================================
# INITIALIZE
# ==========================================================

init_environment_db()

