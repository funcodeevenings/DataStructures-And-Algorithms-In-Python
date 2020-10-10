class SegmentTree:

    def __init__(self,nums):
        self.len=4*len(nums)
        self.tree=[]*self.len
        self.nums=nums
        self.lazy=[0]*self.len
        self.build(0,0,len(nums)-1)

    def build(self,node,start,end):
        if start==end:
            self.tree[node]=self.nums[start]
        else:
            mid=(start+end)//2
            self.build(node*2,start,mid)
            self.build(node*2+1,mid+1,end)
            tree[node]=tree[node*2]+tree[node*2+1]

    def update(self,node,start,end,idx,val):
        if start==end:
            self.nums[start]=self.nums[start]+val
            self.tree[node]=self.tree[node]+val
        else:
            mid=(start+end)//2
            if start<=idx and idx<=mid:
                self.update(node*2,start,mid,idx,val)
            else:
                self.update(node*2+1,mid+1,end,idx,val)
            tree[node]=tree[node*2]+tree[node*2+1]

    def query(self,node,start,end,l,r):
        if r<start or end<l:
            return 0
        if l<=start and end<=r:
            return tree[node]
        mid=(start+end)//2
        p1=self.query(node*2,start,mid,l,r)
        p2=self.query(node*2+1,mid+1,end,l,r)
        return p1+p2

    def updateRange(self,node,start,end,l,r,val):
        if self.lazy[node]!=0:
            self.tree[node] = self.tree[node]+(end-start+1)*lazy[node]
            if start!=end:
                self.lazy[node*2]= self.lazy[node*2]+self.lazy[node]
                self.lazy[node*2+1]= self.lazy[node*2+1]+self.lazy[node]
            self.lazy[node]=0
        if start > end or start > r or end <l:
            return
        if start>=l and end <=r:
            self.tree[node] = self.tree[node]+(end-start+1)*val
            if start != end:
                self.lazy[node*2]=self.lazy[node*2]+val 
                self.lazy[node*2+1]=self.lazy[node*2+1]+val
            return
        mid = (start+end)//2
        self.updateRange(node*2,start,mid,l,r,val)
        self.updateRange(node*2+1,mid+1,end,l,r,val)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]

    def queryRange(self,node,start,end,l,r):
        if start>end or start>r or end<l:
            return 0
        if self.lazy[node]!=0:
            self.tree[node]=self.tree[node]+(end-start+1)*self.lazy[node]
            if start!=end:
                self.lazy[node*2]=self.lazy[node*2]+self.lazy[node]
                self.lazy[node*2+1]=self.lazy[node*2+1]+self.lazy[node]
            self.lazy[node]=0
        if start >=l and end <=r:
            return self.tree[node]
        mid = (start+end)//2
        p1 = self.queryRange(node*2,start,mid,l,r)
        p2 = self.queryRange(node*2+1,mid+1,end,l,r)
        return p1+p2
        
