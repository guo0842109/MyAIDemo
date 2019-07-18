import tensorflow as tf

# a = 2
# b = 3
# c = tf.add(a,b,name="Add")
#
# sess = tf.Session()
# print(sess.run(c))
# sess.close()

# 变量的定义
# var1 = tf.get_variable(name='var1',initializer=[[1,3],[4,7]],dtype=tf.int32)
# var2 = tf.get_variable(name='var2',initializer=[[2,5],[1,9]],dtype=tf.int32)
# var1_add_var2 = tf.add(var1,var2)
# #variable需要初始化
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)
# print(sess.run(var1_add_var2))

# 使用占位符placeholder
# var3 = tf.placeholder(name='var3',shape=[2,2],dtype=tf.int32)
# var4 = tf.placeholder(name='var4',shape=[2,2],dtype=tf.int32)
#
# var3_add_var4 = tf.add(var3,var4)
# with tf.Session() as sess:
#     print(sess.run(var3_add_var4,feed_dict={var3:[[4,6],[1,5]],var4 :[[5,3],[2,7]]}))