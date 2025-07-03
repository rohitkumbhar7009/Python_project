# Q2. Explain Python memory management.

# Python uses automatic memory management with a garbage collector.

# Objects are managed using reference counting.

# The gc module can be used to manage memory manually.


# import gc
# print(gc.isenabled())

# --------------------------------------------------------------------
# 2. Data Structures

# Q3. Differentiate between List, Tuple, Set, and Dictionary.

# List: Ordered, mutable, allows duplicates.

# Tuple: Ordered, immutable.

# Set: Unordered, mutable, unique values.

# Dictionary: Key-value pairs, mutable.

# Example:
# lst = [1, 2, 3]
# tpl = (1, 2, 3)
# st = {1, 2, 3}
# dct = {'a': 1, 'b': 2}

# -------------------------------------------------------
# Q4. How would you remove duplicates from a list?

# lst = [1, 2, 2, 3, 4, 4]
# lst = list(set(lst))
# print(lst)

# --------------------------------------------------------------------
# 3. Functions and OOPs

# Q5. Explain the difference between @staticmethod, @classmethod, and instance methods.

# @staticmethod: Independent method, no access to class or instance.

# @classmethod: Takes class as the first argument (cls).

# Instance Method: Accesses class and instance variables using self.

# Example:

# class MyClass:
#     @staticmethod
#     def static_method():
#         print('Static Method')
    
#     @classmethod
#     def class_method(cls):
#         print(f'Class Method: {cls}')

# obj = MyClass()
# obj.static_method()
# obj.class_method()

# ----------------------------------------------------------------------------------------------
# Q6. How is exception handling done in Python?

# Use try-except blocks to handle exceptions.

# Use finally to execute code regardless of exceptions.

# Example:

# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(f'Error: {e}')
# finally:
#     print('Execution completed.')


# -------------------------------------------------------------------------------------------------
# 4. Real-Time Scenarios

# Q7. How would you optimize a Python code that reads large files?

# Read line by line using a generator.

# Use memory-efficient data structures.

# Example:
# with open('large_file.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# -------------------------------------------------------------------------------------------------------
# Q8. How do you connect to a database using Python?
# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM users')
# print(cursor.fetchall())

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# ''')


import sqlite3

# Connect to the database (It will create if not exists)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

print("Database and table created successfully.")

# Insert sample data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 28)")

conn.commit()
print("Data inserted successfully.")

# Fetch and display data
cursor.execute('SELECT * FROM users')
print("Users in the database:", cursor.fetchall())

# Close connection
conn.close()



# --------------------------------------------------------------------------------
# Q9. Explain how to create and use a REST API using Flask.

# from flask import Flask, jsonify
# app = Flask(__name__)

# @app.route('/api/greet', methods=['GET'])
# def greet():
#     return jsonify({'message': 'Hello, World!'})

# if __name__ == '__main__':
#     app.run(debug=True)

# -----------------------------------------------------------------------------------
# 5. Advanced Concepts

# Q10. What is the difference between deep copy and shallow copy?

# Shallow Copy: Creates a new object but inserts references to the original objects.

# Deep Copy: Creates a new object and recursively copies all objects.

# Example:
# import copy
# lst = [[1, 2], [3, 4]]
# deep_copy = copy.deepcopy(lst)
# shallow_copy = copy.copy(lst)

# print("deep_copy",deep_copy)
# print("shallow_copy" , shallow_copy)
