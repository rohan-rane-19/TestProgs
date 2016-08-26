import numpy as np
import matplotlib.pyplot as plt


def main():
 a = np.random.normal(size=100)
 a = a.reshape((50,2))

 print ("The array mean:",a.mean())
 print ("The array var:",a.var())
 print ("The array std:",a.std())
 print ("The array median:",np.median(a))
 c = np.corrcoef(a)
 print ("The correlation coefeciant is:",c)
 print ("Random array is:",a)
 
 plt.plot(a,'ro')
 plt.xlabel('numbers')
 plt.ylabel('cubes')
 plt.show()
      
if __name__ == '__main__':
 main()