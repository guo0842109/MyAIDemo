import tensorflow as tf
import numpy as np

a = tf.constant(np.ones([4,4]))
b = tf.constant(np.ones([4,4]))
print(a)

session = tf.Session()
print(session.run(a*b))
print(session.run(np.matmul(a,b)))