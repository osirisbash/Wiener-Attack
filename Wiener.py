import ContinueFractions
import Arithmetic

def Wiener(N : int, e : int) -> int :
    """
    Wiener Attack
    return the private key if it's vulnerable
    if not, return 0
    """
    
    #1 - initialize the list of partial quotients
    quot = ContinueFractions.cont_frac(e,N)
    print(quot)
    
    #2 - initialize a list of continued fractions
    seq = ContinueFractions.frac_seq(quot)
    print(seq)

    #check if d is actually the key
    for (k,d) in seq :
        # Now we are going to check if the couple (k,d)
        # produce a factorization of N (p * q)
        
        if k == 0:
            continue

        # compute phi
        # phi(N) = (ed - 1)/ k
        phi = (e * d - 1) // k
        
        # Now from phi and N we can deduce the eventual factorization
        # by solving the equation : x^2 - ((N-phi)+1)x + N
        a = 1
        b = (N - phi) + 1
        c = N
        
        discr = b*b - 4 * a * c
    
        # in that case we got solutions to the equation
        if discr > 0 :
            # to works, the solutions must be integers
            # first, the root of the discriminent must be integer 
            rdiscr = Arithmetic.isqrt(discr)

            if (rdiscr * rdiscr) == discr :
                #the root of the discr is integer, we compute the solutions 
                p = -((-b - rdiscr) // (2 * a))
                q = -((-b + rdiscr) // (2 * a))
                if N == (p * q) :
                    print("Hacked")
                    return d

    print("Not vulnerable to Wiener")

    return 0

def test_hack_RSA():
    print("Testing Wiener Attack")
  
    

     #e = 169172609599399770878176257733611916126128765749132346531846851005776093458749535512804948886273960466150476674064259633854202370228998466878486947234189437667232890685114026187243859048003844668420320863295053511263366227207196358914657236229589630078484440029902442203289247092373494598228501976778089147663
    #N = 390927538156049465086293303582122466689929778415279771145146291314589164937280925171422429866065731668229942262382651166995761749347253605777451425021477521754022694013452252160439760745381191508154497289780008935195582184530471235782730890218697336090157672003227966800579552362512037459784039505363181815377
    e = 17993
    N = 90581
    print("(e,n) is (", e, ", ", N, ")")

    
    hacked_d = Wiener(N, e)
    

        
    print("hacked_d = ", hacked_d)
    print("-------------------------")
       
    
if __name__ == "__main__":
    test_hack_RSA()
