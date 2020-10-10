from heapq import nlargest

class Candidate:
    _id=0
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def __str__(self):
        return str(self.id)+str(self.name)
 
class Voting:
    def __init__(self, candidates):
        self.candidates= candidates
        self.votes = [ (0,cand.id) for cand in candidates]

    def voteCandidate(self, cnd_id):
        self.votes[cnd_id]=(self.votes[cnd_id][0]+1,self.votes[cnd_id][1])

    def getTopK(self,k):
        votes_k= nlargest(k,self.votes)
        for votes,id in votes_k:
            print("name = ",self.candidates[id].name,"votes =",votes)

	
cands = [Candidate("Modi",0),Candidate("Gandhi",1),Candidate("Kej",2),Candidate("irani",3)]
for cand in cands:
    print(cand)
v=Voting(cands)
v.voteCandidate(0)
v.voteCandidate(0)
v.voteCandidate(0)
v.voteCandidate(2)
v.voteCandidate(1)
v.voteCandidate(0)
v.voteCandidate(0)
v.getTopK(1)
v.voteCandidate(2)
v.voteCandidate(3)
v.voteCandidate(3)
v.voteCandidate(3)
v.getTopK(3)