from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I feel depressed about my rejection in Presidio final round.")

print("Answer: ", result)