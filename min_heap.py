class MinHeap:
    def __init__(self,num_vert):
        self.heapList = [0]
        self.currentSize = 0
        self.vertices=[-2]*num_vert

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i][1] < self.heapList[i // 2][1]:
                self.vertices[self.heapList[i][0]]=i//2
                self.vertices[self.heapList[i // 2][0]]=i
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i=i//2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.vertices[k[0]]=self.currentSize
      self.percUp(self.currentSize)

    def replace(self,i,k):
        self.heapList[i]=k
        self.percUp(i)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i][1] > self.heapList[mc][1]:
              self.vertices[self.heapList[i][0]] = mc
              self.vertices[self.heapList[mc][0]] = i
              self.heapList[mc],self.heapList[i]= self.heapList[i],self.heapList[mc]
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
        #min
        retval = self.heapList[1]

        #swap min and last element
        self.vertices[self.heapList[self.currentSize][0]]=1
        self.heapList[1] = self.heapList[self.currentSize]


        self.currentSize = self.currentSize - 1
        self.heapList.pop()

        self.percDown(1)
        return retval
