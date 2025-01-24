def elliptic_add(p_1, p_2, A):

    if p_1[0]==float('inf') and p_1[1]==float('inf'):
        return p_2

    if p_2[0]==float('inf') and p_1[1]==float('inf'):
        return p_1

    if p_1[0]==p_2[0] and p_1[1]==-p_2[1]:
        return [float('inf'),float('inf')]

    else:

        if p_1 != p_2:
            lbda = (p_2[1] - p_1[1]) / (p_2[0] - p_1[0])

        if p_1 == p_2:
            lbda = (3*p_1[0]**2 + A) / (2*p_1[1])

        x_3 = lbda**2 - p_1[0] - p_2[0]
        y_3 = lbda*(p_1[0] - x_3) - p_1[1]
        p_3 = [x_3, y_3]

        return p_3

    return None

p_1 = [3,4]
p_2 = [3,4]
A = -7
elliptic_add(p_1,p_2,A)