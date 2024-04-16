from bank import*

user = PropertyBank("Mikki",18,2000,'8888')
user.money = 3000
user.key = '5555'
user.set_name('Vinni')
print(user.get_name(),user.money,user.key)