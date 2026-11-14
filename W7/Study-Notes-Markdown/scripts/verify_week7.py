"""Verify source-based Week 7 calculations, independently of Markdown layout.

Requires SymPy and SciPy. The local course environment can run this with:
/Users/stevenli/opt/anaconda3/bin/python scripts/verify_week7.py
"""
import math
from fractions import Fraction
import sympy as s
from scipy.integrate import quad
from scipy.stats import poisson, binom, hypergeom

x=s.symbols('x', real=True)
p=s.symbols('p', positive=True)
checks=0

def exact(actual,expected,label):
    global checks
    assert s.simplify(actual-expected)==0,(label,actual,expected)
    checks+=1

def near(actual,expected,label,tol=2e-10):
    global checks
    assert math.isclose(float(actual),float(expected),abs_tol=tol,rel_tol=tol),(label,actual,expected)
    checks+=1

def integral(f,a,b):
    return s.integrate(f,(x,a,b))

def moments(parts):
    return [sum(integral(x**r*f,a,b) for f,a,b in parts) for r in range(3)]

def meanvar(parts,label,mean,var):
    m=moments(parts)
    exact(m[0],1,label+' norm');exact(m[1],mean,label+' mean');exact(m[2]-m[1]**2,var,label+' variance')
    return m

# Lecture counts, event translations, and independent PMF sums.
def pois(k,lam):return math.exp(-lam+k*math.log(lam)-math.lgamma(k+1))
near(sum(pois(k,20) for k in range(18,21)),poisson.cdf(20,20)-poisson.cdf(17,20),'mechanic a')
near(sum(pois(k,3) for k in range(2,80)),1-4*math.exp(-3),'monarch')
near(binom.sf(0,5,.1),.40951,'scratch cards')
near(hypergeom.pmf(1,10,3,3),.525,'books without replacement')
near(binom.pmf(1,3,.3),.441,'books with replacement alternative')
assert [85*r*r-600 for r in [18,19,20]]==[26940,30085,33400];checks+=1
assert 85*(16**2+16)-480==22640;checks+=1
for lo,hi,result in [(12,28,.9442796565187097),(11,29,.9673700636477899),(15,25,.7829507461740454)]:
    near(sum(pois(k,20) for k in range(lo,hi+1)),result,'repair interval '+str((lo,hi)))
    near(poisson.cdf(hi,20)-poisson.cdf(lo-1,20),result,'repair CDF interval')
assert (poisson.ppf(.125,20),poisson.ppf(.875,20))==(15,25);checks+=1
# Competing-stop PMF must normalize, unlike a single unbounded NB model.
for chance in [0,.1,.25,.5,.9,1]:
    q=1-chance
    masses=[math.comb(n-1,3)*(chance**4*q**(n-4)+q**4*chance**(n-4)) for n in range(4,8)]
    near(sum(masses),1,'series total p='+str(chance))
    near(masses[1],4*chance**4*q+4*q**4*chance,'series five games')
for lam in [1,3,16,20]:
    near(sum(k*pois(k,lam) for k in range(0,200)),lam,'Poisson mean')
    near(sum(k*(k-1)*pois(k,lam) for k in range(0,200)),lam**2,'Poisson factorial moment')
for prob in [.1,.3,.7]:
    near(sum(k*prob*(1-prob)**k for k in range(1000)),(1-prob)/prob,'geometric failures mean')
