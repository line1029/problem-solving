class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prefix_product = [1]
        self.last_zero_idx = None

    def add(self, num: int) -> None:
        self.arr.append(num)
        num_product = self.prefix_product[-1]
        if num:
            num_product *= num
        else:
            self.last_zero_idx = len(self.arr) - 1
        self.prefix_product.append(num_product)

    def getProduct(self, k: int) -> int:
        if self.last_zero_idx is not None and len(self.arr) - self.last_zero_idx <= k:
            return 0
        return self.prefix_product[-1] // self.prefix_product[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)