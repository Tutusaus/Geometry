import transformations as t

point = [1, 2, 3]
vector = np.array([30, 40])
vector = vector + [0, 0, 0]

print(t.translation(point, vector))