import tensorflow as tf

# 可视化
with tf.device('/cpu:0'):
    with tf.variable_scope('foo'):
        x_init1 = tf.get_variable('init_x',[10],tf.float32,tf.random_normal_initializer())[0]
        x = tf.Variable(initial_value=x_init1,name='x')
        # y = tf.constant(3.0)
        y = tf.placeholder(dtype=tf.float32,name='y')

        z= x+y
    with tf.variable_scope('bar'):
        a=tf.constant(2.0)+5


    w = z*a
    # 开始记录信息(展示需要展示的信息的输出)
    tf.summary.scalar('scalar_init_x',x_init1)
    tf.summary.scalar(name='scalar_init_x',tensor= x)
    tf.summary.scalar('scalar_init_y', y)
    tf.summary.scalar('scalar_init_z', z)
    tf.summary.scalar('scalar_init_w', w)

    # update x
    assign_op = tf.assign(x, x + 1)
    with tf.control_dependencies([assign_op]):
        with tf.device('/gpu:0'):
            out = x*y
        tf.summary.scalar('scalar_out',out)
    with tf.Session(config=tf.ConfigProto(log_device_placement=True,allow_soft_placement=True)) as sess:
        merged_summary= tf.summary.merge_all()
        # 得到输出到文件的对象
        writer = tf.summary.FileWriter('./result',sess.graph)
       #初始化
        sess.run(tf.global_variables_initializer())
#     print

        for i in range(1,5):
            summary,r_out,r_x,r_w = sess.run([merged_summary,out,x,w],feed_dict={y:i})
            print('{},{},{}'.format(r_out,r_x,r_w))

        #     关闭通道，程序会默认关闭，写不写没关系
        writer.close()



