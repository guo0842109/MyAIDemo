import tensorflow as tf
import numpy as np

a1 = tf.constant(np.ones([4,4])*2)

a2 = tf.constant(np.ones([4,4]))

b1 = tf.Variable(a1)

b2 = tf.Variable(np.ones([4, 4]))

#定义placeholder
# c3 = tf.placeholder(dtype=tf.float32,shape=[4,4])

c2 = tf.placeholder(dtype=tf.float64, shape=[4, 4])

c2_dot_b2 = tf.matmul(c2,b2)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


print(sess.run(c2_dot_b2,feed_dict = {c2 : np.ones([4,4])}))

