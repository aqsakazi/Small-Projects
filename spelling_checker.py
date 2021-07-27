from textblob import TextBlob

original_text = str(input("Enter some text: "))
correct_text = TextBlob(original_text)

print("Corrected text is: "+ str(correct_text.correct()))
