import requests
import json

HOSTNAME = "localhost"
PORT = 4567
HOST = f"http://{HOSTNAME}:{PORT}"

JSON = "application/json"
GET_HEADERS = {"Accept": JSON}
POST_HEADERS = {"Content-type": JSON, "Accept": JSON}
IMAGE = "does_not_exist.png"
TOKEN = "jwt token verfication not implemented"

INDENT = 4

# HTTP requests

def get_request(uri, params=None):
    if params is None:
        params = dict()
    url = f"{HOST}{uri}"
    print("#### Performing GET request ####")
    print(f"URL: {url}")
    print(f"Params: {json.dumps(params, indent=INDENT)}")
    response = requests.get(url, headers=GET_HEADERS, params=params)
    print_response(response)

def post_json_request(uri, json_payload):
    url = f"{HOST}{uri}"
    print("#### Performing POST request ####")
    print(f"URL: {url}")
    print(f"JSON payload: {json.dumps(json_payload, indent=INDENT)}")
    response = requests.post(url, headers=POST_HEADERS, json=json_payload)
    print_response(response)

def print_response(response):
    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {json.dumps(response.json(), indent=INDENT)}")
    print()

# Use cases

def create_tag(tag_name):
    uri = "/create/tag"
    json_payload = {
        "name": tag_name
    }
    post_json_request(uri, json_payload)

def create_ingredient(name, units, image_uri=IMAGE):
    uri = "/create/ingredient"
    json_payload = {
        "name": name,
        "units": units,
        "imageUri": image_uri
    }
    post_json_request(uri, json_payload)

def create_user(username, email_address):
    uri = "/create/user"
    json_payload = {
        "username": username,
        "emailAddress": email_address
    }
    post_json_request(uri, json_payload)

def create_recipe(recipe_details):
    uri = "/create/recipe"
    json_payload = {
        "encryptedJwtToken": TOKEN,
        "recipe": recipe_details
    }
    post_json_request(uri, json_payload)

def get_entity(entity, name):
    get_request(f"/{entity}/{name}")

def get_tag(name):
    get_entity("tags", name)

def get_ingredient(name):
    get_entity("ingredients", name)

def get_user(username):
    get_entity("users", username)

def get_recipe(unique_name):
    get_entity("recipes", unique_name)

def search(entity, search_terms):
    get_request(f"/search/{entity}", {"terms": "+".join(search_terms)})

def search_for_tags(search_terms):
    search("tags", search_terms)

def search_for_ingredients(search_terms):
    search("ingredients", search_terms)

def search_for_users(search_terms):
    search("users", search_terms)

def search_for_recipes(search_terms):
    search("recipes", search_terms)

def bookmark_recipe(username, recipe_unique_name):
    uri = "/bookmark/recipe"
    json_payload = {
        "username": username,
        "recipe": recipe_unique_name,
        "encryptedJwtToken": TOKEN
    }
    post_json_request(uri, json_payload)

def add_ingredients_to_shopping_list(username, ingredients):
    uri = "/shopping-list/add-ingredients"
    json_payload = {
        "username": username,
        "encryptedJwtToken": TOKEN,
        "ingredients": ingredients
    }
    post_json_request(uri, json_payload)

def add_recipe_to_shopping_list(username, recipe_unique_name):
    uri = "/shopping-list/add-recipe-ingredients"
    json_payload = {
        "username": username,
        "encryptedJwtToken": TOKEN,
        "recipe": recipe_unique_name,
        "addOnlyMissingIngredients": False
    }
    post_json_request(uri, json_payload)

# Demo

def main():
    get_tag("breakfast")
    create_tag("breakfast")
    create_tag("one ingredient")

    create_ingredient("egg", "unit")
    create_ingredient("cheddar cheese", "cup")

    create_user("jane_doe", "JaneDoe1219411712718@hotmail.com")
    create_user("john_dough", "JohnDoughThough1284158917581@aol.com")

    egg_omelette = {
        "name": "egg_omelette",
        "presentationName": "Simple Egg Omelette",
        "authorUsername": "jane_doe",
        "prepTime": 4,
        "cookTime": 4,
        "imageUri": IMAGE,
        "numServings": 1,
        "avgRating": 4.5,
        "numRatings": 20,
        "directions": [
            "Crack eggs into bowl",
            "Beat eggs",
            "Start stove with temperature on medium",
            "..."
        ],
        "tags": [
            "breakfast",
            "one ingredient",
        ],
        "requiredIngredients": {
            "egg": 2,
        }
    }
    cheese_omelette = {
        "name": "cheese_omelette",
        "presentationName": "Tasty Cheese Omelette",
        "authorUsername": "john_dough",
        "prepTime": 5,
        "cookTime": 5,
        "imageUri": IMAGE,
        "numServings": 1,
        "avgRating": 4.6,
        "numRatings": 21,
        "directions": [
            "Crack eggs into bowl",
            "...",
            "Add cheese",
            "..."
        ],
        "tags": [
            "breakfast",
        ],
        "requiredIngredients": {
            "egg": 2,
            "cheddar cheese": 0.75,
        }
    }

    create_recipe(egg_omelette)
    create_recipe(cheese_omelette)

    get_tag("breakfast")
    get_ingredient("egg")
    get_user("jane_doe")
    get_recipe("cheese_omelette")

    search_for_tags(["one"])
    search_for_ingredients(["cheese"])
    search_for_recipes(["tasty"])
    search_for_recipes(["omelette"])
    search_for_recipes(["nothing"])

    bookmark_recipe("john_dough", "egg_omelette")
    add_ingredients_to_shopping_list("john_dough", {"egg": 3})
    add_recipe_to_shopping_list("jane_doe", "cheese_omelette")
    
    get_user("john_dough")
    get_user("jane_doe")

if __name__ == "__main__":
    main()
