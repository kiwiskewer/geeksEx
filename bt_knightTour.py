class knightTour:
    def __init__(self,N,x,y):
        self.N = N
        self.sol = [[ -1 for x in range(N)] for y in range(N)]
        # self._xMove = [-1,1,2,2,1,-1,-2,-2]
        # self._yMove = [2,2,1,-1,-2,-2,-1,1]
        self._xMove = (2, 1, -1, -2, -2, -1, 1, 2)
        self._yMove = (1, 2, 2, 1, -1, -2, -2, -1)
        self.sol[y][x] = 0

    def go(self,x,y,m):
        if m == self.N * self.N:
            return True
        for i in range(8):
            #print(i,m)
            next_x = x + self._xMove[i]
            next_y = y + self._yMove[i]
            if self.isSafe(next_x, next_y):
                self.sol[next_y][next_x] = m
                if self.go(next_x,next_y,m+1):
                    return True
                else:
                    self.sol[next_y][next_x] = -1
        return False

    def isSafe(self,x,y):
        safe = x >= 0 and x < self.N and y >=0 and y < self.N and self.sol[y][x] == -1
        return safe

    def printSol(self):
        for y in range(self.N):
            for x in range(self.N):
                print('{} '.format(self.sol[y][x]),end='')
            print('')

ktour = knightTour(8,0,0)
ktour.printSol()
print('gogogo')
ktour.go(0,0,1)
ktour.printSol()

