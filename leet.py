class Solution(object):
    
    def preProcess(self,matrix):
        z=list()
        for i in xrange(len(matrix[0])):
            for j in xrange(len(matrix)):
                if matrix[i][j] == 0:
                    z.append((i,j))
                else:
                    matrix[i][j] = 10000
        return z
    
    def within(self,matrix, x,y):
        return True if x < len(matrix[0]) and y < len(matrix) and x >= 0 and y >= 0 else False
    
    def distance(self, matrix, count, x, y):
        
        if self.within(matrix,x,y):
            print str(x)+" "+str(y)+" "+str(count)+" "+str(matrix[x][y])
            if matrix[x][y] > count or count == 0:
                matrix[x][y] = count
                matrix = self.distance(matrix,count+1,x+1,y+1)
                matrix = self.distance(matrix,count+1,x-1,y+1)
                matrix = self.distance(matrix,count+1,x+1,y-1)
                matrix = self.distance(matrix,count+1,x-1,y-1)
        return matrix
                    
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        z = self.preProcess(matrix)
        print z
        for each in z:
            matrix = self.distance(matrix,0, each[0], each[1])
        return matrix

for each in Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]):
    print each
