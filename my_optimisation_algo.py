
from sympy import symbols, diff
import time
x, y = symbols('x y', real=True)
def my_optimisation_algo(function_to_minimise, initialise = (0,0), learning_rate=0.1, time_out_seconds=120, error=0.01):
    """
    LOGIC:
    Its a modified version of gradient descent.
    Idea is using simple learning_rate as a step as long as function is getting minimised. Pain arise when
    point reaches increasing side of the curve, i.e, function start to increase -> Now use gradient descent 
    to find optimal values
    
    NEED:
    plane surface -> gradient descent fails -> takes very small steps
    """
    #a corresponds to value of x and same for b and y
    a_final = None
    b_final = None
    t1 = time.time()
    
    #this is partial differential of 'f' w.r.t 'x'
    dl_dx = diff(function_to_minimise,x)
    dl_dy = diff(function_to_minimise,y)
    a,b = initialise
    while True:
        t2 = time.time()
        if t2-t1>time_out_seconds:
            return "time out from first loop"
        f1 = function_to_minimise.subs({x:a,y:b})
        a = a - learning_rate
        b = b - learning_rate
        f2 = function_to_minimise.subs({x:a,y:b})
        
        if abs(f2-f1)<=error:
            return (a,b)
        
        #this condition is first part of the logic
        if f2<=f1:
            continue
        #this condition is second part of the logic
        else:
            while True:
                t3 = time.time()
                if t3-t1>time_out_seconds:
                    return "time out from second loop"
#                 f3 = function_to_minimise.subs({x:a,y:b})
                
                #idea is stop iteration on 'a' if whilee got 'a_final' value
                if abs(learning_rate*dl_dx.subs({x:a,y:b}))<=error:
                    a_final = a
                if a_final is None:
                    a = a - learning_rate*dl_dx.subs({x:a,y:b})
                    
                #idea is stop iteration on 'b' if whilee got 'b_final' value
                if abs(learning_rate*dl_dy.subs({x:a,y:b}))<=error:
                    b_final = b
                if b_final is None:
                    b = b - learning_rate*dl_dy.subs({x:a,y:b})
                
                if (a_final is not None) and (b_final is not None):
                    return (a_final,b_final)
                
#                 f4 = function_to_minimise.subs({x:a,y:b})
#                 if abs(f3-f4)<=error:
#                     return (a,b)

            
    

my_optimisation_algo((x-1)**2 + (y-10)**2,error=0.01, learning_rate=0.01)