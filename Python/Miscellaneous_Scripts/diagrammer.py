import spacy


# Use SpaCy to classify every word in the text
# sentence = "After the picnic, the dog ran home at night."
sentence = "I gave my friend a present after school."
sentence = "That hairy kid definitely is stupid."
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
possible_object_dep_ = ["dobj", "acomp"]
for token in doc:
    match token.dep_:
        case "dobj":
            object_of_sentence = " | " + token.text
        case "acomp":
            object_of_sentence = " \\ " + token.text

subj_desc = [token.text for token in doc if token.head.text == subject]

# TODO: Translate the classified and parsed text into a diagram
first_line = f"{subject} | {verb}"
if object_of_sentence != "":
    first_line += object_of_sentence

# Diagram all words describing the subject
descriptors = []
for i in range(len(max(subj_desc, key=len))):
    descriptors.append(" " * i)

    for entry in subj_desc:
        try:
            descriptors.append(f"\\{entry[i]}")
        except IndexError:
            descriptors.append("  ")

        descriptors.append(" ")

    descriptors.append("\n")

# TODO: The program currently creates the multiline diagram of noun descriptors and then tries to add the verb descriptors onto that. Need to do both at the same time.

# Diagram all words describing the verb
verb_desc = [
    token.text for token in doc if token.head.text == verb and token.dep_ == "advmod"
]

# Get the index of where the verb starts in the diagram
verb_start_index = first_line.index(verb[0])
num_align_spaces = 0
candidate = ""
while candidate != "\n":
    for i in descriptors:
        candidate = i
        num_align_spaces += len(i)

for i in descriptors:
    if i == "\n":
        descriptors.remove(i)

for i in range(len(max(verb_desc, key=len))):
    if verb_start_index > num_align_spaces:
        descriptors.append(" " * (verb_start_index - num_align_spaces))

    for entry in verb_desc:
        try:
            descriptors.append(f"\\{entry[i]}")
        except IndexError:
            descriptors.append("  ")

        descriptors.append(" ")

    descriptors.append("\n")

baseline = []
for char in first_line:
    if char == "|" or char == "\\":
        baseline.append("+")
    else:
        baseline.append("-")

print(first_line)
print("".join(baseline))
print("".join(descriptors))
