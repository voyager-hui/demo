import numpy as np

a = np.array([[-87.633308037, 41.899602111],
              [-87.620992913, 41.884987192],
              [-87.626214906, 41.892507781],
              [-87.632746489, 41.880994471],
              [-87.63186395, 41.892042136],
              [-87.90303966100002, 41.97907082],
              [-87.618868355, 41.890922026],
              [-87.655998182, 41.944226601],
              [-87.626210532, 41.899155613000005],
              [-87.612945414, 41.891971508000005],
              [-87.642648998, 41.879255084],
              [-87.617358006, 41.859349715],
              [-87.750934289, 41.785998518],
              [-87.655878786, 41.96581197],
              [-87.663416405, 41.986711799999995],
              [-87.69915534299999, 41.92276062],
              [-87.67016685700001, 42.009622881],
              [-87.620334624, 41.857183858],
              [-87.72345239, 41.953582125],
              [-87.77116670299999, 41.978829526],
              [-87.64396537, 41.949829346],
              [-87.804532006, 41.985015101],
              [-87.666596265, 41.775928827],
              [-87.726929842, 41.769778059000004],
              [-87.58747925799999, 41.805911699]])
np.save("data.npy", a)


# method 1
b = np.load("data.npy")
print("待发送的信息:", b)
print("type(b):", type(b))
for i in range(25):
    msg = str(b[i, 0]) + ',' + str(b[i, 0])
    print('msg:', msg)
    print('len(msg):', len(msg))
    print('type(msg):', type(msg))

# method 2
msg = input("Please input:")
print('msg:', msg)
print('len(msg):', len(msg))
print('type(msg):', type(msg))

