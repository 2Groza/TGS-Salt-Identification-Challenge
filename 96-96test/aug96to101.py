import numpy as np
def aug101(test_pred_now):
    up = test_pred_now[:5,:,0]
    half = np.vstack((up,test_pred_now[:,:,0]))
    left = half[:,:5]
    final = np.hstack((left,half))
    final = np.reshape(final,[101,101,1])
    return final
