
# Basic NLP Text Preprocessing Pipeline

## Objective

To understand and implement fundamental text preprocessing techniques used in Natural Language Processing (NLP).

---

##  Tasks Performed

* Convert text to lowercase
* Remove punctuation
* Tokenize text
* Remove stopwords

##  Implementation

### Step 1: Lowercasing

Converting all characters to lowercase to ensure uniformity.

```python
text_lower = text.lower()
```

---

### 🔹 Step 2: Remove Punctuation

Eliminate punctuation marks to avoid noise in tokens.

```python
import string
text_no_punct = text_lower.translate(str.maketrans('', '', string.punctuation))
```

---

### 🔹 Step 3: Tokenization

Split the text into individual words (tokens).

```python
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text_no_punct)
```

---

### 🔹 Step 4: Stopword Removal

Remove commonly used words that do not add significant meaning.

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
```

---

## Example Input

```
"Hello! This is a sample sentence, showing off the stopwords filtration."
```

---

##  Output

###  Cleaned Text

```
hello sample sentence showing stopwords filtration
```

###  Tokenized Output

```
['hello', 'sample', 'sentence', 'showing', 'stopwords', 'filtration']
```

## Requirements

Install required libraries:

```bash
pip install nltk
```

Download NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## Pipeline Overview

```
Raw Text
   ↓
Lowercasing
   ↓
Remove Punctuation
   ↓
Tokenization
   ↓
Stopword Removal
   ↓
Cleaned Tokens
```
