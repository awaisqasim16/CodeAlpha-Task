import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firebase()

def fetch_all_entries():
    docs = db.collection('entries').stream()
    return [doc.to_dict() for doc in docs]

def insert_entry(entry):
    db.collection('entries').add(entry)
