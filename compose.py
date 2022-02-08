import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) # we are turining whitespaces into just spaces
        text = text.lower() # making everything lowercase to compare stuffs
        # now we could be complex and deal with everything punctuations, but there are cases where 
        # you might add a period such as [Mr, Blackish],but that is not really 
        # a punctuation, so we just remove all punctuations
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = words[:1000]

    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)
        # set our word to the 
        prev_word = word_vertex
    # now remembering that we want to generate a probabilty mappig before composing 
    # this might just be where toimplement such
    g.generate_probability_mappings()
    
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    # step 1: get word from text
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song in os.listdir('songs/{}'.format(artist)):
        # if song == '.DS_Store':
        #     continue
        # words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))
        
    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()