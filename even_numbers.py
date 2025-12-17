# Iterators
# class EvenNumbers:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.limit:
#             raise StopIteration
        
#         value = self.current
#         self.current +=2
#         return value


# if __name__ == '__main__':
#     even_num = EvenNumbers(100)
#     for item in even_num:
#         print(item)

# Generators
def even_numbers(limit):
    current = 0
    while current <= limit:
        yield current
        current += 2

for num in even_numbers(10):
    print(num)