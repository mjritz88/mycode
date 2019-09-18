#!/usr/bin/python3

import re

androidsDream = "In the sumptuous and enormous hotel room \
Rick Deckard sat reading the typed carbon sheets on the \
two androids Roy and Irmgard Baty. In these two cases \
telescopic snapshots had been included, fuzzy 3-D color \
prints which he could barely make out. The woman, he \
decided, looks attractive. Roy Baty, however, is something \
different. Something worse. A pharmacist on Mars, he read. \
Or at least the android had made use of that cover. \
In actuality it had probably been a manual laborer, \
a field hand, with aspirations for something better. \
Do androids dream? Rick asked himself..."

meetsteven = re.sub(r"Roy", "Steven", androidsDream)

print(f"After changing 'Roy' to 'Steven':\n{meetsteven}")

noandroids = re.sub(r"android", "narwhal", meetsteven)

print(f"\nOur new story featuring no androids:\n{noandroids}")

novowels = re.sub(r"[AEIOUaeiou]", "", meetsteven)

print(f"\nOur new story featuring no vowelse:\n{novowels}")
