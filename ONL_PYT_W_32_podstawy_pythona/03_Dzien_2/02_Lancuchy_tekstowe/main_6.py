#!/usr/bin/python3

def message(actor):
    if 'role' not in actor or 'name' not in actor or 'movie' not in actor:
        return None

    return f"In movie {actor['movie']}, name is {actor['name']} a role {actor['role']}."


input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))

input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
