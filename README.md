# Emoji Tales 🧚

Can we tell stories using only emoji? _Emoji Tales_ is inspired by the work of [Warja Laveter](https://en.wikipedia.org/wiki/Warja_Lavater).
Lavater was a 20th-century artist, best known for her [books](https://books-on-books.com/tag/warja-lavater/) that retold classic fairytales.
Her storybooks only contained symbols, not words or pictures.

In that spirit, Emoji Tales translates stories from text to emoji.

<br>

Requires Python3. Run with `python3 emojitales/main.py`.
To translate your own stories, add them as `.txt` files to the `source_texts` directory.

<br>

All sample texts are from D. L. Ashliman's [Folktexts: A Library of Folktales, Folklore, Fairy Tales, and Mythology](https://sites.pitt.edu/~dash/folktexts.html).

<br>

### Future Work

- Optimize emoji search functionality. Current implementation uses direct unicode lookup, does not have wildcard search, and returns the occasional wingding. Add a map of aliased words and better handling for multiples:
  `three little pigs` returns 🐖🐖🐖
  `forest` returns 🌳🌳🌳🌳🌳🌳

<br>

- Enable GUI file browsing and selection for users to translate their own texts (bypassing the need to copy files to `source_texts`). Possibly use the [tkinter library](https://docs.python.org/3/library/tkinter.html)

<br>

- Improve [package management](https://packaging.python.org/en/latest/guides/creating-command-line-tools/#pyproject-toml)
