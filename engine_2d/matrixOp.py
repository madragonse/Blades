import math

class Matrix_op:
    
    def determinant(self, m):
        if math.sqrt(len(m)*len(m[0])) - int(math.sqrt(len(m)*len(m[0]))) == 0:
            return self.__determinant(m)
        else:
            raise Exception("Imput must be a 2D square matrix array")

    def __determinant(self, m):
        if len(m) == 2:
            return self.__determinant_2(m)
        else:
            return self.__determinant_n(m)

    def __determinant_2(sefl, m):
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    def __determinant_n(self, m):


        ret = 0
        for i in range(0, len(m)):
            tem_mul = m[i][0]
            tem_mat = []
            for j in range(0, len(m)):
                if j == i: continue
                tem_mat.append(m[j][1:])

            if i%2==1:
                ret += tem_mul*self.__determinant(tem_mat)
            else:
                ret -= tem_mul*self.__determinant(tem_mat)
        return ret


    def multiply(self, m1, m2):
        ret = []
        len = m1.__len__()
        x_len = m2.__len__()
        y_len = m1[0].__len__()
        for x in range(0, x_len):
            ret.append([])
            for y in range(0, y_len):
                ret[x].append(0)
                for i in range(0, len):
                    ret[x][y] += m1[i][y] * m2[x][i]
        return ret
        
    def multiply_vector(self, m, v):
        ret = []
        len = m.__len__()
        y_len = m[0].__len__()
        for y in range(0, y_len):
            ret.append(0)
            for i in range(0, len):
                ret[y] += m[i][y] * v[i]
        return ret