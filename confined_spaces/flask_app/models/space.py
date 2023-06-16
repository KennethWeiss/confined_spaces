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
    def delete_space(cls, id):
        data = {'id':id}
        query = """
                DELETE FROM confined_spaces WHERE id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_space(cls, id):
        data = {'id':id}
        query = "SELECT * from confined_spaces WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_spaces(cls):
        query = "SELECT * from confined_spaces;"
        results = connectToMySQL(cls.db).query_db(query)
        spaces = []
        for space in results:
            spaces.append(cls(space))
        return spaces

    @classmethod
    def get_users_spaces(cls, data):
        query = """
                SELECT confined_spaces.id, confined_spaces.name, confined_spaces.created_at, confined_spaces.updated_at FROM confined_spaces.confined_spaces
                JOIN confined_spaces.users_has_confined_spaces
                ON confined_spaces.confined_spaces.id = users_has_confined_spaces.confined_space_id
                JOIN users
                ON users_has_confined_spaces.user_id = users.id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
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
    
    @classmethod
    def edit_space(cls, data):
        query = """
                UPDATE confined_spaces
                SET name = (%(name)s)
                WHERE id = (%(id)s);
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def delete_space(cls, data):
        query = """
                DELETE FROM users_has_confined_spaces 
                WHERE confined_space_id=%(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        query = """
                DELETE FROM confined_spaces
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def delete_space_from_user(cls, data):
        query = """
                    DELETE FROM confined_spaces.users_has_confined_spaces 
                    WHERE user_id=%(id)s and confined_space_id=%(space_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def add_hazard_to_space(cls, data):
        query = """

                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def add_space_to_user(cls, data):
        query = """
                INSERT INTO users_has_confined_spaces
                (confined_space_id, user_id)
                VALUES (%(space_id)s, %(user_id)s)
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