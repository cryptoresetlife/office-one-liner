"""Make the AI Judge Laugh: one office joke under 200 characters."""
import os

LINE = (
    "Our team cancelled the weekly status meeting to save an hour, "
    "then booked a recurring meeting to decide what to do with the hour."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
