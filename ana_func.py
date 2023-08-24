# This is code for doing DFT and IDFT
# Author: Yu-Chuan Kan
# Date: Aug 24, 2023

# Function for doing DFT
def DFT(arr):
  
  '''
  input:
    arr :: 1D or 2D is satisfied with computing methods in the function.
  process:
    dim  :: length of the dimension of the array going to be done DFT
    n, k :: exponent in DFT
  output:
    C_k, S_k :: cosine and sine coefficients of DFT
  '''

  dim = round(arr.shape[1])

  n = np.matrix(np.linspace(0, dim-1, dim))
  k = 2 * np.pi / dim * (np.matrix(np.linspace(0, dim-1, dim)))

  C_k = np.cos(k.T * n) * np.matrix(arr).T / dim
  S_k = np.sin(k.T * n) * np.matrix(arr).T / dim

  return C_k, S_k

# Function for doing IDFT
def IDFT(C_k, S_k, arr):

  '''
  input:
    arr :: 1D or 2D is satisfied with computing methods in the function.
    C_k, S_k :: cosine and sine coefficients of DFT
  process:
    dim  :: length of the dimension of the array going to be done IDFT
    n, k :: exponent in IDFT
    c, s :: inverse array of IDFT
  output:
    C_k_out, S_k_out :: inverse cosine and sine coefficients of IDFT.
  '''
  
  dim = round(arr.shape[0])

  n = np.matrix(np.linspace(0, dim-1, dim))
  k = 2 * np.pi / dim * np.matrix(np.linspace(0, dim1, dim))

  c = np.cos(k.T * n[:, :round(dim / 2)])
  s = np.sin(k.T * n[:, :round(dim / 2)])

  C_k_out = (c * C_k).T
  S_k_out = (s * S_k).T

  return C_k_out, S_k_out
