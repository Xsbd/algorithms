# python3
import math

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # for i in range(len(self._data)):
    #  for j in range(i + 1, len(self._data)):
    #    if self._data[i] > self._data[j]:
    #      self._swaps.append((i, j))
    #      self._data[i], self._data[j] = self._data[j], self._data[i]
    for i in range(math.ceil(len(self._data)/2)-1, -1, -1):
      HeapBuilder.ShiftDown(self,i)

  def ShiftDown(self,i):
    if 2*i+1 >= len(self._data):
        return		#return if it has no leaf
    if 2*i+2 < len(self._data):		# right child exists
        key = min(self._data[i], self._data[2*i+1], self._data[2*i+2])
    else:				# no right child
        key = min(self._data[i], self._data[2*i+1])
    if self._data[i] > key:
      if self._data[2*i+1] > key:
        self._swaps.append((i,2*i+2))
        self._data[i], self._data[2*i+2] = self._data[2*i+2], self._data[i]
        key = 2*i+2
      else:
        self._swaps.append((i,2*i+1))
        self._data[i], self._data[2*i+1] = self._data[2*i+1], self._data[i]
        key = 2*i+1
      return HeapBuilder.ShiftDown(self,key)
    else:
      return

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