# Source polynomial density and the distinct piecewise-CDF example.
lecture=3*(x-1)**2
meanvar([(lecture,0,1)],'lecture Y',s.Rational(1,4),s.Rational(3,80))
exact(integral(lecture,0,s.Rational(1,4)),s.Rational(37,64),'slide 17 left')
exact(integral(lecture,s.Rational(3,4),1),s.Rational(1,64),'slide 17 right')
exact(integral(lecture,s.Rational(1,10),s.Rational(2,5)),s.Rational(513,1000),'slide 19 interval')
exact((s.Rational(3,2)/2)-(s.Rational(1,2)**3/2),s.Rational(11,16),'slide20 interval')
exact(integral(3*x*x/2,0,1)+integral(s.Rational(1,2),1,2),1,'slide20 density norm')
exact((s.Rational(1,2)**s.Rational(1,3))**3,s.Rational(1,2),'median slide22')
meanvar([(x,0,1),(2-x,1,2)],'gas pump',1,s.Rational(1,6))
near(10000/math.sqrt(6),4082.48290463863,'gas SD in gallons')
# MMSA 3, 4, 5, 6, 7.
error=s.Rational(3,32)*(4-x*x)
exact(integral(error,-2,2),1,'M3 norm')
exact(integral(error,0,2),s.Rational(1,2),'M3b')
exact(integral(error,-1,1),s.Rational(11,16),'M3c')
exact(1-integral(error,-s.Rational(1,2),s.Rational(1,2)),s.Rational(81,128),'M3d')
rayleigh=x/s.Integer(10000)*s.exp(-x*x/20000)
exact(integral(rayleigh,0,s.oo),1,'M4 norm')
exact(integral(rayleigh,0,200),1-s.exp(-2),'M4b')
exact(integral(rayleigh,100,200),s.exp(-s.Rational(1,2))-s.exp(-2),'M4c')
overtime=s.Rational(3,8)*x*x
exact(integral(overtime,0,2),1,'M5 norm')
exact(integral(overtime,0,1),s.Rational(1,8),'M5b')
exact(integral(overtime,1,s.Rational(3,2)),s.Rational(19,64),'M5c')
exact(integral(overtime,s.Rational(3,2),2),s.Rational(37,64),'M5d')
gpa=s.Rational(3,4)*(1-(x-3)**2)
meanvar([(gpa,2,4)],'M6/M22 GPA',3,s.Rational(1,5))
exact(integral(gpa,s.Rational(11,4),s.Rational(13,4)),s.Rational(47,128),'M6d')
exact(1-integral(gpa,s.Rational(5,2),s.Rational(7,2)),s.Rational(5,16),'M6e')
exact(integral(s.Rational(1,10),33,35),s.Rational(1,5),'M7b')
exact(integral(s.Rational(1,10),28,32),s.Rational(2,5),'M7c')
# MMSA 8/24 total-wait model.
bus=[(x/25,0,5),((10-x)/25,5,10)]
meanvar(bus,'M8/M24 bus',5,s.Rational(25,6))
exact(integral(x/25,0,3),s.Rational(9,50),'M8c')
exact(1-integral((10-x)/25,8,10),s.Rational(23,25),'M8d')
exact(integral(x/25,3,5)+integral((10-x)/25,5,8),s.Rational(37,50),'M8e')
exact(integral(x/25,0,2)+integral((10-x)/25,6,10),s.Rational(2,5),'M8f')
exact(s.sqrt(50*p)**2/50,p,'M24 lower quantile')
exact(1-(10-(10-s.sqrt(50*(1-p))))**2/50,p,'M24 upper quantile')
# Referenced flood PDF, normalization, and requested events.
flood=s.Rational(1,25)*s.exp(-(x-10)/25)
exact(integral(flood,10,s.oo),1,'M9 norm')
exact(integral(flood,10,40),1-s.exp(-s.Rational(6,5)),'M9a')
exact(integral(flood,40,60),s.exp(-s.Rational(6,5))-s.exp(-2),'M9c')
# Pareto formulas: differentiation of antiderivatives and the quantile identity.
k,theta,b=s.symbols('k theta b',positive=True)
t=s.symbols('t',positive=True)
exact(s.diff(-(theta/t)**k,t),k*theta**k/t**(k+1),'M10 integral')
# Logarithm/exponent manipulation on positive parameters.
near(1-(2/(2/(1-.7)**(1/3)))**3,.7,'M10 percentile substitution')
# MMSA 11,12,13,18.
checkout=x/2
meanvar([(checkout,0,2)],'M18 checkout',s.Rational(4,3),s.Rational(2,9))
exact(integral(x*x*checkout,0,2),2,'M18 charge')
exact(integral(checkout,s.Rational(1,2),1),s.Rational(3,16),'M11b')
exact(integral(checkout,s.Rational(1,2),2),s.Rational(15,16),'M11c')
exact(s.sqrt(2)**2/4,s.Rational(1,2),'M11 median')
exact(integral(error,s.Rational(1,2),2),s.Rational(81,256),'M12c')
exact(integral(3*x**-4,1,s.oo),1,'M13 norm')
exact(integral(3*x**-4,2,3),s.Rational(19,216),'M13c')
# MMSA 20 uniform mFRI with support-truncated SD intervals.
lo,hi=s.Rational(11,20),s.Rational(29,20)
meanvar([(s.Rational(10,9),lo,hi)],'M20 mFRI',1,s.Rational(27,400))
near(2*math.sqrt(.0675)/.9,1/math.sqrt(3),'M20 oneSD')
assert 1-2*math.sqrt(.0675)<float(lo) and 1+2*math.sqrt(.0675)>float(hi);checks+=1
# MMSA 25 expected area: average the square, not square the average.
radius=s.Rational(3,4)*(1-(10-x)**2)
exact(integral(s.pi*x*x*radius,9,11),s.Rational(501,5)*s.pi,'M25 area')
# MMSA 26 includes a new clipped leftover function.
propane=2*(1-x**-2);mean=3-2*s.log(2)
meanvar([(propane,1,2)],'M26 propane',mean,s.Rational(8,3)-mean**2)
exact(integral((s.Rational(3,2)-x)*propane,1,s.Rational(3,2)),2*s.log(s.Rational(3,2))-s.Rational(3,4),'M26 leftover')
for probability in [.1,.5,.9]:
    quantile=(4+probability+math.sqrt((4+probability)**2-16))/4
    near(2*quantile+2/quantile-4,probability,'M26 quantile')
