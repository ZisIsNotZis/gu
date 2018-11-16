# 咕咕音

# [永] 解放自己2只怪兽才能召唤
@loc(gu.hand)
@hook(gu.summon, selfOnly)
@mustUse
def doveDontWantToMove(c, gu, chk, toBeSummoned, hookChk):
    if hookChk: return len(gu.mzone[c.p]) >= 2
    gu.release(gu.select(c.p, gu.mzone[c.p], 2))

# [启] 横置场上所有怪兽 (不能空发)
@ignite
@oncePerTurn
def doveAll(c, gu, chk):
    toBeDoved = filter(gu.mzone, lambda card: not card.T)
    if chk: return toBeDoved
    gu.transpose(toBeDoved)

# [战斗阶段外][被横置时] 英雄回复5HP
@trigger(gu.transpose, selfOnly)
def doveIsGood(c, gu, chk, theTransposed):
    if chk: return gu.phase != 'battle'
    gu.recover(gu.mzone[c.p][0], 5)

# [被破坏时] 特招两个咕咕蛋 (有格子的场合)
@trigger(gu.destroy, selfOnly)
def doveMustNotDie(c, gu, chk, theDestroyed):
    if chk: return len(gu.mzone[c.p]) <= 4
    gu.summon((card(gu.db[1]), card(gu.db[1])))
