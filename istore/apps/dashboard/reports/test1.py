def counter(self,t = 0):
        t += 1
        print('тут бля next %d\n%t')
        yield

for i in range(5):
    counter()
