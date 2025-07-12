import random
example = random.randint(-10, 10)
print(f"Positive: {example}" if example
      > 0 else f"Negative: {example}")
