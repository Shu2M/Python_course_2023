from neural import Neural


n = Neural()
n.training()


z_0 = n.inference([[10.22, 248.07, 28.74, 7.51, 3.93, 2.83, 13.78, 84.60, 2.67]])
z_1 = n.inference([[6.28, 258.30, 13.77, 7.48, 3.28, 5.63, 16.46, 73.51, 4.10]])

print('z_0: ', z_0)
print('z_1: ', z_1)
