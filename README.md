# Sentify - Real-Time Chat with Sentiment Analysis

📌 Sentify is a real-time chat application built using Django and MySQL.  
It integrates a sentiment analysis model to detect emotions (positive, negative, neutral) in conversations.  
The app features user authentication, responsive UI, and real-time feedback to enhance chat experience.  

## Features

- User authentication (login and logout)
- View list of conversations
- Real-time chat rooms for conversations between users
- Sentiment analysis on messages (Positive, Negative, Neutral)
- Create new conversations with other registered users

## Usage

- Register or login with your user credentials.
- View your existing conversations or start a new conversation with another user.
- Send messages in chat rooms; each message will be analyzed for sentiment.
- Logout when finished.

## Project Structure

- `sentify/` - Django project configuration files
- `chat/` - Main chat application with models, views, templates, and static files
- `MySQL` - MySQL database file
- `manage.py` - Django management script

## Dependencies

- Django
- TextBlob (for sentiment analysis)
