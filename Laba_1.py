##Task_1
#def printDiagonalSums(mat, n): 
#    result = 0;
#    for i in range(0, n):  
#        for j in range(0, n):  
  
            
#            if (i != j): 
#                result += mat[i][j] 
   
          
#    return result; 
  

#a = [[ 3, 4, 4, 1 ], 
#     [ 5, 6, 9, 8 ],  
#     [ 1, 0, 3, 9 ], 
#     [ 5, 6, 3, 1 ]] 
#print(printDiagonalSums(a, 4))

##Task_2
#def GetWorldWithThreeE(world):
#    allWorld = world.split()
#    lenght = len(allWorld)
#    for i in range(0, lenght):
#        if allWorld[i].count("e") == 3:
#            print(allWorld[i])

#GetWorldWithThreeE("Some energetic iseheekeie perfomance cheese degree deeded world letter alienee")

##Task_3
#import numpy as np

#x = int(input("Введіть x масиву:"))

#y = int(input("Введіть y масиву:"))

#array = np.random.randint(1,5,(x,y))
#print(array)
#sum = 0.0;
#count = 0;
#for i in range(0,x):
#    for j in range(0,y):
#        if array[i,j] < 3 : 
#            sum+=array[i,j]
#            count+=1


#print("avg: "+str(sum/count));
#print("sum: "+str(int(sum)));

##Task_4
#import pylab
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.colors import LinearSegmentedColormap
#from matplotlib import cm
#import numpy

#def makeData (step):
    
#    x = numpy.arange (-numpy.pi * 2, numpy.pi * 2, step)
#    y = numpy.arange (-numpy.pi * 2, numpy.pi * 2, step)
#    xgrid, ygrid = numpy.meshgrid(x, y)

#    zgrid = (numpy.sin (xgrid) /  xgrid) * numpy.abs(numpy.cos(ygrid))
#    return xgrid, ygrid, zgrid

#x, y, z = makeData(0.01)

#fig = pylab.figure()
#axes = Axes3D(fig)

#axes.plot_surface(x, y, z, rstride=2, cstride=2, cmap = cm.jet)

#pylab.show()

##Task_5
#from pandas import DataFrame

#data = {'Gender': ['male','male','female','male','male','female','female','male','female','male'],
#        'Age': [21,33,12,45,30,55,30,84,42,30]
#        }

#df = DataFrame(data, columns= ['Gender', 'Age'])
#print( df.query('Gender=="male" & Age == 30'))