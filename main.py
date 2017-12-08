import matplotlib.pyplot as plt
import fractalset
import function as f
import matplotlib.colors as colors


plt.xticks([])
plt.yticks([])
norm = colors.PowerNorm(0.3)
'''
FRACTAL MANDELBROT 
'''
#plt.imshow(fractalset.mandelbrot_set(500, 500, -2.5, 1.5, -2, 2, 500, 10, f.f_4), cmap='bone_r')


'''
FRACTAL Julia 0.285 0.01
'''
c_re_im = [-1, 0]
h_w = [1024, 1024]
x = [-2, 2]
y = [-2, 2]
iteration = 500

plt.imshow(fractalset.julia_set(h_w[0], h_w[1], c_re_im[0], c_re_im[1], x[0], x[1],
                                y[0], y[1], iteration, f.f_2),
           cmap='viridis_r', extent=(-2, 2, -2, 2))


plt.show()
