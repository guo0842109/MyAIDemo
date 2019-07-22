import tensorflow as tf
# 实现一个累加器，并且每一步均输出累加器的结果值
# 1、定一个变量
x = tf.Variable(1,dtype=tf.int32,name='v_x')
# 2、变量的更新assign， ref指定更新的变量名称
assign_op = tf.assign(ref=x,value= x+1)
# 变量初始化
x_init_op = tf.global_variables_initializer()

# 3、运行
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    sess.run(x_init_op)
    for i in range(5):
        r_x = sess.run(x)
        print(r_x)
#         执行跟新操作
        sess.run(assign_op)


# 编写一段代码，实现动态的更新变量的维度数
# 1、定义一个不定形状的变量
x = tf.Variable(
    initial_value=[],#给定一个不固定的值
    dtype=tf.float32,
    trainable=False,#不把它加载缓存区（只有不定形状才是false）
    validate_shape= False#设置为True，表示在变量更新的时候，进行shape检查，默认为true
)

# 2、变量更改
contact = tf.constant([x,[0,0]],axis=0)
#实现一个求解阶乘的代码

