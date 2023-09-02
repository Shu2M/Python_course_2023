def stop_words_filter(stop_words: list, sentence: str) -> str:
    return ' '.join(filter(lambda w: w not in stop_words, sentence.split()))


print(stop_words_filter(['Python', 'php', 'go', 'C'], ' php ppg go Python fsfsdfsdf '))
