import random
from tokenize import NEWLINE

WORDS = [
    "place",
    "leave",
    "stop",
    "around",
    "mile",
    "very",
    "very",
    "its",
    "found",
    "men",
    "took",
    "number",
    "about",
    "earth",
    "the",
    "with",
    "does",
    "earth",
    "large",
    "for",
    "try",
    "now",
    "if",
    "paper",
    "must",
    "as",
    "may",
    "seem",
    "idea",
    "never",
    "high",
    "so",
    "be",
    "little",
    "fire",
    "what",
    "another",
    "many",
    "year",
    "both",
    "try",
    "must",
    "long",
    "own",
    "his",
    "but",
    "oil",
    "soon",
    "you",
    "know",
    "would",
    "got",
    "which",
    "began",
    "book",
    "near",
    "those",
    "will",
    "life",
    "watch",
    "idea",
    "try",
    "was",
    "ask",
    "in",
    "know",
    "began",
    "later",
    "get",
    "is",
    "follow",
    "out",
    "there",
    "feet",
    "river",
    "walk",
    "enough",
    "different",
    "come",
    "such",
    "every",
    "you",
    "with",
    "study",
    "these",
    "any",
    "way",
    "point",
    "show",
    "has",
]

HIGH_FREQUENCY = [
    "The quick brown fox jumps over the lazy dog",
    "She said that it was time to go home now",
    "They went to the park to play with a ball",
    "You should try to eat some good food today",
]
HOME_ROW_BASIC_FINGER_MOVEMENT = [
    "Ask the lad to add a sash to the dress",
    "All fall as the tall glass falls to the floor",
    "Dad said to add salt to the fat fish",
    "She sells shells by the side of the sea",
]
RHYTHMIC_SENTENCES = [
    "Work hard and play soft for a long life",
    "Keep your eyes on the road and your hands on the wheel",
    "Every small step leads to a very large leap",
    "Light the fire and stay warm in the cold night",
]

# for i in WORDS:
#  print(i)


scores = 0
target = int(input("Repetition: "))

chosen_sentence = int(
    input("1.HIGH_FREQUENCY 2.HOME_ROW_BASIC_FINGER_MOVEMENT 3.RHYTHMIC_SENTENCES:   ")
)


while scores <= target:
    if chosen_sentence == 1:
        z = random.choice(HIGH_FREQUENCY)
    elif chosen_sentence == 2:
        z = random.choice(HOME_ROW_BASIC_FINGER_MOVEMENT)
    elif chosen_sentence == 3:
        z = random.choice(RHYTHMIC_SENTENCES)
    else:
        z = "Invalid choice!"
    # z = random.choice(z)
    print(z)
    y = input("Touch Type: ")

    if y in z:
        print("correct")
        scores += 1
    else:
        print("incorrect")
