class LazyLoad:
  def __init__(self, price):
    self.price = price

  def __getattr__(self, name):
    if name == "taxed_price":
      value = self.price * 0.2
    elif name == "discounted_price":
      value = self.price * 0.1
    else:
      raise AttributeErrro(f"attribute {name} not found")
    settattr(self, name, value) 
    return value 

obj = Lazyload(1000)
print(obj.taxed_price)
print(obj.discounted_price)
