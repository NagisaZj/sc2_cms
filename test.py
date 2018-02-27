import tensorflow as tf
a = tf.constant([-1, -2])
sess = tf.Session()
b = tf.one_hot(a,depth = 3, axis=1)
m = sess.run(b)
print(m)
print(-1%64)
print(-1//64)

