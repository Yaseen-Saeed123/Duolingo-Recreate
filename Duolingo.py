from time import sleep
def prints(word):
    print(word)
    sleep(2)
    print("-"*30)
# Check if words are structurally correct (Follows basic English constraints)
def correct(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    allowed_consonant_starters = [
        # The S-Clusters
        "sc", "sk", "sl", "sm", "sn", "sp", "st", "sw",
        
        # The Liquid/Glide Followers
        "bl", "cl", "fl", "gl", "pl",
        "br", "cr", "dr", "fr", "gr", "pr", "tr",
        "dw", "gw", "tw",
        
        # The Y-Followers (Phonetic Vowels / Structural Consonants)
        "by", "cy", "dy", "hy", "ly", "my", "py", "sy", "ty",
        
        # The H-Team Digraphs
        "ch", "gh", "ph", "sh", "th", "wh",
        
        # Historical Silents (Allowed in written English)
        "kn", "gn", "pn", "ps", "wr"
    ]
    # Case 0: If there is no word at all
    if len(word) == 0 or (len(word) == 1 and word not in ["i"]):
        return False, "Too small to be a word"
    # Case 1: q followed by u
    if 'q' in word and 'qu' not in word:
        return False, "Q must be followed by U"
    # Case 2: word doesn't end in v
    if word[-1] == 'v':
        return False, "Words can't end in V"
    # Case 3: Vowels exist
    for char in word:
        if char in vowels:
            break
    else:
        return False, "No vowel exists"
    # Case 4: Non-Forbidden starters
    first_two = word[:2]
    if first_two[0] in vowels or first_two[1] in vowels:
        return True
    elif first_two in allowed_consonant_starters:
        return True
    else:
        return False, "There is a Forbidden starter"
# The core of the program
sentence_structures = {
    "S-V": {
        "name": "Subject + Verb",
        "pattern": ["Subject", "Verb"],
        "description": "The absolute baseline; a subject performs an action.",
        "examples": [
            "Dogs bark.",
            "She slept.",
            "The snow fell."
        ]
    },
    "S-V-O": {
        "name": "Subject + Verb + Object",
        "pattern": ["Subject", "Verb", "Object"],
        "description": "The most common pattern; an action transitions to a receiver.",
        "examples": [
            "Cats chase mice.",
            "He bought a car.",
            "Children love games."
        ]
    },
    "S-V-Adj": {
        "name": "Subject + Linking Verb + Adjective",
        "pattern": ["Subject", "Linking Verb", "Adjective"],
        "description": "Describes the state, condition, or quality of the subject.",
        "examples": [
            "The coffee is hot.",
            "She seems tired.",
            "The sky became dark."
        ]
    },
    "S-V-Adv": {
        "name": "Subject + Verb + Adverb",
        "pattern": ["Subject", "Verb", "Adverb"],
        "description": "Explains how, when, or where an action happens.",
        "examples": [
            "Time moves quickly.",
            "He speaks softly.",
            "They arrived early."
        ]
    },
    "S-V-Prep": {
        "name": "Subject + Verb + Prepositional Phrase",
        "pattern": ["Subject", "Verb", "Preposition", "Noun"],
        "description": "Adds physical context like location, direction, or time.",
        "examples": [
            "The book is on the table.",
            "We walked to the park.",
            "Birds fly in the sky."
        ]
    },
    "S-V-IO-DO": {
        "name": "Subject + Verb + Indirect Object + Direct Object",
        "pattern": ["Subject", "Verb", "Object 1 (Receiver)", "Object 2 (Thing)"],
        "description": "Used when an action is done to or for someone.",
        "examples": [
            "My mom gave me a book.",
            "The teacher assigned the class homework.",
            "He bought his sister a gift."
        ]
    },
    "S-V-O-OC": {
        "name": "Subject + Verb + Object + Object Complement",
        "pattern": ["Subject", "Verb", "Object", "Noun/Adjective"],
        "description": "Introduces an object and immediately renames or describes it.",
        "examples": [
            "They elected him president.",
            "The cold weather made the milk sour.",
            "We painted the house white."
        ]
    }
}
sentence_quiz = {
    "S-V": [
        {
            "question": "Which of the following sentences follows the strict Subject + Verb (S-V) pattern without any objects?",
            "choices": [
                "A) The birds flew away.",
                "B) The birds built a nest.",
                "C) The birds are beautiful.",
                "D) The birds love worms."
            ],
            "answer": "A",
            "explanation": "'Flew' is an intransitive verb that does not require a direct object to receive the action."
        },
        {
            "question": "In the sentence 'The alarm rang loudly', what constitutes the core S-V backbone?",
            "choices": [
                "A) alarm (S) + loudly (V)",
                "B) The (S) + alarm (V)",
                "C) alarm (S) + rang (V)",
                "D) rang (S) + loudly (V)"
            ],
            "answer": "C",
            "explanation": "'Alarm' is the noun subject performing the action, and 'rang' is the main verb. 'Loudly' is an adverb modifying the verb."
        }
    ],
    "S-V-O": [
        {
            "question": "Identify the direct object in the S-V-O sentence: 'The chef prepared a delicious meal.'",
            "choices": [
                "A) chef",
                "B) prepared",
                "C) delicious",
                "D) meal"
            ],
            "answer": "D",
            "explanation": "'Meal' is the noun receiving the action of the transitive verb 'prepared'."
        },
        {
            "question": "Which sentence perfectly exhibits the Subject + Verb + Object structure?",
            "choices": [
                "A) She smiled at him.",
                "B) She wrote a letter.",
                "C) She became a writer.",
                "D) She wrote beautifully."
            ],
            "answer": "B",
            "explanation": "'She' is the subject, 'wrote' is the transitive verb, and 'letter' is the direct object."
        }
    ],
    "S-V-Adj": [
        {
            "question": "In the sentence 'The fresh milk turned sour', what grammatical role does 'sour' play?",
            "choices": [
                "A) Direct Object",
                "B) Adverb modifying 'turned'",
                "C) Predicate Adjective describing 'milk'",
                "D) Subject Complement Noun"
            ],
            "answer": "C",
            "explanation": "'Turned' acts as a linking verb here, and 'sour' is an adjective describing the condition of the subject 'milk'."
        },
        {
            "question": "Which of the following contains a linking verb followed by an adjective?",
            "choices": [
                "A) The engine runs smoothly.",
                "B) The soup tastes salty.",
                "C) The cook tasted the soup.",
                "D) The bell rang suddenly."
            ],
            "answer": "B",
            "explanation": "'Tastes' is functioning as a linking verb connecting the subject 'soup' to its descriptive adjective 'salty'."
        }
    ],
    "S-V-Adv": [
        {
            "question": "Which sentence represents an S-V-Adv pattern where the final word answers 'how' the action was done?",
            "choices": [
                "A) The guest arrived late.",
                "B) The plane landed safely.",
                "C) The children played outside.",
                "D) The meeting ended early."
            ],
            "answer": "B",
            "explanation": "'Safely' is an adverb of manner showing *how* the plane landed."
        },
        {
            "question": "What is the grammatical breakdown of the sentence: 'Time passes quickly.'?",
            "choices": [
                "A) Subject + Verb + Object",
                "B) Subject + Linking Verb + Adjective",
                "C) Subject + Verb + Adverb",
                "D) Subject + Verb + Preposition"
            ],
            "answer": "C",
            "explanation": "'Time' is the subject, 'passes' is the action verb, and 'quickly' is an adverb modifying the action."
        }
    ],
    "S-V-Prep": [
        {
            "question": "Identify the prepositional phrase completing the S-V-Prep pattern in: 'The passengers waited at the terminal.'",
            "choices": [
                "A) The passengers",
                "B) waited at",
                "C) at the terminal",
                "D) the terminal"
            ],
            "answer": "C",
            "explanation": "'At the terminal' is a prepositional phrase starting with the preposition 'at' and ending with the noun 'terminal'."
        },
        {
            "question": "Which sentence follows the Subject + Verb + Prepositional Phrase blueprint?",
            "choices": [
                "A) Water flows downhill.",
                "B) The keys fell under the car.",
                "C) The keys open the car.",
                "D) The keys are metallic."
            ],
            "answer": "B",
            "explanation": "'Under the car' is a prepositional phrase showing location, paired with the subject 'keys' and verb 'fell'."
        }
    ],
    "S-V-IO-DO": [
        {
            "question": "In the sentence 'The guide showed the tourists the ancient ruins', which words represent the Indirect Object and Direct Object respectively?",
            "choices": [
                "A) guide / tourists",
                "B) ruins / tourists",
                "C) tourists / ruins",
                "D) showed / ruins"
            ],
            "answer": "C",
            "explanation": "'Tourists' is the indirect object receiving the direct object, which is the actual item being shown ('ruins')."
        },
        {
            "question": "Which sentence contains both an Indirect Object and a Direct Object?",
            "choices": [
                "A) I bought a watch for my father.",
                "B) I bought my father a watch.",
                "C) My father bought a brand new watch.",
                "D) The watch was bought by my father."
            ],
            "answer": "B",
            "explanation": "In option B, 'my father' sits directly between the verb and the direct object ('watch') without requiring a preposition, fulfilling the exact S-V-IO-DO structure."
        }
    ],
    "S-V-O-OC": [
        {
            "question": "In the sentence 'The stress made him sick', what is the grammatical function of the word 'sick'?",
            "choices": [
                "A) Direct Object",
                "B) Indirect Object",
                "C) Object Complement",
                "D) Adverb modifying 'made'"
            ],
            "answer": "C",
            "explanation": "'Sick' is an adjective acting as an object complement because it describes the state resulting *to* the object ('him')."
        },
        {
            "question": "Which sentence demonstrates the Subject + Verb + Object + Object Complement (Noun) structure?",
            "choices": [
                "A) The judge found the man guilty.",
                "B) The committee appointed Sarah chairperson.",
                "C) Sarah painted the old fence white.",
                "D) Sarah likes her new job."
            ],
            "answer": "B",
            "explanation": "'Sarah' is the object, and 'chairperson' is a noun complement that renames and identifies her new status."
        }
    ]
}
types = list(sentence_structures.keys())
sentence = {}
print("-"*30)
print("Welcome to Grammar Exercise")
print("-"*30)
# Choosing Type of sentence
print("Choose a sentence Type from these types to be explained for you:- ")
print("-"*30)
for i, key in enumerate(types, start=1):
    print(f"{i}- {sentence_structures[key]["name"]}")
    print("."*10)
while True:
    try:
        number = int(input("=> ").strip())
        print("-"*30)
        index = number - 1
        if index > len(types) or index < 0:
            print('Number Out Of Range')
            print("-"*30)
        else:
            break
    except ValueError:
            print("-"*30)
            print('Not A Valid Input')
            print("-"*30)
# Explain the type of sentence
struct = types[index]
pattern = sentence_structures[struct]["pattern"]
describe = sentence_structures[struct]["description"]
examples = sentence_structures[struct]["examples"]
prints(f"Pattern: {pattern}")
prints(f"Explanation: {describe}")
prints("Here are some examples")
for i in range(len(examples)):
    prints(f"{i+1}. {examples[i]}")
prints("Ok Let's answer a few questions")
# Exercise: Mode 1
prints("Exercise 1: Make up your own sentence")
for part in pattern:
    while True:
        word = input(f"{part}: ").strip()
        print("-"*30)
        is_correct = correct(word.lower())
        if is_correct == True:
            sentence[part] = word
            break
        else:
            print(is_correct[1])
            print("-"*30)
# Print out the sentence
answer = list(sentence.values())
my_sentence = " ".join(answer).capitalize()
prints(f"Excellent Work 😁 Your sentence is '{my_sentence}.'")
# Exercise: Mode 2
prints("Exercise 2: Answer The following questions")
score = 0
for i in range(2):
    question = sentence_quiz[struct][i]
    prints(f"Q{i+1}: {question['question']}")
    for choice in question['choices']:
        print(choice)
        print("."*10)
    while True:
        response = input("=> ").strip().upper()
        print("-"*30)
        if response not in ["A", "B", "C", "D"]:
            prints("Not a Valid Answer ❌❌")
        else:
            if response == question['answer']:
                score += 1
                prints("Good Job You got the correct answer ✅")
            else:
                prints("Sorry You got the wrong answer ❌")
                prints(f"The correct answer is {question['answer']}")
            prints(f"The score is now {score}/{i+1}")
            prints(f"Explanation: {question['explanation']}")
            break
# Evaluate Score
if score == 0:
    prints("You need to focus on the explanation given above. Then, you may retake the exercises once more")
elif score == 1:
    prints(f"Keep going you are very close to mastering the {struct} sentence")
else:
    prints(f"Excellent work there You've mastered the {struct} sentence")