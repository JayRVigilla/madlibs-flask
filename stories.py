"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.get_result_text(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def get_result_text(self, answers):
        """Return result text from dictionary of {prompt: answer, ...}."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

silly_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

# long_story = Story([],""" STORY_GOES_HERE {}""")
vacation_story = Story(["adjective1", "adjective2", "noun1", "noun2",
"plural_noun1","game", "plural_noun2", "verb_ending_in_ING_1",
"verb_ending_in_ING_2", "plural_noun3", "verb_ending_in_ING_3", "noun3",
"plant", "part_of_body","place", "verb_ending_in_ING_4", "adjective3",
"number", "plural_noun4"],
"""A vacation is when you take a trip to some {adjective1} place with your
{adjective2} family. Usually you go to some place that is near a/an {noun1} or
up on a/an {noun2}. A good vacation place is one where you can ride
{plural_noun1} or play {game} or go hunting for {plural_noun2} . I like to
spend my time {verb_ending_in_ING_1} or {verb_ending_in_ING_2}.

When parents go on a vacation, they spend their time eating three
{plural_noun3} a day, and fathers play golf, and mothers sit around
{verb_ending_in_ING_3}. Last summer, my little brother fell in a/an {noun3} and
got poison {plant} all over {part_of_body}. My family is going to go to (the)
{place}, and I will practice {verb_ending_in_ING_4}. Parents need vacations
more than kids because parents are always very {adjective3} and because they
have to work {number} hours every day all year making enough {plural_noun4} to
pay for the vacation.""")