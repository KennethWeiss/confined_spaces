from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Space:
    db = "confined_spaces"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """INSERT INTO confined_spaces (name) 
                VALUES (%(name)s);"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def get_spaces(cls):
        query = "SELECT * from confined_spaces;"
        results = connectToMySQL(cls.db).query_db(query)
        spaces = []
        for space in results:
            print(space)
            spaces.append(cls(space))
        return spaces

    @classmethod
    def get_users_spaces(cls):
        query = """
                SELECT confined_spaces.id, confined_spaces.name, confined_spaces.created_at, confined_spaces.updated_at FROM confined_spaces.confined_spaces
                JOIN confined_spaces.users_has_confined_spaces
                ON confined_spaces.confined_spaces.id = users_has_confined_spaces.confined_space_id
                JOIN users
                ON users_has_confined_spaces.user_id = users.id;
                """
        results = connectToMySQL(cls.db).query_db(query)
        spaces = []
        for space in results:
            spaces.append(cls(space))
        return spaces
    
    @classmethod
    def create_space(cls, data):
        query = """
                INSERT INTO confined_spaces (name) 
                VALUES (%(name)s);
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @staticmethod
    def is_valid(user_dict):
        is_valid = True
        if len(user_dict["first_name"]) < 2:
            is_valid = False
            flash("First name should have at least 2 characters", "registration")
        if len(user_dict["last_name"]) < 2:
            is_valid = False
            flash("Last name should have at least 2 characters", "registration")
        if len(user_dict["email"]) < 2:
            is_valid = False
            flash("Email should have at least 2 characters", "registration")
        if len(user_dict["password"]) < 2:
            is_valid = False
            flash("Password should have at least 2 characters", "registration")
        if user_dict["password_confirmation"] != user_dict["password"]:
            is_valid = False
            flash("Password must match password confirmation", "registration")
        return is_valid
    
    @staticmethod
    def valid_login(user_dict):
        is_valid = True
        if len(user_dict["email"]) < 2:
            is_valid = False
            flash("Email should have at least 2 characters")
        if len(user_dict["password"]) < 2:
            is_valid = False
            flash("Password should have at least 2 characters")
        # if user_dict["password_confirmation"] != user_dict["password"]:
        #     is_valid = False
        #     flash("Password must match password confirmation")
        return is_valid 