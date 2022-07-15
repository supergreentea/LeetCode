class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.cur_product = 1
        

    def add(self, num: int) -> None:
        if num == 0:
            self.products = []
            self.cur_product = 1
        else:
            self.cur_product *= num
            self.products.append(self.cur_product)

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        elif len(self.products) == k:
            return self.products[-1]
        else:
            return (self.products[-1] // self.products[-1-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)