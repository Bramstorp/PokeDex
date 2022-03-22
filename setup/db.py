import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_pokemon_table = """
CREATE TABLE pokemon (
  pokemon_id INT PRIMARY KEY,
  height INT,
  weight INT,
  name VARCHAR(50) NOT NULL,
  img BLOB,
  hp INT,
  attack INT,
  defense INT,
  speed INT, 
  special_attack VARCHAR(50),
  special_defense VARCHAR(50),
  abilities INT,
  types INT
);
"""

create_abilities_table = """
CREATE TABLE abilities (
  abilities_id INT PRIMARY KEY,
  abilitie VARCHAR(50)
);
"""

create_types_table = """
CREATE TABLE types (
  types_id INT PRIMARY KEY,
  name VARCHAR(50)
);
"""

alter_pokemon = """
ALTER TABLE pokemon
ADD FOREIGN KEY(abilities)
REFERENCES abilities(abilities_id)
ON DELETE SET NULL;
"""

alter_pokemon_again = """
ALTER TABLE pokemon
ADD FOREIGN KEY(types)
REFERENCES types(types_id)
ON DELETE SET NULL;
"""
connection = create_db_connection("localhost", "root", "password", "db") 
execute_query(connection, create_pokemon_table)
execute_query(connection, create_abilities_table)
execute_query(connection, create_types_table)

execute_query(connection, alter_pokemon)
execute_query(connection, alter_pokemon_again)