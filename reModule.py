import re

# raw string
print('\tTab')  # it will print Tab with tab key entered at the start
print(r'\tTab')  # \tTab- \t is not handled special way with raw string

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

321-555-4321
123.555.1234
123*555*1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
print(matches)  # <callable_iterator object at 0x0000024C8AD4D948>
for match in matches:
    print(match)  # <re.Match object; span=(1, 4), match='abc'>
    # span is begining and end index of the match, with that help we can do string slicing and get value
print(text_to_search[1:4])  # abc

'''
Metacharacters:
Capital letter negates smaller letter meaning
. - Any character except new line
\d - Digit(0-9)
\D - Not a Digit (0-9)
\w - Word character(a-z, A-Z, 0-9, underscore)
\W - Not a word character
\s - Whitespace (Space, tab, newline)
\S - Not whitespace
\b - word boundary, for example Ha HaHa, here it will match first Ha and second Ha and not third Ha
as there is no boundary space between second and third
\B - not a word boundary
^ - Beginning of string
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^Start')
$ - End of string
pattern = re.compile(r'end$')
'''

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

'''
<re.Match object; span=(67, 79), match='321-555-4321'>
<re.Match object; span=(80, 92), match='123.555.1234'>
'''

# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

# character set match, characters specified in [] will match with string only once
# like if we have -- in the string, it will match only first -
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
for match in pattern.finditer(text_to_search):
    print(match)  # it will match string containing -.

# if we want to match numbers starting from 800 or 900 then pattern will be below
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# range of character to match can be specified with - in []
# pattern = re.compile(r'[a-z]A-Z]'), this will match string containing small case and upper case chars
# pattern = re.compile(r'[^a-z]A-Z]'), this will match characters other than a-zA-z IN STRING
# pattern = re.compile(r'[^b]at'), this will not match bat but all the other strings ending with at.

# Quantifier, which helps in matching multiple characters
'''
Quantifiers:
* - 0 or more
+ - 1 or more
? - 0 or one
{3} - Exact Number
{3,4} - Range of numbers(min, max)
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
'''

# Groups - ()
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')  # \.? matches one or zero instances of ., \. before ?
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

'''
output
<re.Match object; span=(107, 118), match='Mr. Schafer'>
<re.Match object; span=(119, 127), match='Mr Smith'>
<re.Match object; span=(128, 136), match='Ms Davis'>
<re.Match object; span=(137, 150), match='Mrs. Robinson'>
<re.Match object; span=(151, 156), match='Mr. T'>
'''

emails = '''
CoreySchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
# pattern = re.compile(r'[A-Za-z]+@[a-zA-Z]+\.com')  # <re.Match object; span=(1, 23), match='CoreySchafer@gmail.com'>
# pattern = re.compile(r'[A-Za-z.-]+@[a-zA-Z]+\.(com|edu)')
'''
<re.Match object; span=(1, 23), match='CoreySchafer@gmail.com'>
<re.Match object; span=(24, 52), match='corey.schafer@university.edu'>
'''
pattern = re.compile(r'[A-Za-z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nsa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # 3 groups
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))  # group 0 is whole string match like first url is https://www.google.com
    print(match.group(3))


# sub - substitute the match
subbed_urls = pattern.sub(r'\2\3', urls) # 2nd 3rd group in the match
print(subbed_urls)

'''
output
google.com
coreyms.com
youtube.com
nsa.gov
'''

# findall, return matches as list of string
# match function, match doesn't return iterable, this matches things which match at begining of string
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'Start')
# pattern = re.compile(r'sentence'), this will return None as it is not at start of sentence
matches = pattern.match(sentence)
print(matches)  # <re.Match object; span=(0, 5), match='Start'>

# search function, this matches substring at any position of string
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'sentence')
# pattern = re.compile(r'den') # this will return None as no match
matches = pattern.search(sentence)
print(matches)  # <re.Match object; span=(8, 16), match='sentence'>


# flags
pattern = re.compile(r'sentence', re.IGNORECASE)