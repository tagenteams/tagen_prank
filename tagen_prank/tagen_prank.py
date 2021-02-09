
class TagenPrank(object):
    """Prank library
    """

    def __init__(self, input_word: str):
        self._input_word = input_word

    @staticmethod
    def say_nanii():
        print('なにィ!!!')

def main():
    prank = TagenPrank('テストなんさなあ')
    prank.say_nanii()
