class card:
    def __init__(s, id, dbrec):
        s.db  = dbrec
        s.atk = dbrec[4]
        s.spd = dbrec[5]
        s.hp  = dbrec[6]
        s.T   = False
        exec('from c'+id+' import *')
        s.hook = hook
        s.trig = trig
        s.igni = igni
        s.move = move
