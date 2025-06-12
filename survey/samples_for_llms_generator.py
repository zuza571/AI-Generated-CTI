import random
import json

samples = []
labels = []
with open('samples_for_survey.jsonl', 'r') as file:
    lines = file.readlines()
    for line in lines:
        sample = json.loads(line)
        label = 'GENERATED' if sample['label'] == 1 else 'REAL'
        samples.append((sample['text'], label))

random.shuffle(samples)

with open('samples_for_llms.txt', 'w') as file:
    for i, sample in enumerate(samples, start=1):
        text, label = sample
        labels.append(label)
        file.write(f"{i}. {text}\n")

with open('samples_for_llms_labels.txt', 'w') as file:
    for i, label in enumerate(labels, start=1):
        file.write(f"{i}. {label}\n")
