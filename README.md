# 📬 MailMerge

A beginner-friendly **Python automation project** that generates personalized letters using a name list and a letter template. This project demonstrates how to read and write files, replace placeholders, and generate output dynamically — all great foundational skills for working with file I/O and string manipulation.

---

## 📌 Project Objective

🔧 Automatically generate letters for each name listed in a file by:

1. Reading a starting letter from a template.
2. Replacing `[name]` in the template with the actual recipient's name.
3. Writing a personalized letter to the `ReadyToSend` output folder.

---

## 🗂️ Folder Structure
    Beginner-MailMerge/
    │
    ├── Input/
    │ ├── Names/
    │ │ └── invited_names.txt # Contains names (one per line)
    │ └── Letters/
    │ └── starting_letter.txt # Template letter with [name] placeholder
    │
    ├── Output/
    │ └── ReadyToSend/ # Final letters will be stored here
    │
    └── main.py # Main Python script

---

## 🧠 How It Works

- `PLACEHOLDER = '[name]'`: This string is used to identify where to insert the recipient’s name.
- Reads all names from `invited_names.txt`.
- For each name:
  - Loads the letter template.
  - Replaces the placeholder with the actual name.
  - Writes the custom letter to a new file in `Output/ReadyToSend/`.

---

## 📝 Example

**Template (starting_letter.txt):**

    Dear [name],
    
    You are invited to my birthday this Saturday.
    
    Hope you can make it!
    
    Bhagirath

---

## 🚀 Features

- Uses built-in Python file handling.

- Simple placeholder replacement.

- Great for beginners learning automation and file processing.

---





