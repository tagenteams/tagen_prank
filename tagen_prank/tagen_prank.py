import random

class TagenPrank(object):
    """Prank library
    """

    def __init__(self, input_word: str = 'テストなんさなあ'):
        self._input_word = input_word

    @staticmethod
    def captain():
        word_li = [
            'なにィ!!!',
            'くっ!ガッツがたりない! ',
            'サッカーは格闘技',
            '若林源三の噛ませ犬じゃないんだ！！！',
            '単なるデブは全日本にはいらない',
            'お前こそが日本のSGGKだ！',
            '森崎くんだからとれなーい！',
            'もりさきくん　するどいパンチング！　だが、とどかない！',
            '森崎もだ！こんなシュート若林くんならかるく胸でキャッチしてるぞ！',
        ]
        print(random.choice(word_li))

def main():
    prank = TagenPrank()
    prank.captain()