# PAR 6.1 only a–c; 6.2; 6.4–6.7.
exact(integral(2*x,0,1),1,'P601 norm');exact(integral(2*x,0,s.Rational(1,2)),s.Rational(1,4),'P601b');exact(integral(2*x*x,0,1),s.Rational(2,3),'P601c')
exact(integral(x*s.exp(-x/2)/4,0,s.oo),1,'P602 norm');exact(integral(x*x*s.exp(-x/2)/4,0,s.oo),4,'P602 mean')
near(math.exp(-.03*12**1.2),.553357695849,'P604 survival')
positive=s.symbols('positive',positive=True)
exact(s.diff(1-s.exp(-s.Rational(3,100)*positive**s.Rational(6,5)),positive),s.Rational(36,1000)*positive**s.Rational(1,5)*s.exp(-s.Rational(3,100)*positive**s.Rational(6,5)),'P604 derivative')
c=1/(s.exp(2)-s.exp(-2))
exact(integral(c*s.exp(x),-2,2),1,'P605 norm');exact(integral(x*c*s.exp(x),-2,2),(s.exp(2)+3*s.exp(-2))/(s.exp(2)-s.exp(-2)),'P605 mean')
meanvar([(4*x**-5,1,s.oo)],'P606',s.Rational(4,3),s.Rational(2,9))
exact(integral(4*x**-5,2,3),s.Rational(65,1296),'P606c')
exact(integral(s.cos(x),0,s.pi/2),1,'P607 norm');exact(integral(x*s.cos(x),0,s.pi/2),s.pi/2-1,'P607 mean')
# Distinct fixed-density qualification in PAR 6.13.
assert 2+(-1)==1 and 2*1+(-1)*1==1;checks+=1
# Numerical quadrature, separate from symbolic antiderivatives.
near(quad(lambda t:(1.5-t)*2*(1-1/t**2),1,1.5)[0],float(2*s.log(s.Rational(3,2))-s.Rational(3,4)),'quad leftover')
near(quad(lambda t:math.pi*t*t*.75*(1-(10-t)**2),9,11)[0],float(s.Rational(501,5)*s.pi),'quad area')
print(f'PASS: {checks} symbolic/numerical checks, including source models, support-aware intervals, moments, quantiles, and unit conversions.')
