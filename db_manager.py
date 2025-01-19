import sqlite3
import face_recognition as frg

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    #drop table
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            regd_no VARCHAR(20),
            branch TEXT,
            student_type TEXT,
            course TEXT,
            college_name TEXT,
            student_image BLOB
        )
    """)
    conn.commit()
    conn.close()

# Register a new user
def register_user(name, email, regd_no, branch, student_type, course, college_name, student_image):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        # Read the image file as a binary stream
        if student_image is not None:
            student_image = student_image.read()

        cursor.execute("""
            INSERT INTO users (name, email, regd_no, branch, student_type, course, college_name, student_image) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, email, regd_no, branch, student_type, course, college_name, student_image))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

import io

def validate_user(email, uploaded_image):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Fetch the user's registered image based on email
    cursor.execute("SELECT student_image FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return None, "Email not found"

    # Convert binary data from the database into a file-like object
    registered_image_stream = io.BytesIO(result[0])

    try:
        # Load registered and uploaded images
        registered_image = frg.load_image_file(registered_image_stream)
        uploaded_image_stream = io.BytesIO(uploaded_image.read())
        uploaded_image = frg.load_image_file(uploaded_image_stream)

        # Generate face encodings
        registered_encoding = frg.face_encodings(registered_image)[0]
        uploaded_encoding = frg.face_encodings(uploaded_image)[0]

        # Compare face encodings
        match = frg.compare_faces([registered_encoding], uploaded_encoding, tolerance=0.5)

        if match[0]:
            return True, "Login successful"
        else:
            return False, "Face mismatch"
    except IndexError:
        return False, "Face not detected in one or both images"




def valid_user(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user