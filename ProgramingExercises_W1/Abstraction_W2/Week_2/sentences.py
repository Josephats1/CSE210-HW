import random

# Function to get a randomly chosen determiner based on quantity
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter:
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this function 
            will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

# Function to get a randomly chosen noun based on quantity
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will return one of these single nouns:
        "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of these plural nouns:
        "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"
    Parameter:
        quantity: an integer that determines if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

# Function to get a randomly chosen verb based on quantity and tense
def get_verb(quantity, tense):
    """Return a randomly chosen verb. 
    If tense is "past", this function will return one of the following verbs:
        "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, it will return one of:
        "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is not 1, it will return one of:
        "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"
    If tense is "future", it will return one of:
        "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"
    Parameters:
        quantity: an integer determining if the verb is singular or plural.
        tense: a string that determines the verb tense ("past", "present", or "future").
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    return random.choice(words)

# Function to get a randomly chosen preposition
def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["in", "on", "under", "over", "with", "at", "by", "through"]
    return random.choice(prepositions)

# Function to build a prepositional phrase (a determiner + noun with a preposition)
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase with a determiner, noun, and preposition."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()
    return f"{preposition} {determiner} {noun}"

# Function to build and return a sentence using the determiner, noun, verb, and optional prepositional phrase
def make_sentence(quantity, tense):
    """Build and return a sentence with four parts: a determiner, a noun, a verb, and a prepositional phrase."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

# Main function to generate and print six sentences
def main():
    # Generate and print sentences with different combinations of quantity and tense
    print(make_sentence(1, "past"))  # Single past
    print(make_sentence(1, "present"))  # Single present
    print(make_sentence(1, "future"))  # Single future
    print(make_sentence(2, "past"))  # Plural past
    print(make_sentence(2, "present"))  # Plural present
    print(make_sentence(2, "future"))  # Plural future

# Call the main function to execute the program
if __name__ == "__main__":
    main()
