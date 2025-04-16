# 🐍 Python Chat App

A simple desktop chat interface built with **Tkinter** and **MongoDB**. This app lets you send and view messages in real-time (with a 2-second refresh loop).

## 🛠 Features

- Send messages via a simple GUI
- Stores messages in a MongoDB database
- Automatically fetches and displays new messages every 2 seconds

## 💡 Requirements

- Python 3.x
- [MongoDB](https://www.mongodb.com/try/download/community)
- Python packages:
  - `tkinter` (usually included with Python)
  - `pymongo`

## 📦 Installation

1. **Clone the repo**:
   ```
   git clone https://github.com/your-username/python-chat-app.git
   ```

2. **Install dependencies**:
   ```
   pip install pymongo
   ```

3. **Make sure MongoDB is running locally**:
   - Default URI is `mongodb://localhost:27017/`

4. **Run the app**:
   ```
   python chat_app.py
   ```

## 🧠 How It Works

- Connects to a local MongoDB database named `PythonChat` and collection `messages`.
- When you type a message and click "Send", it gets saved to the DB.
- Every 2 seconds, it fetches all messages and updates the display.

## 📁 Folder Structure

```
python-chat-app/
│
├── chat_app.py       # Main app script
└── README.md         # Project documentation
```

## 🚀 Future Improvements

- Add usernames or timestamps
- Enable multi-user chat in a local network
- Add scrollable message view

## 📝 License

MIT License. Feel free to use, modify, and share!
