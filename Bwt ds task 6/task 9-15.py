from collections import defaultdict

# Create a defaultdict with a default value of 0 for any new key
word_count = defaultdict(int)

sentence = "the quick brown fox jumps over the lazy dog"
for word in sentence.split():
    word_count[word] += 1

print(word_count)
