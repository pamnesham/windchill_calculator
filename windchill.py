#!python3

def main():
    print("What is the ambient temperature?")
    ambTemp = float(input())
    print("What is the wind velocity")
    windVel = float(input())
    print(wind_chill(ambTemp, windVel))

def wind_chill(ambTemp, windVel):
    chill = 35.74 + (0.6215*ambTemp) - (35.75*windVel**.16) + (.4275*ambTemp*windVel**.16)
    return(chill)


if  __name__ == '__main__':
    main()
