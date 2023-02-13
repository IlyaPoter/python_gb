from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()



# from isOdd import isOdd

# print(isOdd(0))
# print(isOdd(4))