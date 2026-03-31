import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Input text
text = "Hello! This is a sample sentence, showing off the stopwords filtration."

# Step 1: Convert to lowercase
text_lower = text.lower()

# Step 2: Remove punctuation
text_no_punct = text_lower.translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenization
tokens = word_tokenize(text_no_punct)

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Outputs
cleaned_text = " ".join(filtered_tokens)

print("Cleaned Text:", cleaned_text)
print("Tokens:", filtered_tokens)