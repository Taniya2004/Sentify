# Sentify

Sentify is a Django-based chat application that allows users to authenticate, create conversations, and send messages with built-in sentiment analysis. The sentiment of each message is analyzed using TextBlob and categorized as Positive, Negative, or Neutral.

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
