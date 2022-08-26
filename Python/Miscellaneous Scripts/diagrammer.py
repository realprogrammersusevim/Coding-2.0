import spacy


# Use SpaCy to classify every word in the text
# sentence = "After the picnic, the dog ran home at night."
# sentence = "I gave my friend a present after school."
sentence = "He is stupid."
# sentence = "Go away."
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
for token in doc:
    if token.dep_ == "nsubj":
        subject = token.text
        break

    # If the sentence is imperative and no subject is found than the subject is an implicit (you)
    subject = "(you)"

for token in doc:
    if token.head == token:
        verb = token.text

object_of_sentence = ""
for token in doc:
    if token.dep_ == "dobj" or token.dep_ == "acomp":
        object_of_sentence = token.text
        break

# TODO: Translate the classified and parsed text into a diagram
first_line = f"{subject} | {verb}"
if object_of_sentence != "":
    first_line += f" | {object_of_sentence}"

underline = []
for char in first_line:
    if char == "|":
        underline.append("+")
    else:
        underline.append("-")

print(first_line)
print("".join(underline))
