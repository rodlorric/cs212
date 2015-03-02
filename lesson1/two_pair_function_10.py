# -----------
# User Instructions
# 
# Define a function, two_pair(ranks).

def two_pair_sphex_very_sad(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pairs = {}
    count = 0
    first = ranks[0]
    for r in ranks:
        print (str(first)+'-'+str(r))
        if first-r == 0:
            if count==0:
                pairs[count] = r
                count += 1
            else:
                pairs[count] = r
                count += 1
        first = r
        print count
    if (count <= 1): return None    
    else: return (pairs[0], pairs[1])
    
def two_pair(ranks):
    upperpair = kind(2, ranks)
    lowerpair = kind(2, list(reversed(ranks)))
    if upperpair and lowerpair and upperpair != lowerpair:
        return upperpair, lowerpair
    else: return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "TD TC 3H 7C 7D".split() # Two Pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    print two_pair(tpranks)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (10, 7)
    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

print test()