text = str(input("Enter the text: "))
word = str(input("Enter the word to search for: "))
counter = 0


def search(text, word):
    global counter
    if word in text:
        for _ in text.split():
            if _ == word:
                counter += 1
        return f'Word found {counter} times'
    else:
        return 'Word not found'


print(search(text, word))
