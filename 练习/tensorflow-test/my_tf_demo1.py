import tensorflow as tf

import numpy as np


a = tf.constant(dtype=tf.float32,shape=[2,2],value=np.ones([2,2]))
b = tf.get_variable(dtype=tf.float32,shape=[2,2],name = 'b')
b= a*2
c = tf.placeholder(dtype=tf.float32,shape=[2,2],name = 'c')

c  = tf.multiply(a,b)

with tf.Session(config=tf.ConfigProto(log_device_placement=True,allow_soft_placement=True)) as sess:
    tf.global_variables_initializer().run()
    print(sess.run(b))
    print(sess.run(c,feed_dict={b : np.random.random([2,2])}))