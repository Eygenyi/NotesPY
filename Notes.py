
import json
from datetime import datetime

class Note:
    def __init__(self, id, title, body, creation_date, last_modified_date):
        self.id = id
        self.title = title
        self.body = body
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date

class NoteManager:
    def __init__(self):
        try:
            with open('notes.json', 'r') as file:
                self.notes = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.notes = []

    def add_note(self, title, body):
        creation_date = datetime.now().isoformat()
        note = Note(len(self.notes) + 1, title, body, creation_date, creation_date)
        self.notes.append(note.__dict__)
        self.save_notes()

    def edit_note(self, id, title, body):
        for note in self.notes:
            if note['id'] == id:
                note['title'] = title
                note['body'] = body
                note['last_modified_date'] = datetime.now().isoformat()
        self.save_notes()

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note['id'] != id]
        self.save_notes()

    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file, indent=4)

    def print_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['body']}, Created: {note['creation_date']}, Last Modified: {note['last_modified_date']}")


note_manager = NoteManager()

while True:
    print("1. Add a note")
    print("2. Edit a note")
    print("3. Delete a note")
    print("4. Print notes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        note_manager.add_note(title, body)
    elif choice == "2":
        id = int(input("Enter note id to edit: "))
        title = input("Enter new title: ")
        body = input("Enter new body: ")
        note_manager.edit_note(id, title, body)
    elif choice == "3":
        id = int(input("Enter note id to delete: "))
        note_manager.delete_note(id)
    elif choice == "4":
        note_manager.print_notes()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")