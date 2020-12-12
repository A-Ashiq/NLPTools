from typing import Union

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_word_cloud(text: Union[str, list[str]]) -> None:

    if type(text) is list:
        text = " ".join(text)

    wordcloud = WordCloud(background_color="white", mask=None, collocations=False)
    wordcloud.generate(text)

    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    
