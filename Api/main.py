from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from database import database
from models import Pokemon, User


import secrets

# Set app
app = Flask(__name__)
CORS(app)
api = Api(app)

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_app(app)

class PokemonApi(Resource):
    def post(self):
        raw = request.get_json()
        print("Incoming JSON:", raw)

        if raw is None:
            return {"error": "No JSON received"}, 400

        try:
            pokemon = Pokemon(
                name=raw.get("Name"),
                level=raw.get("Level"),
                gender=raw.get("Gender"),
                age=raw.get("Age"),
                nature=raw.get("Nature"),
                ability=raw.get("Ability"),

                baseHealth=raw.get("BaseHealth"),
                will=raw.get("Will"),
                logic=raw.get("Logic"),
                instinct=raw.get("Instinct"),
                primal=raw.get("Primal"),

                heldItem=raw.get("HeldItem"),
                garment1=raw.get("Garment1"),
                garment2=raw.get("Garment2"),
                garment3=raw.get("Garment3"),
                Status=raw.get("Status"),

                primaryType=raw.get("PrimaryType"),
                secondaryType=raw.get("SecondaryType"),

                strength=raw.get("Strength"),
                strengthPotential=raw.get("StrengthPotential"),

                dexterity=raw.get("Dexterity"),
                dexterityPotential=raw.get("DexterityPotential"),

                vitality=raw.get("Vitality"),
                vitalityPotential=raw.get("VitalityPotential"),

                special=raw.get("Special"),
                specialPotential=raw.get("SpecialPotential"),

                insight=raw.get("Insight"),
                insightPotential=raw.get("InsightPotential"),

                fight=raw.get("Fight"),
                survival=raw.get("Survival"),
                contest=raw.get("Contest"),
                brawl=raw.get("Brawl"),
                channel=raw.get("Channel"),
                clash=raw.get("Clash"),
                evasion=raw.get("Evasion"),
                alert=raw.get("Alert"),
                athletic=raw.get("Athletic"),
                natureStat=raw.get("NatureStat"),
                stealth=raw.get("Stealth"),
                allure=raw.get("Allure"),
                etiquette=raw.get("Etiquette"),
                intimidate=raw.get("Intimidate"),
                perform=raw.get("Perform"),
                experiencePoints=raw.get("ExperiencePoints"),
                isNpc=raw.get("IsNpc"),
                Guid=raw.get("Guid")
            )

            database.session.add(pokemon)
            database.session.commit()

        except Exception as e:
            print("DB ERROR:", e)
            database.session.rollback()
            return {"error": str(e)}, 500

        return {"message": "Created", "id": pokemon.id}, 201


class Register(Resource):
    def get(self):
        return render_template_string(register_template)

    def post(self):
        data = request.form if request.form else request.json

        username: str = data.get("username")
        password: str = data.get("password")

        if not username or not password:
            return {"message": "Username & password required"}, 400

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 409

        # Generate a cryptographically secure random salt
        salt: str = secrets.token_hex(32)  # 64 chars

        # Hash salt + password
        hashed: str = generate_password_hash(salt + password)

        newUser: User= User(
            username=username,
            password=hashed,
            passwordSalt=salt
        )

        database.session.add(newUser)
        database.session.commit()

        return {"message": "User registered successfully"}, 201

class Login(Resource):
    def get(self):
        return render_template_string(login_template)

    def post(self):
        data = request.form if request.form else request.json

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if not user:
            return {"message": "Invalid username or password"}, 401

        # Recreate salted hash input
        salted_input = user.passwordSalt + password

        if not check_password_hash(user.password, salted_input):
            return {"message": "Invalid username or password"}, 401

        return {"message": f"Welcome, {username}!"}, 200

class PullCharacterData(Resource):
    def get(self, guid):
        character = Pokemon.query.filter_by(Guid=guid).first_or_404()
        return jsonify({"data": character.toDict()})

api.add_resource(PullCharacterData, "/PullCharacterData/<string:guid>")
api.add_resource(PokemonApi, '/data')
api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    app.run("0.0.0.0", 9000, debug=True)
1