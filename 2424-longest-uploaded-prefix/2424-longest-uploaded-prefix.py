class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = list(range(n+2))
        self.LUP = 0
        
    def find(self, i) :
        if i != self.uploaded[i] :
            self.uploaded[i] = self.find(self.uploaded[i])
        return self.uploaded[i]
    
    def upload(self, video: int) -> None:
        self.uploaded[video] = self.find(video+1)
        if video != self.LUP + 1 :
            return
        self.LUP = self.uploaded[video] - 1
        
    def longest(self) -> int:
        return self.LUP


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()