def get(f):
    def get(s, *arg, **kwarg):
        for i in (s.mzone, s.szone):
            for i in i:
                for i in i:
                    if get in i.hook:
                        arg, kwarg = i.hook[get](*arg, **kwarg)
        return f(*arg, **kwarg)
    return get
def set(f):
    def set(s, *arg, **kwarg):
        for i in (s.mzone, s.szone):
            for i in i:
                for i in i:
                    if set in i.hook:
                        arg, kwarg = i.hook[set](*arg, **kwarg)
        f(*arg, **kwarg)
        for i in (s.mzone, s.szone):
            for i in i:
                for i in i:
                    if set in i.hook:
                        arg, kwarg = i.trig[set](*arg, **kwarg)
    return set
class gu:
    def __init__(s, deck0, deck1, tp):
        deck0   = s.loaddeck(deck0)
        deck1   = s.loaddeck(deck1)
        s.deck  = [deck0[1:], deck1[1:]]
        s.hand  = [[], []]
        s.mzone = [deck0[:1], deck1[:1]]
        s.szone = [[], []]
        s.grave = [[], []]
        s.tp    = p
        s.shuffle(0)
        s.draw(0, 5)
        s.diaodu(0)
        s.shuffle(1)
        s.draw(1, 5)
        s.diaodu(1)
        while True:
            s.tick('draw')
            s.setmp(0, 6)
            s.setmp(1, 6)
            for i in (s.mzone, s.szone):
                for i in i:
                    for i in i:
                        if i.T:
                            s.transpose(i)
            
            s.draw(s.tp)
            s.tick('main')
            t = effect()
            while t.name != 'battle':
                t = s.cp()
                s.select(t, s.effect(s.hand[t]+s.mzone[t]+s.szone[t], s.usable)).run()
            s.phase(s.battle)
            t = s.cp()
            while t:
                s.select(t[0], s.effect(t[1], s.usable)).run(s)
                t = s.cp()
            s.tp = 1 - s.tp
    @staticmethod
    def loaddb(db='db.csv'):
        with open(db) as f:
            gu.db = [i[:-1].split(',') for i in f]
    def loaddeck(s, src):
        with open(src) as f:
            return [card(i[:-1], s.db[int(i)]) for i in f]
    @get
    def cp(s):
        if s.phase() != 'battle': return s.tp if s.mp[s.tp]() >= s.mp[1-s.tp]() else 1-s.tp
        max = -1
        maxc = None
        for i in s.mzone:
            for i in i:
                if (i.speed > max or (i.speed == max and i.p == s.tp)):
                    max = i.speed
                    maxc = i
        return maxc
    def effect(s, cards, filte=lambda e: e.chk(s)):
        e = [i.effect for i in cards] if s.phase != 'battle' else [i.beffect for i in cards]
        return filter(e, filte)
    @set
    def setmp(s, p, n):
        s.mp[p] = n
    @set
    def tick(s, phase):
        s.phase = phase    
    @set
    def move(s, cards, loc, seq=-1):
        for i in cards if type(cards) == list else (cards,):
            i.loc.remove(i)
            loc.insert(seq, i)
            i.loc = loc
    @set
    def draw(s, p, n=1):
        if len(s.deck[p]) < n: s.win(p, 'cant draw enough')
        s.move(s.deck[:p], s.hand[p])
    @set
    def shuffle(s, p):
        shuffle(s.deck[p])
    @set
    def summon(s, cards, p=None):
        if type(cards) != list: cards = [cards]
        s.move(cards, s.mzone[cards[0].p if p is None else p])
    @set
    def transpose(s, cards):
        for i in cards if type(cards) == list else (cards,):
            i.T = not i.T
    @set
    def destroy(s, destroyer, destroyed):
        move(destroyed, s.grave[destroyed.p])
    @set
    def damage(s, damager, damaged, n):
        damaged.hp -= n
        if damaged.hp <= 0:
            if damaged.type & card.hero: s.win(1-damaged.p, 'hero hp reach 0')
            else: s.destroy(damager, damaged)
    @set
    def attack(s, attacker, attacked, transpose=True):
        if transpose and not attacker.T: s.transpose(attacker)
        s.damage(s, attacker, attacked, attacker.atk)
