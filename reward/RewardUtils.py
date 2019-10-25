from scipy import exp


def gauss(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))








