# author: Hendrik Werner // s4549775
# author: Constantin Blach // s4329872

import numpy
import scipy

# assignment 1.3.1

# assignment 1.3.2
v1 = numpy.array([14, 22, 13, 44, 25])
v2 = numpy.array([41, 5, 1, 3, 5])

print(scipy.spatial.distance.cosine(5 * v1, v2)
      == scipy.spatial.distance.cosine(v1, v2))
