import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')  # For stopword removal
text = "Hello! How are you doing today? I'm doing GREAT!!!"

# Step 1: Lowercase
text_lower = text.lower()
print("After lowercase:", text_lower)
# Output: "hello! how are you doing today? i'm doing great!!!"
import string

# Step 2: Remove punctuation
# string.punctuation contains !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
text_no_punct = text_lower.translate(str.maketrans('', '', string.punctuation))
print("After removing punctuation:", text_no_punct)
# Output: "hello how are you doing today im doing great"

from nltk.tokenize import word_tokenize

# Step 3: Tokenization
tokens = word_tokenize(text_no_punct)
print("After tokenization:", tokens)
# Output: ['hello', 'how', 'are', 'you', 'doing', 'today', 'im', 'doing', 'great']

from nltk.corpus import stopwords

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
print("Example stopwords:", list(stop_words)[:10])
# Shows: ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]

filtered_tokens = [word for word in tokens if word not in stop_words]
print("After stopword removal:", filtered_tokens)
# Output: ['hello', 'today', 'great']