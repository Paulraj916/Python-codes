# 2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream","Paul Raj"]

food = [drinks,dinner,dessert]

for i in range(0,3,1):
    for j in range(0,3,1):
        print(food[i][j])