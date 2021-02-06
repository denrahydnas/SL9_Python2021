<<<<<<< HEAD
#classwork dice game, use with oop_hands and oop_scores
=======
>>>>>>> 7b0388aa3927513599041eecdfa7b36819a24198
import oop_hands

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)
    def score_twos(self, hand):
        return sum(hand.twos)
    def score_threes(self, hand):
        return sum(hand.threes) 
    def score_fours(self, hand):
        return sum(hand.fours)
    def score_fives(self, hand):
        return sum(hand.fives)
    def score_sixes(self, hand):
        return sum(hand.sixes)


    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)