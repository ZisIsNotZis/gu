# 咕咕蛋

# [诱] 出场的第2个回合结束时，解放自己，召唤1只咕咕音（不需要解放或费用）
@hook(gu.tick, 'draw')
def hereComesTheDove(c, gu, chk, *_):
	if chk: return gu.turn == c.turn + 1
	gu.release(c)
	gu.summon(card(gu.db[0]))

# [永] 1回合1次不会被破坏
@hook(gu.__init__): # 注册"被破坏次数"
def defendInit(c, gu, chk):
	c.desTurn = 0

@hook(gu.destroy, run):
def defend(c, gu, chk):
	if c.desTurn < gu.turn:
		c.desTurn = gu.turn
		return True
