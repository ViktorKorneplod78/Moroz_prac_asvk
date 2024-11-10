from math import acos, pi
class Triangle:
    def __init__(self, a, b, c):
        self.a_x, self.a_y, self.b_x, self.b_y, self.c_x, self.c_y = a[0], a[1], b[0], b[1], c[0], c[1]

    def dist(self, a_x, a_y, b_x, b_y):
        return ((a_x - b_x)**2 + (a_y - b_y)**2)**0.5

    def __abs__(self):
        ab = self.dist(self.a_x, self.a_y, self.b_x, self.b_y)
        ac = self.dist(self.a_x, self.a_y, self.c_x, self.c_y)
        bc = self.dist(self.c_x, self.c_y, self.b_x, self.b_y)
        p = (ab + ac + bc) / 2
        S = (p * (p - ab) * (p - ac) * (p - bc))  ** 0.5
        return S if S > 0 else 0

    def __bool__(self):
        return self.__abs__() != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def angle(self, a_x, a_y, o_x, o_y, b_x, b_y):
        t = (a_x - o_x)*(b_y - o_y) - (a_y - o_y)*(b_x - o_x)
        sign = 1 if t > 0 else 0 if t == 0 else -1
        ao, ob, ab = self.dist(a_x, a_y, o_x, o_y), self.dist(o_x, o_y, b_x, b_y), self.dist(a_x, a_y, b_x, b_y)
        return 2*pi if ao * ob == 0 else sign * acos((ao**2 + ob**2 - ab**2) / (2 * ao * ob))

    def o_inside(self, o_x, o_y):
        s = self.angle(self.a_x, self.a_y, o_x, o_y, self.b_x, self.b_y)
        s += self.angle(self.b_x, self.b_y, o_x, o_y, self.c_x, self.c_y)
        s += self.angle(self.c_x, self.c_y, o_x, o_y, self.a_x, self.a_y)
        return abs(s) > 1

    def __contains__(self, other):
        if self == other or (not other):
            return True
        return self.o_inside(other.a_x, other.a_y) and self.o_inside(other.b_x, other.b_y) and self.o_inside(other.c_x, other.c_y)

    def check_semisurface(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        return self.angle(c_x, c_y, a_x, a_y, d_x, d_y) * self.angle(c_x, c_y, b_x, b_y, d_x, d_y) >= 0

    def check_blin(self, other):
        check_bc_a = self.check_semisurface(self.a_x, self.a_y, other.a_x, other.a_y, self.b_x, self.b_y, self.c_x, self.c_y)
        check_bc_b = self.check_semisurface(self.a_x, self.a_y, other.b_x, other.b_y, self.b_x, self.b_y, self.c_x, self.c_y)
        check_bc_c = self.check_semisurface(self.a_x, self.a_y, other.c_x, other.c_y, self.b_x, self.b_y, self.c_x, self.c_y)
        bc_divides = not (check_bc_a or check_bc_b or check_bc_c)

        check_ac_a = self.check_semisurface(self.b_x, self.b_y, other.a_x, other.a_y, self.a_x, self.a_y, self.c_x, self.c_y)
        check_ac_b = self.check_semisurface(self.b_x, self.b_y, other.b_x, other.b_y, self.a_x, self.a_y, self.c_x, self.c_y)
        check_ac_c = self.check_semisurface(self.b_x, self.b_y, other.c_x, other.c_y, self.a_x, self.a_y, self.c_x, self.c_y)
        ac_divides = not (check_ac_a or check_ac_b or check_ac_c)

        check_ab_a = self.check_semisurface(self.c_x, self.c_y, other.a_x, other.a_y, self.b_x, self.b_y, self.a_x, self.a_y)
        check_ab_b = self.check_semisurface(self.c_x, self.c_y, other.b_x, other.b_y, self.b_x, self.b_y, self.a_x, self.a_y)
        check_ab_c = self.check_semisurface(self.c_x, self.c_y, other.c_x, other.c_y, self.b_x, self.b_y, self.a_x, self.a_y)
        ab_divides = not (check_ab_a or check_ab_b or check_ab_c)

        return ab_divides or bc_divides or ac_divides

    def __and__(self, other):
        if (not self) or (not other):
            return False
        return not(self.check_blin(other) or other.check_blin(self))
import sys
exec(sys.stdin.read())
