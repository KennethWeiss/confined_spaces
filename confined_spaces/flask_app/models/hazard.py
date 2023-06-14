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