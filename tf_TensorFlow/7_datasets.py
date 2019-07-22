import tensorflow as tf
import numpy as np

dateset = tf.data.Dataset.from_tensor_slices(np.array([1,2,3,4,5]))

# 非eager模式下读取dataset
iterator = dateset.make_one_shot_iterator()#从头到尾读取一次
one_element = iterator.get_next()
with tf.Session(config=tf.ConfigProto(log_device_placement=True))  as sess:
    for i in range(5):
        print(sess.run(one_element))