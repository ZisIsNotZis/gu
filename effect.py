# This module should provide base effect type and implement high level effect programming utility

class effect:
    def chk(s, gu): return True
    def run(s, gu): pass

def All(*chk):
    def All(s, gu):
        return all(i(s, gu) for i in chk)
    return All

def Any(*chk):
    def Any(s, gu):
        return any(i(s, gu) for i in chk)
    return Any

def OncePerTurn(run):
    def OncePerTurn(s, gu, chk=False):
        if chk: return s.actTurn < gu.Turn and run(s, gu, True)
        s.actTurn = gu.Turn
        run(s, gu, False)
    return OncePerTurn
