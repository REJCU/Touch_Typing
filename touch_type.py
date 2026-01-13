import datetime
import random
import time
import json
from decimal import Rounded
from tokenize import NEWLINE


sentence_categories = {
    "HIGH_FREQUENCY": [
        "The quick brown fox jumps over the lazy dog",
        "She said that it was time to go home now",
        "They went to the park to play with a ball",
        "You should try to eat some good food today",
    ],
    "HOME_ROW_BASIC_FINGER_MOVEMENT": [
        "Ask the lad to add a sash to the dress",
        "All fall as the tall glass falls to the floor",
        "Dad said to add salt to the fat fish",
        "She sells shells by the side of the sea",
    ],
    "RHYTHMIC_SENTENCES": [
        "Work hard and play soft for a long life",
        "Keep your eyes on the road and your hands on the wheel",
        "Every small step leads to a very large leap",
        "Light the fire and stay warm in the cold night",
    ],
}



scores = 0
target = int(input("Repetition: "))
attempt_date = datetime.datetime.now()
category_names = list(sentence_categories.keys())

for i, name in enumerate(category_names):
    print(f"{i + 1}---{name}")

# Get user's choice
try:
    choice_index = int(input(">>> ")) - 1
    if not 0 <= choice_index < len(category_names):
        print("Invalid choice!")
        exit()
    chosen_category_name = category_names[choice_index]
    sentence_list = sentence_categories[chosen_category_name]
except (ValueError, IndexError):
    print("Invalid input!")
    exit()


start_time = time.time()
while scores < target:
    sentence = random.choice(sentence_list)
    print(sentence)
    answer = input("Touch Type: ")

    if answer == sentence:
        print("correct")
        scores += 1
    else:
        print("incorrect")

end_time = time.time()
total_seconds = end_time - start_time
minutes = int(total_seconds // 60)
seconds = int(total_seconds % 60)
# current average words
total_chars_typed = scores * len(sentence) # This is an approximation
if total_seconds > 0:
    time_in_minutes = total_seconds / 60
    wpm = (total_chars_typed / 5) / time_in_minutes
    rounded_wpm = round(wpm, 2)
else:
    rounded_wpm = "N/A"

print(f"Time: {minutes} Minutes and {seconds} Seconds")
print(f"WPM: {rounded_wpm}")


try:
    with open("typing_scores.json", "r") as f:
        all_scores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    all_scores = []

all_scores.append(
    {
        "chosen_sentence": chosen_category_name,
        "repetition": scores,
        "time_seconds": int(total_seconds),
        "date": f"{attempt_date.day}-{attempt_date.month}-{attempt_date.year}",
        "wpm": rounded_wpm,
    }
)

with open("typing_scores.json", "w") as f:
    json.dump(all_scores, f, indent=4)



"""
Add a time and date to record progress and eventually plot it out.

Make into Classes and eventually a GUI

Accuracy Percentage: Tracking total hits vs. misses.

Live Error Highlighting: Change the text color to red for mistakes and green for correct keys instantly.

Code Mode: Use snippets of Python, C++, or HTML. Coding requires many special characters (;, {, [) that standard typing tests ignore.

Weak Key Focus: Track which keys the user misses most often (e.g., "p" and "q"). Generate custom strings that force the user to practice those specific letters.

RSS or News Feed: Use an API to pull real-time news headlines so the content is always fresh.

"""
