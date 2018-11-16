# 厨卡

# [行] 对全部敌方单位各进行1次攻击，每破坏1只怪兽抽1
@move
def attackAll(s, gu, chk):
	if chk: return True
	draw = 0
	for i in s.mzone[1-s.p]:
		gu.attack(s, i)
		if i.loc != s.mzone[1-s.p]:
			draw += 1
	if draw > 0: gu.draw(s.p, draw)
