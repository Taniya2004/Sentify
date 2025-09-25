# 🎭 Sentify – Real-Time Chat with Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TextBlob-ff69b4?style=for-the-badge)

---

## 📌 Project Overview
**Sentify** is a **real-time chat application** integrated with a **sentiment analysis model**.  
It analyzes user messages during conversations and detects emotions like **positive, negative, or neutral**.  

This helps users understand the overall mood of the chat while providing a smooth chatting experience.

---

## 🚀 Features
- 💬 Real-time chatting
- 🎭 Sentiment analysis on messages
- 🔒 User authentication
- 🗄️ Database integration with MySQL
- 🛠️ Built with Django (Python)
- 📊 Clear and user-friendly interface

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, (Add React if you plan to use)  
- **Backend:** Django (Python)  
- **Database:** MySQL  
- **ML/NLP:** TextBlob / Scikit-learn  

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Taniya2004/Sentify.git
   cd Sentify
   ```

2. **Create virtual environment & activate**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database (MySQL)**
   - Update `settings.py` with your MySQL username & password.
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. Open in browser → `http://127.0.0.1:8000/`

---

## 📊 Screenshots / Demo

| Chat Screen | Sentiment Detection |
|-------------|---------------------|
| ![Chat Screenshot](assets/chat.png) | ![Sentiment Screenshot](assets/sentiment.png) |

*(Add your own screenshots in an `assets/` folder and update links here)*

---

## 🤝 Contributing
Contributions are welcome!  
- Fork the repo  
- Create a feature branch  
- Submit a Pull Request  

---

## 📜 License
This project is licensed under the **MIT License**.  

---

## 👩 Author
**Taniya Kanojiya**  
[GitHub Profile](https://github.com/Taniya2004) | [LinkedIn](#)
