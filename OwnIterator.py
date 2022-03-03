class Sentence:

    def __init__(self, str):
        self.str = str
        self.index = 0
        self.words = self.str.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence('This is a test')
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
# print(next(my_sentence))

'''
This
is
a
test
Traceback (most recent call last):
  File "C:/D-Drive/learning/Corey-Schafer/OwnIterator.py", line 24, in <module>
    print(next(my_sentence))
  File "C:/D-Drive/learning/Corey-Schafer/OwnIterator.py", line 13, in __next__
    raise StopIteration
StopIteration
'''

# Generator way


def sentence(sentence):
    for word in sentence.split():
        yield word


test_sentence = sentence('hello how are you')
print(next(test_sentence))
print(next(test_sentence))
print(next(test_sentence))
print(next(test_sentence))
print(next(test_sentence))