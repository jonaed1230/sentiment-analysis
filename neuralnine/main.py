from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')
choice = input("Do you want to enter a URL or a text? (URL/text): ")
if choice.lower() == "url":
    url = input("Enter the URL: ")
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.summary
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print("Your result for this article is: " + str(sentiment))
elif choice.lower() == "text":
    text = input("Enter the text: ")
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print("Your result for this text is: " + str(sentiment))
else:
    print("Invalid choice!")