# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  print(f"original words: {words}")
  filtered = remove_hyphens_and_short_words(words)
  elipsis = add_elipses(filtered)
  ans = print_list(elipsis)
  
  return ans

def remove_hyphens_and_short_words(words):
  for word in words[:]:
    if '-' in word  or len(word) < 10:
      words.remove(word)
  print(f"word List no hyphens or under 10: {words}")
  return words

def add_elipses(words):
  wor = []

  for word in words:
    if len(word) >= 15:
      wor.append(word[0:15] + "...")
    else:
      wor.append(word)
  #words = [word[0:15] + "..." if len(word) >= 15 else word for word in words]

  print(f"word List elipses added: {words}")

  return wor

def print_list(words):
  final_list = f"These words are quite long: {', '.join(words)}"
  #print("word List:" .join())

  return final_list
    
check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'K-O',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
