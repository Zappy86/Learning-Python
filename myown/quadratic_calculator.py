from math import sqrt

def quad_calculator(a, b, c):

    if(a == 0):
        return("Not a quadratic.")

    discriminant = (b*b) + (-4*a*c)

    if(discriminant < 0): return("No real roots.")
    elif(discriminant == 0): return[-b/(2*a)]
    elif(discriminant > 0): return[((-b + sqrt(discriminant))/(2*a)), ((-b - sqrt(discriminant))/(2*a))]
    else: return("Error")

if __name__ == "__main__":
    while True:    
        a = float(input("\nA: "))
        b = float(input("B: "))
        c = float(input("C: "))

        result = quad_calculator(a, b, c)
        
        if type(result) == list:
            print(f"x ∈ {result}")
        else:
            print(result)