# tests/test_hangman.py

# Test d'un exemple de fonction dans hangman.py

# Exemple d'une fonction que tu pourrais avoir dans hangman.py
def test_check_letter_in_word():
    from src.hangman import check_letter_in_word

    word = "pendu"
    letter = "p"
    result = check_letter_in_word(word, letter)

    assert result  # On attend True car "p" est dans "pendu"

    letter = "z"
    result = check_letter_in_word(word, letter)

    assert not result  # On attend False car "z" n'est pas dans "pendu"
