notes = list(map(int, input().split()))
ascending, descending = False, False
for before_note, after_note in zip(notes, notes[1:]):
    if before_note < after_note:
        ascending = True
    else:
        descending = False

if ascending and descending:
    print("mixed")
elif ascending:
    print('ascending')
else:
    print(descending)
