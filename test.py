vectors = {'I': [[0, 1], [0, 2], [0, 3]],
            'T': [[-1, 1], [0, 1], [1, 1]],
            'O': [[-1, 0], [-1, 1], [0, 1]],
            'Z': [[-1, 0], [0, 1], [1, 1]],
            'S': [[1, 0], [0, 1], [-1, 1]],
            'L': [[0, 1], [0, 2], [1, 2]],
            'J': [[0, 1], [0, 2], [-1, 2]]}

point = [0, 5]

def i_fig():
    i_vect = vectors['I']
    return [point,
                [point[0] + i_vect[0][0], point[1] + i_vect[0][1]],
                [point[0] + i_vect[1][0], point[1] + i_vect[1][1]],
                [point[0] + i_vect[2][0], point[1] + i_vect[2][1]]]

def t_fig():
    t_vect = vectors['T']
    return [point,
                [point[0] + t_vect[0][0], point[1] + t_vect[0][1]],
                [point[0] + t_vect[1][0], point[1] + t_vect[1][1]],
                 [point[0] + t_vect[2][0], point[1] + t_vect[2][1]]]

def o_fig():
    o_vect = vectors['O']
    return [point,
               [point[0] + o_vect[0][0], point[1] + o_vect[0][1]],
               [point[0] + o_vect[1][0], point[1] + o_vect[1][1]],
               [point[0] + o_vect[2][0], point[1] + o_vect[2][1]]]

def z_fig():
    z_vect = vectors['Z']
    return [point,
               [point[0] + z_vect[0][0], point[1] + z_vect[0][1]],
               [point[0] + z_vect[1][0], point[1] + z_vect[1][1]],
               [point[0] + z_vect[2][0], point[1] + z_vect[2][1]]]

def s_fig():
    s_vect = vectors['S']
    return [point,
                [point[0] + s_vect[0][0], point[1] + s_vect[0][1]],
                [point[0] + s_vect[1][0], point[1] + s_vect[1][1]],
                [point[0] + s_vect[2][0], point[1] + s_vect[2][1]]]

def l_fig():
    l_vect = vectors['L']
    return [point,
               [point[0] + l_vect[0][0], point[1] + l_vect[0][1]],
               [point[0] + l_vect[1][0], point[1] + l_vect[1][1]],
               [point[0] + l_vect[2][0], point[1] + l_vect[2][1]]]

def j_fig():
    j_vect = vectors['J']
    return [point,
                 [point[0] + j_vect[0][0], point[1] + j_vect[0][1]],
                 [point[0] + j_vect[1][0], point[1] + j_vect[1][1]],
                 [point[0] + j_vect[2][0], point[1] + j_vect[2][1]]]

fig_choice = {'1': i_fig(),
              '2': t_fig(),
              '3': o_fig(),
              '4': z_fig(),
              '5': s_fig(),
              '6': l_fig(),
              '7': j_fig()}

a = [1, 4, 7]
print(sum(a))

