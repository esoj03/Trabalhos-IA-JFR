import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

############################################################
# Custom Types
# NOTE: You do not need to modify these.

"""
You can think of the keys of the defaultdict as representing the positions in
the sparse vector, while the values represent the elements at those positions.
Any key which is absent from the dict means that that element in the sparse
vector is absent (is zero).
Note that the type of the key used should not affect the algorithm. You can
imagine the keys to be integer indices (e.g., 0, 1, 2) in the sparse vectors,
but it should work the same way with arbitrary keys (e.g., "red", "blue", 
"green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problem 4a

def find_alphabetically_first_word(text: str) -> str:
    """
    Given a string |text|, return the word in |text| that comes first
    lexicographically (i.e., the word that would come first after sorting).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() handy here. If the input text is an empty string, 
    it is acceptable to either return an empty string or throw an error.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")

    # Split the input text into words using whitespace as the delimiter
    words = text.split()

    # Check if the list of words is empty
    if not words:
        # You can either return an empty string or raise an error here
        # In this example, I'll return an empty string
        return ''

    # Use the max function with a custom key function to find the first lexicographically word
    first_word = max(words, key=lambda word: word.lower())

    return first_word
    # END_YOUR_CODE


############################################################
# Problem 4b

def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")

    x1, y1 = loc1
    x2, y2 = loc2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

    # END_YOUR_CODE


############################################################
# Problem 4c

def mutate_sentences(sentence: str) -> List[str]:
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 17 lines of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")

    def is_similar(new_sentence, original_words_set):
        new_words = new_sentence.split()
        if len(new_words) != len(original_words_set):
            return False
        for i in range(len(new_words) - 1):
            if new_words[i] + ' ' + new_words[i + 1] not in original_words_set:
                return False
        return True

    def backtrack(current_sentence, remaining_words, original_words_set):
        if not remaining_words:
            return [current_sentence] if is_similar(current_sentence, original_words_set) else []

        similar_sentences = []
        for i in range(len(remaining_words)):
            new_sentence = current_sentence + ' ' + remaining_words[i]
            new_remaining_words = remaining_words[:i] + remaining_words[i + 1:]
            similar_sentences.extend(backtrack(new_sentence, new_remaining_words, original_words_set))

        return similar_sentences

    words = sentence.split()
    original_words_set = set(' '.join([words[i], words[i + 1]]) for i in range(len(words) - 1))
    similar_sentences = backtrack('', words, original_words_set)
    return list(set(similar_sentences))
    # END_YOUR_CODE


############################################################
# Problem 4d

def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Given two sparse vectors (vectors where most of the elements are zeros)
    |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.

    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")

    # Create a list of the products of corresponding elements in v1 and v2
    products = [v1[key] * v2[key] for key in v1 if key in v2]

    # Sum the products to calculate the dot product
    dot_product_value = sum(products)

    return dot_product_value
    # END_YOUR_CODE


############################################################
# Problem 4e

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector, ) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scale is zero, you are allowed to modify v1 to include any
    additional keys in v2, or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")

    if scale == 0:
        # If the scale is zero, you can choose not to add new keys from v2 to v1.
        # In this implementation, we will not add new keys.
        return

    for key, value in v2.items():
        v1[key] = v1.get(key, 0) + scale * value
    # END_YOUR_CODE


############################################################
# Problem 4f

def find_nonsingleton_words(text: str) -> Set[str]:
    """
    Split the string |text| by whitespace and return the set of words that
    occur more than once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")

    # Split the input string into words using whitespace as the delimiter
    words = text.split()

    # Use defaultdict to count word occurrences
    word_counts = collections.defaultdict(int)
    for word in words:
        word_counts[word] += 1

    # Create a set of words that occur more than once
    duplicate_words = {word for word, count in word_counts.items() if count > 1}

    return duplicate_words
    # END_YOUR_CODE
