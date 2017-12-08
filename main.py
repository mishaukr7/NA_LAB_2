import matplotlib.pyplot as plt
import fractalset
import function as f
import matplotlib.colors as colors


plt.xticks([])
plt.yticks([])


'''
FRACTAL MANDELBROT 
'''
# h_w = [1024, 1024]
# x = [-2, 1.5]
# y = [-1.5, 1.5]
# iteration = 500
# border = 2
# plt.imshow(fractalset.mandelbrot_set(h_w[0], h_w[1], x[0], x[1], y[0], y[1], iteration, border, f.f_5),
#            cmap='bone_r')


'''
FRACTAL Julia 0.285 0.01
'''

c_re_im = [0.6, 0.55]
h_w = [1024, 1024]
x = [-1.5, 1.5]
y = [-1.5, 1.5]
iteration = 1000

plt.imshow(fractalset.julia_set(h_w[0], h_w[1], c_re_im[0], c_re_im[1], x[0], x[1],
                                y[0], y[1], iteration, f.f_4),
           cmap='bone_r')


plt.show()
