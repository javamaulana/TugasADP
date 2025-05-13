print("""
f(x) = 4x³ + 7x - 5, x ≥ 0
f(x) = 3x² - 5x + 1, x < 0
g(x) = (f(x))² - f(x)
h(x) = f(x) × g(x)
""")

x_list = []
f_list = []
g_list = []
h_list = []
ulang = 'Y'
while ulang.upper() == 'Y':
    n = int(input("Input banyak data n: "))
    
    for i in range(n):
        x = float(input(f"Input x ke {i+1}: "))
        x_list.append(x)
        
        if x >= 0:
            f = 4 * x**3 + 7 * x - 5
        else:
            f = 3 * x**2 - 5 * x + 1
        f_list.append(f)
       
        g = (f**2) - f
        g_list.append(g)
        
        h = f * g
        h_list.append(h)

    print("\nOutput:")
    print("-" * 60)
    print(f"{'No':<3}| {'x':<11}| {'f(x)':<15}| {'g(x)':<15}| {'h(x)':<15}")
    print("-" * 60)
    for i in range(len(x_list)):
         print(f"{i+1:<3}| {x_list[i]:<11,.2f}| {f_list[i]:<15,.2f}| {g_list[i]:<15,.2f}| {h_list[i]:<15,.2f}")
   
    ulang = input("\nInput nilai x lagi Y/N?: ")
