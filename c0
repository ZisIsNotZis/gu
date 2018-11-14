import effect

class doveAll(effect.effect):
    @effect.OncePerTurn
    def run(s, gu, chk=False):
        toBeTransposed = []
        for zone in (gu.mzone, gu.szone):
            for playerZone in zone:
                for card in playerZone:
                    if not card.T:
                        toBeTransposed.append(card)
        if chk:
            return toBeTransposed
        gu.transpose(toBeTransposed)
    
igni = [doveAll]
move = []
hook = []
trig = []
