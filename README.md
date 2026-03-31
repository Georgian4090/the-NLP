
# Basic NLP Text Preprocessing Pipeline

## Objective

To understand and implement fundamental text preprocessing techniques used in Natural Language Processing (NLP).

---

##  Tasks Performed

* Convert text to lowercase
* Remove punctuation
* Tokenize text
* Remove stopwords

## Example used

### Input Text

```text id="7y1n8d"
Hello! How are you doing today? I'm doing GREAT!!!
```

---

## Deliverables

###  Cleaned Text

```text id="h7w3kx"
hello doing today im doing great
```

---

### Tokenized Output

```text id="qk9v2p"
['hello', 'doing', 'today', 'im', 'doing', 'great']
```

---

### Explanation of Steps

**1. Lowercasing**
All characters are converted to lowercase to ensure uniformity. This prevents the same word in different cases from being treated as different entities.

**2. Removing Punctuation**
Special characters such as `!`, `?`, and `'` are removed. This helps eliminate noise and ensures words are processed in a clean format.

**3. Tokenization**
The sentence is broken down into individual words. These tokens act as the basic units for further processing in NLP tasks.

**4. Stopword Removal**
Common words like “how”, “are”, and “you” are removed because they do not add significant meaning in most contexts. This step helps focus on more informative words.

---




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
