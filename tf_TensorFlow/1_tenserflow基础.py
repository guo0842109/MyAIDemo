import tensorflow as tf
#常量
a = tf.constant(2)
b = tf.constant(3)
c = a+b
with tf.Session() as sess:
    print(sess.run(c))

