import random



def generate_color(n):

    """
    Function to generate colors for tickers. n - number of colors.
    """
    
    for _ in range(n):
        
        r = lambda: random.randint(0,255)
        
        print('"#%02X%02X%02X",' % (r(),r(),r()))



COLORS = [
"#BDEA75",
"#F8816B",
"#93D45E",
"#AB46BF",
"#9B890A",
"#C015D5",
"#BCF9A4",
"#9EEA30",
"#617057",
"#B25F1F",
]

