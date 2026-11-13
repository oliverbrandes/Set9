# Gamma-law equation of state:  P = (Gamma - 1) rho e


class Gamma_Law:

    def __init__(self, gamma):
        self.gamma = gamma

    def P(self, rho, e):
        P = (self.gamma - 1) * e * rho
        return P

    def e_from_P(self, rho, P):
        e = P / ((self.gamma - 1) * rho)
        return e

    def sound_speed(self, rho, e):
        # c_s^2 = Gamma P / rho   (adiabatic sound speed, 9.1b)
        c_s = (self.gamma * self.P(rho, e) / rho)**(1 / 2)
        return c_s
