#I/usr/bin/env python3
import time
import math
import infos
import lab_4_classes

def get_error(x_g, y_g, x, y, theta):
    ex = (x_g - x); ey = (y_g - y)

    rho = math.sqrt(ex ** 2 + ey ** 2)
    alpha = math.atan2(ey, ex) - theta

    return(rho, alpha)

def calc_control(rho, alpha):
    v_goal = Ks * rho
    w_goal = Kr * alpha
    return(v_goal, w_goal)

def saturation(u, u_max = 100):
    if u>=u_max:
        return u_max
    if u<=-u_max:
        return -u_max
    return u

if __name__ == "__main__":
    Kr = 1 #подбираем первым(угол поворота)
    Ks = 0 #подбираем вторым
    x_goal = 1; y_goal = 1

    rho, alpha = get_error(x_goal, y_goal, 0, 0, 0)
    print(rho, alpha)
    v_goal, w_goal = calc_control(rho, alpha)
    ur = saturation(v_goal + w_goal)
    ul = saturation(v_goal - w_goal)

    print(ur, ul)