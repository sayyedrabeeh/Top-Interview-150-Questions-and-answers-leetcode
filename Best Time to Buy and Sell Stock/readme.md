
 
##  Best Time to Buy and Sell Stock

###  Question

You are given an array `prices` where `prices[i]` is the price of a stock on the *i-th* day.

You want to maximize your profit by choosing:

* **one day to buy** the stock
* **a later day to sell** the stock

Return the **maximum profit** you can achieve.
If no profit is possible, return `0`.

---

###  Example 1:

```
Input: prices = [7,1,5,3,6,4]
Output: 5
```

**Explanation:**
Buy at price `1` (day 2) and sell at price `6` (day 5).
Profit = `6 - 1 = 5`

---

###  Example 2:

```
Input: prices = [7,6,4,3,1]
Output: 0
```

**Explanation:**
Prices keep decreasing, so no profit is possible.

---

##  Solution Explanation

We will scan the prices **once** and keep track of:

1. The **minimum price so far** (best day to buy)
2. The **maximum profit so far**

---

###  Full Code:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price

        return max_profit
```

---

##  Line-by-Line Explanation:

### `class Solution:`

* Defines a class named `Solution`.
* Required by platforms like LeetCode.

---

### `def maxProfit(self, prices: List[int]) -> int:`

* Defines a method called `maxProfit`.
* Parameters:

  * `self`: reference to the class instance.
  * `prices`: list of stock prices.
* `-> int` means the function returns an integer.

---

### `min_price = float('inf')`

* Initializes the **minimum price** to infinity.
* This ensures any real stock price will be smaller.
* Used to track the **best day to buy**.

---

### `max_profit = 0`

* Stores the **maximum profit** found so far.
* Starts at `0` because profit cannot be negative.

---

### `for i in prices:`

* Loops through each stock price day by day.

---

### `if i < min_price:`

* Checks if the current price is **lower** than any price seen before.

---

### `min_price = i`

* Updates the minimum price.
* This means: *“This is the best day to buy so far.”*

---

### `elif i - min_price > max_profit:`

* Calculates profit if we sell today.
* Compares it with the current maximum profit.

---

### `max_profit = i - min_price`

* Updates the maximum profit if a better one is found.

---

### `return max_profit`

* Returns the highest profit possible.
* If no profit exists, it returns `0`.

---

##  Example Walkthrough:

### Input:

```
prices = [7,1,5,3,6,4]
```

| Day | Price | Min Price | Profit | Max Profit |
| --- | ----- | --------- | ------ | ---------- |
| 1   | 7     | 7         | 0      | 0          |
| 2   | 1     | 1         | 0      | 0          |
| 3   | 5     | 1         | 4      | 4          |
| 4   | 3     | 1         | 2      | 4          |
| 5   | 6     | 1         | 5      | 5 ✅        |
| 6   | 4     | 1         | 3      | 5          |

---

## ⏱ Time & Space Complexity:

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |

* Only one pass through the array.
* No extra memory used.

---

##  Summary:

| Concept         | Explanation             |
| --------------- | ----------------------- |
| `min_price`     | Best day to buy         |
| `max_profit`    | Best profit so far      |
| Single loop     | Efficient solution      |
| Greedy approach | Always keep best choice |

---
 
