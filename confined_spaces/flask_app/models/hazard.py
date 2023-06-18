from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Hazard:
    db = "confined_spaces"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_hazards(cls):
        query = "SELECT * from hazards;"
        results = connectToMySQL(cls.db).query_db(query)
        hazards = []
        for hazard in results:
            hazards.append(cls(hazard))
        return hazards
    
    @classmethod
    def create_hazard(cls, data):
        query = "INSERT INTO hazards (name, description) VALUE (%(name)s, %(description)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def add_hazard_to_space(cls, data):
        query = "INSERT INTO hazards_has_confined_spaces (hazard_id, confined_space_id) VALUE (%(hazard_id)s, %(confined_space_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def space_hazards(cls, id):
        data = {'id':id}
        query = """
                SELECT * from hazards
                JOIN hazards_has_confined_spaces ON id = hazard_id
                WHERE confined_space_id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def delete_hazard(cls, data):
        query = "DELETE FROM hazards WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results