import spacy


# Use SpaCy to classify every word in the text
sentence = "After the picnic, the dog ran home at night."
nlp = spacy.load("en_core_web_sm")
doc = nlp(sentence)

# Print each token and some of its attributes
print(sentence)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

# Create a list of prepostions
prepostions = [token for token in doc if token.dep_ == "prep"]

# Find each prepositional phrase by searching for the words whose head is the preposition
all_prep_phrases_dict = {}
all_prep_phrase_tokens = []
num_phrases = 0
prep_phrase = []
for prepostion in prepostions:
    num_phrases += 1
    for token in doc:
        if token.head == prepostion:
            prep_phrase.append(prepostion.text)
            all_prep_phrase_tokens.append(prepostion)
            obj_of_prep = token
            all_prep_phrase_tokens.append(obj_of_prep)

            # Find all words in the prepositional phrase
            for token in doc:
                if token.head == obj_of_prep:
                    prep_phrase.append(token.text)
                    all_prep_phrase_tokens.append(token)

            prep_phrase.append(obj_of_prep.text)
            all_prep_phrases_dict[num_phrases] = prep_phrase
            prep_phrase = []
            break

print(all_prep_phrases_dict)
print(all_prep_phrase_tokens)

# TODO: Read the flow chart in the Analytical Grammar book and implement the conditional tree

# TODO: Translate the classified and parsed text into a diagram
