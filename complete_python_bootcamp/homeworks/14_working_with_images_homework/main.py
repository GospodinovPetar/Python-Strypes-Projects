from PIL import Image

words = Image.open("words.png")
word_windows = Image.open("word_windows.png")
mask = word_windows.resize((1015, 559))

mask.putalpha(200)
words.paste(mask, (0, 0), mask)

words.show()
