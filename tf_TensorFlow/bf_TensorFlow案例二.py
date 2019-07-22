import tensorflow as tf

a = tf.Variable([1,2,3],dtype=tf.int32,name='a')
b = tf.constant(2,dtype=tf.int32,name='b')

c= a+b


# with tf.device('/cpu:0'):
#      #这个代码块中定义的操作，会在tt.device指定的设备上运行
#      #有一些操作。是不会在GPU上运行的（一定要注意）
# 如果安装的是TensorFlow cpu版本，没法指定运行环境
#      a = tf.Variable([1, 2, 3], dtype=tf.int32, name='a')
#      b = tf.constant(2, dtype=tf.int32, name='b')
#      c = a + b

with tf.Session(config=tf.ConfigProto(log_device_placement=True,allow_soft_placement=True)) as sess:
    tf.global_variables_initializer().run()
    print(c.eval())