# 黑洞

# 破坏所有随从
@spell
def blackhole(c, gu, chk):
	if chk: return len(gu.mzone[0]) > 1 or len(gu.mzone[1]) > 1
	gu.destroy(gu.mzone[0][1:] + gu.mzone[1][1:])

# 解放场上3只鸽子生物，这张卡从墓地加入手卡
@loc(gu.grave)
@ignite
def recycle(c, gu, chk):
	if chk: return filter(gu.mzone, lambda x: x.israce('dove'))
	gu.release(gu.select(c.p, sum(gu.mzone,[]), 3))
	gu.tohand(c)
