'''
https://www.investopedia.com/terms/p/price-earningsratio.asp

ratio for valuing a company that measures its current share price relative to its per-share earnings



A high P/E ratio could mean that a company's stock is over-valued,
 or else that investors are expecting high growth rates in the future.

Companies that have no earnings or that are losing money do not have a P/E ratio
 since there is nothing to put in the denominator.

Two kinds of P/E ratios - forward and trailing P/E - are used in practice.



'''



def peRatio(MVPS, EPS):
    # Market Value Per Share
    # Earnings Per Share
    return MVPS / EPS

def peRatioPerShare(MV, EP, S):
    return (MV/EP)/S

'''
Forward P/E Formula
FPE = (Current Share Price) / (Estimated Future Earnings per Share)
'''
def forwardPE(sharePrice, eps, percentGrowth = 0):
    return sharePrice / (eps * (1+(percentGrowth/100)))



