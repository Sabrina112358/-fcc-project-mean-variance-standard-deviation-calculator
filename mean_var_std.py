import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError( "List must contain nine numbers.")

  # convert to numpy array

  mtx = np.reshape(np.array(list), (3, 3))

  calculations = {
  'mean': [np.mean(mtx, axis=0).tolist(), np.mean(mtx, axis=1).tolist(), np.mean(mtx)],
  'variance': [np.var(mtx, axis=0).tolist(), np.var(mtx, axis=1).tolist(), np.var(mtx)],
  'standard deviation': [np.std(mtx, axis=0).tolist(), np.std(mtx, axis=1).tolist(), np.std(mtx)],
  'max': [np.max(mtx, axis=0).tolist(), np.max(mtx, axis=1).tolist(), np.max(mtx)],
  'min': [np.min(mtx, axis=0).tolist(), np.min(mtx, axis=1).tolist(), np.min(mtx)], 
  'sum': [np.sum(mtx, axis=0).tolist(), np.sum(mtx, axis=1).tolist(), np.sum(mtx)]}

  return calculations