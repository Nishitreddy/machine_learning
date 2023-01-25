# Question 6.
sentence = "I am a teacher and I love to inspire and teach people"
# Split the sentence into words
words = sentence.split()

# Use set to get the unique words
unique_words = set(words)

# Find the length of the set to get the number of unique words
uniqueWords = len(unique_words)

# Print the results
print("Sentence:", sentence)
print("Number of unique words:", uniqueWords)

#Explanation:
#In the given sentence, we must first use split() to determine the number of distinct words, 
#and then len() to determine the length of distinct words.