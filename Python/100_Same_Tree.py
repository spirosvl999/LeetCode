class Solution(object):
    def isSameTree(self, p, q):
        if p == None or q == None:
            return p==q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
