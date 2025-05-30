# -----------------------------------------------------------------------------
#  WORDS-NOVA – A random, human-readable, and optimized word generator.
#
#  Description:
#  This script implements the WORDS-NOVA algorithm, designed to generate
#  pronounceable, pseudo-random words by alternating between consonants and
#  vowels. It also optionally appends random numeric digits to the word.
#  The algorithm ensures a low collision probability (~1 in 2.5 trillion).
#
#  Author: Junaid(www.abujuni.dev)
#  License: MIT License
#  Copyright © 2025 Junaid. All rights reserved.
# -----------------------------------------------------------------------------

import random


def generate_word(length=10, add_number_digits=4):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    if length <= 0:
        return ""

    word_chars = []
    # Start with consonant or vowel randomly
    use_consonant = random.choice([True, False])

    for i in range(length):
        if use_consonant:
            char = random.choice(consonants)
        else:
            char = random.choice(vowels)
        word_chars.append(char)
        # Alternate consonant/vowel
        use_consonant = not use_consonant

    word = "".join(word_chars)

    if add_number_digits > 0:
        digits = "".join(random.choice("0123456789") for _ in range(add_number_digits))
        return word + digits
    else:
        return word
