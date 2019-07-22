import tensorflow as tf

# # 方式一
# def my_fun(x):
#     w1 = tf.Variable(tf.random_normal([1])[0])
#     b1 = tf.Variable(tf.random_normal([1])[0])
#     r1 = w1*x +b1
#
#     w2 = tf.Variable(tf.random_normal([1])[0])
#     b2 = tf.Variable(tf.random_normal([1])[0])
#     r2 = w2 * r1 + b2
#
#     return r1,w1,b1,r2,w2,b2
#
# # 下面两个代码还是属于图的构建
# x =tf.constant(3,dtype=tf.float32)
# r = my_fun(x)
#
# with tf.Session(config=tf.ConfigProto(log_device_placement=True,allow_soft_placement=True)) as sess:
#     # 初始化
#     tf.global_variables_initializer().run()
#     # 执行结果
#     print(sess.run(r))

# 方式二
def my_fun(x):
    w = tf.get_variable(name='w',shape=[1],initializer=tf.random_normal_initializer(1.0))[0]
    b = tf.get_variable(name='b',shape=[1],initializer=tf.random_normal_initializer())[0]
    # w = tf.Variable(tf.random_normal([1])[0],name='w')
    # b = tf.Variable(tf.random_normal([1])[0],name='b')
    w_assign_op = tf.assign(w,w*2.0)
    with tf.control_dependencies([w_assign_op]):
        r = w * x + b
    return r,w,b

def func(x):
    with tf.variable_scope('po1',reuse=tf.AUTO_REUSE):
        r1 = my_fun(x)
    with tf.variable_scope('po2', reuse=tf.AUTO_REUSE):
        r2 = my_fun(r1[0])
    return r1,r2

# 下面两个代码还是属于图的构建
x1 =tf.constant(3,dtype=tf.float32)
r1 = func(x1)

x2 =tf.constant(4,dtype=tf.float32)
r2 = func(x2)

with tf.Session(config=tf.ConfigProto(log_device_placement=True,allow_soft_placement=True)) as sess:
    # 初始化
    tf.global_variables_initializer().run()
    # 执行结果
    print(sess.run([r1,r2]))