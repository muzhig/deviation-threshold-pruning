import numpy as np
from matplotlib import pyplot as plt

pts = np.float32([
    (4.0,4.0),(4.1,4.1),(4.1,4.0),
    (3.9,4.0),(3.9,4.1),(3.9,3.9),
    (4,4.5),(3.8,3.8),(4.2,3.9),
    (4.1,4.1),(4.5,4.1),(4.5,3.7),

    (7,2),(7,1),(7,6),(8,6),(10,6),(7,7),(8,4),
    ])

mean_pt = np.mean(pts,axis=0)
mean_x,mean_y = mean_pt
diffs = np.apply_along_axis(np.linalg.norm,1,pts - mean_pt)
mean_diff = np.mean(diffs)

filtered = np.float32([pts[i] for i,diff in enumerate(diffs) if diff <= mean_diff])
filtered_mean = np.mean(filtered,axis=0)

plt.plot(pts[:,0],pts[:,1],'ro')
plt.plot(mean_x,mean_y,'w^')
plt.plot(filtered[:,0],filtered[:,1],'bo')
plt.plot(filtered_mean[0],filtered_mean[1],'w^')
plt.show()
