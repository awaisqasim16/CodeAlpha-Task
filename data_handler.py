import re
from Levenshtein import ratio
from firebase_service import fetch_all_entries, insert_entry

def normalize(text):
    return re.sub(r'\s+', '', text.lower())

def validate(entry):
    if not entry.get("content") or not entry.get("email"):
        return False
    if "@" not in entry["email"]:
        return False
    return True

def is_duplicate(new_entry, threshold=0.9):
    entries = fetch_all_entries()
    new_norm = normalize(new_entry["content"])
    
    for existing in entries:
        existing_norm = normalize(existing["content"])
        if ratio(new_norm, existing_norm) > threshold:
            return True
    return False

def process_entry(entry):
    if not validate(entry):
        log_action("Invalid entry rejected.")
        return "Invalid entry."

    if is_duplicate(entry):
        log_action("Duplicate entry detected and ignored.")
        return "Duplicate found."

    insert_entry(entry)
    log_action("New unique entry inserted.")
    return "Inserted successfully."

def log_action(message):
    with open("logs.txt", "a") as log:
        log.write(f"{message}\n")
