from data_handler import process_entry

def main():
    print("📌 Data Redundancy Removal System")
    
    while True:
        content = input("Enter content: ")
        email = input("Enter email: ")

        entry = {
            "content": content,
            "email": email,
            "timestamp": firestore.SERVER_TIMESTAMP
        }

        result = process_entry(entry)
        print("⚙️ Result:", result)

if __name__ == "__main__":
    from firebase_admin import firestore
    main()
