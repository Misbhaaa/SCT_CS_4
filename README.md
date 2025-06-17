# SCT_CS_Task4: Basic Python Keylogger

🔐 This project is Task 4 of the SkillCraft Cyber Security Internship.  
It demonstrates a basic keylogger built using Python that captures and stores keystrokes in a log file.

---

## 🛠️ Features

- Logs **all keyboard input**
- Stops automatically when **Ctrl key** is pressed (left or right)
- Saves keystrokes to a `.txt` file with a timestamped filename
- Built using the `pynput` library

---

## 📦 Requirements

- Python 3.x
- `pynput` library  
  Install it using:

  ```bash
  pip install pynput
## 🚀 How to Run
Clone or download the repo.

Open the terminal and run:
python keylogger.py
A message will appear:

  Keylogger started. Press Ctrl (Left or Right) to stop.

Open Notepad or any other text field and type.

Press Left or Right Ctrl key to stop the keylogger.

A file named like keylog_2025-06-17_18-30-55.txt will be created in the same folder, containing the logged keystrokes.
