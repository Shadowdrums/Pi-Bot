import json
import os
from textblob import TextBlob  # for sentiment analysis

LEARNING_FILE = "pi_learnings.json"

_cache = None  # In-memory cache of the learnings

def load_learnings():
    global _cache
    if _cache is None:
        if os.path.exists(LEARNING_FILE):
            with open(LEARNING_FILE, 'r') as f:
                content = f.read()
                if content:
                    _cache = json.loads(content)
                    return _cache
        _cache = {}
    return _cache

def save_learnings(learnings):
    global _cache
    with open(LEARNING_FILE, 'w') as f:
        json.dump(learnings, f)
    _cache = learnings

def add_response(keyword, response):
    learnings = load_learnings()
    learnings[keyword.lower()] = response
    save_learnings(learnings)

def remove_response(keyword):
    learnings = load_learnings()
    if keyword.lower() in learnings:
        del learnings[keyword.lower()]
        save_learnings(learnings)

def update_response(keyword, new_response):
    learnings = load_learnings()
    learnings[keyword.lower()] = new_response
    save_learnings(learnings)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def analyze_context(text):
    text = text.lower()
    # Greetings
    if any(greeting in text for greeting in ["hi", "hello", "hey"]):
        return "greeting"
    # Farewells
    if any(bye in text for bye in ["bye", "goodbye", "see you", "later"]):
        return "farewell"
    # Weather queries
    if any(weather in text for weather in ["weather", "temperature", "forecast", "raining", "sunny"]):
        return "weather"
    # News queries
    if any(news in text for news in ["news", "headline", "current event", "update"]):
        return "news"
    # Queries about bot's functionality or purpose
    if any(query in text for query in ["what can you do", "your function", "help", "abilities"]):
        return "bot_function"
    # Tech or troubleshooting related
    if any(tech in text for tech in ["error", "problem", "issue", "help", "troubleshoot"]):
        return "tech_support"
    # Personal questions to bot
    if any(personal in text for personal in ["who are you", "what are you", "your name"]):
        return "bot_identity"
    # Gratitude expressions
    if any(thank in text for thank in ["thanks", "thank you", "appreciate"]):
        return "gratitude"
    # ... more contexts can be added as needed

    else:
        return "unknown"

def get_response(query):
    """Return a response based on a known set of responses or generate one."""
    learnings = load_learnings()
    sentiment = analyze_sentiment(query)
    context = analyze_context(query)
    
    if query in learnings:
        return learnings[query]

    for key, response in learnings.items():
        if key in query:
            return response

    # For this example, if the bot doesn't have a set response, it replies based on sentiment.
    if sentiment == "positive":
        return "Thank you for the kind words!"
    elif sentiment == "negative":
        return "I apologize for any inconvenience. Please let me know how I can assist further."
    else:
        return "Can you please elaborate?"

def user_correction(query, correction):
    add_response(query, correction)
