# Plans for the first release
- Frequency List
- Pair Sentences
- Tokenization, Stemming and Lemmatization
- Scoring Pair Sentences according to difficulty
- Assigning Frequency List to Pair Sentences
- Including Audio from Tatoeba
- Anki Deck automatic generation

# After the first release
- Try to prioritize Pair Sentences with already seen words from the Frequency List (how to engage this problem?)
- Better packaging of solution for easier usage
- Test coverage to facilitate understanding and colaboration
- Parametrization to facilitate usage of alternative resources/corpus
- Performance tuning

-----------------------

Thanks to `hermitdave`/[FrequencyWords](https://github.com/hermitdave/FrequencyWords) for the frequency lists used in this project. 
Thanks to `kmicklas`/[sentence-pairs](https://github.com/kmicklas/sentence-pairs) for the logic to extract pairs from Tatoeba files.

Thanks to (https://en.wiki.tatoeba.org/articles/show/make-anki) for a clear example on how to export translated sentences from Tatoeba.

How to get audios:
Judging by this discussion on [GitHub](https://github.com/Tatoeba/tatoeba2/issues/547), you should be able to access audio files using just their language code and sentence ID. The URL scheme seems to be `http://audio.tatoeba.org/sentences/<<language code>>/<<sentence id>>.mp3`
