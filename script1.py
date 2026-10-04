import os
from transformers import pipeline

# loading the pipline
sentiment_classifier = pipeline("sentiment-analysis")

# statment list
sentences = [
    "The new update finally fixed the issue",
    "The new update completely broke my  feature",
    "The new update was released on Tuesday "
]

print("--Sentiment Analysis Results ----")
for text in sentences:
    result = sentiment_classifier(text)[0]  # [0] එක මෙතනට දැම්මා
    print(f"\nText: \"{text}\"")
    print(f"Label: {result['label']} (Confidence: {result['score']:.2%})")
print("--------------------------------------------------")
print("\n------Test with your thought---")

while True:
    user_text =input("Enter Your text or type 'exit' to quit: ").strip()
    if user_text.lower() == "exit":
        print("Thank You , Good Bye")
        break

    if user_text:
        Type_result = sentiment_classifier(user_text)[0]
        print(f"Result : label {Type_result['label']} | Confidence:{Type_result['score']:.2%}\n")
    else:
        print("pLese enter some text")