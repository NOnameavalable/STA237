"""Recompute W6 numerical answers with Python's standard library.

Run: python3 scripts/verify_week6.py
Probabilities are calculated by explicit finite sums of PMFs, not simulation.
"""
import json
import math


def pois(k, mean):
    return math.exp(-mean + k * math.log(mean) - math.lgamma(k + 1))


def pcdf(k, mean):
    return math.fsum(pois(i, mean) for i in range(k + 1))


def bino(k, n, p):
    return math.comb(n, k) * p**k * (1 - p)**(n - k)


def bcdf(k, n, p):
    return math.fsum(bino(i, n, p) for i in range(k + 1))


def total_nb(t, r, p):
    return math.comb(t - 1, r - 1) * p**r * (1 - p)**(t - r)


def hgeom(x, N, K, n):
    if not max(0, n - (N - K)) <= x <= min(n, K):
        return 0.0
    return math.comb(K, x) * math.comb(N - K, n - x) / math.comb(N, n)


def close(a, b, tol=2e-11):
    assert abs(a - b) < tol, (a, b)


def main():
    q = {}
    q['MMSA91'] = [pcdf(10, 20), 1 - pcdf(20, 20),
                   math.fsum(pois(i, 20) for i in range(10, 21)),
                   math.fsum(pois(i, 20) for i in range(11, 20)),
                   math.fsum(pois(i, 20) for i in range(12, 29))]
    q['MMSA93'] = [bino(3, 200, .017), pois(3, 3.4),
                   bcdf(3, 200, .017), pcdf(3, 3.4)]
    q['MMSA94'] = [10, math.sqrt(9.99), 1 - pcdf(10, 10), pois(0, 10)]
    q['MMSA101'] = [4, 1 - pcdf(5, 4), math.log(10) / 2]
    q['MMSA114'] = [3, 2.1 * 490 / 499, 3, 2.1]
    q['MMSA118'] = [60, math.sqrt(600)]
    lo = math.ceil(160 - math.sqrt(480))
    hi = math.floor(160 + math.sqrt(480))
    q['MMSA121'] = [160, math.sqrt(480), lo, hi,
                    math.fsum(total_nb(t, 40, .25) for t in range(lo, hi + 1))]
    q['PAR3.23'] = [4, pois(3, 4)]
    q['PAR3.25'] = [math.log(10), 1 - .1 * (1 + math.log(10))]
    q['PAR3.26'] = [math.fsum(pois(i, 4.375) for i in range(3, 7))]
    q['PAR3.27'] = [1 - pcdf(999, 960)]
    observed = [18, 30, 21, 21, 6, 3, 3, 2]
    mean = sum(i * f for i, f in enumerate(observed)) / sum(observed)
    expected = [104 * pois(i, mean) for i in range(8)]
    q['PAR3.28'] = {'mean': mean, 'expected0to7': expected,
                    'expected8plus': 104 * (1 - pcdf(7, mean))}
    q['PAR3.30'] = [64 * math.exp(-3) / (1 + 64 * math.exp(-3))]
    q['PAR3.31'] = [math.fsum(bino(i, 10000, 1 / 6000) for i in range(1, 4)),
                    math.fsum(pois(i, 10000 / 6000) for i in range(1, 4))]
    q['PAR3.32'] = [bino(2, 100, 1 / 64), pois(2, 100 / 64)]
    q['PAR5.2'] = [5 / 11]
    q['PAR5.4'] = [.3 * .7**2, .7 - .7**8, .7**3]
    q['PAR5.5'] = [.85**4 * .15, 1 - .85**5, 1 / .15]
    q['PAR5.7'] = [math.ceil(math.log(.05) / math.log(.75)),
                   1 - .75**10, 1 - .75**11]
    q['PAR5.20'] = [total_nb(6, 3, .4),
                    math.fsum(total_nb(t, 3, .4) for t in range(5, 11)),
                    1 - math.fsum(total_nb(t, 3, .4) for t in range(3, 8))]
    q['PAR5.21'] = [total_nb(10, 4, .5), bcdf(3, 9, .5)]
    q['PAR5.25'] = [math.fsum(total_nb(t, 10, .072) for t in range(10, 101))]
    q['PAR5.34'] = [hgeom(3, 23, 8, 6),
                    math.fsum(hgeom(i, 23, 8, 6) for i in range(3)), 48 / 23]
    q['slide_phone'] = [bino(2, 10, .08), bcdf(2, 10, .08), 1 - bcdf(2, 10, .08)]
    q['slide_labubu'] = [.95**9 * .05, bino(2, 10, .05),
                         total_nb(11, 3, .05), total_nb(15, 5, .05)]
    q['slide_warehouse'] = [math.fsum(hgeom(i, 50, 5, 10) for i in range(3, 6)),
                            1 - math.fsum(hgeom(i, 5000, 500, 10) for i in range(3)),
                            1 - bcdf(2, 10, .1)]
    q['slide_forest'] = [1 - math.exp(-6), pois(10, 18)]

    # Independent identities and boundary checks, including the large-mean tail.
    close(pcdf(100, 20), 1)
    close(math.fsum(hgeom(i, 23, 8, 6) for i in range(7)), 1)
    close(math.fsum(hgeom(i, 50, 15, 10) for i in range(11)), 1)
    close(math.fsum(total_nb(t, 4, .5) for t in range(10, 120)), bcdf(3, 9, .5))
    close(q['PAR5.25'][0], 1 - bcdf(9, 100, .072))
    close(q['PAR3.27'][0], math.fsum(pois(i, 960) for i in range(1000, 1600)))
    close(q['MMSA121'][-1],
          (1 - bcdf(39, 181, .25)) - (1 - bcdf(39, 138, .25)))
    close(math.fsum(expected) + q['PAR3.28']['expected8plus'], 104)
    close(math.exp(-2 * q['MMSA101'][-1]), .1)
    assert 1 - .3**4 < .995 <= 1 - .3**5
    assert 1 - .75**10 < .95 <= 1 - .75**11
    for r, b in [(1, 5), (3, 4), (7, 2)]:
        close(math.fsum(math.comb(r + b - k, r - 1) / math.comb(r + b, r)
                        for k in range(1, b + 2)), 1)
    print(json.dumps(q, indent=2))
    print('PASS: normalization, alternative sums, NB/binomial event equivalence, '
          'integer thresholds, inverse-time substitution, and first-red PMF.')


if __name__ == '__main__':
    main()
