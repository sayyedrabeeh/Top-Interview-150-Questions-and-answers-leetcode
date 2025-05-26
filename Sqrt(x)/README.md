## Sqrt(x)

### Question 

     Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned      integer should be non-negative as well.
     
     You must not use any built-in exponent function or operator.
     
     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

#### Example 1:

    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.
#### Example 2:

    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
 ### solution explanation 

 Let's break down this Python code **line by line**, and walk through **an example**, like `x = 8`.

---

### ✅ Full Code:

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i*i > x:
                return i - 1
        return x
```

---

### 🧠 What it's doing:

This function computes the **integer part** of the square root of `x` — essentially, `floor(sqrt(x))`.

So, for example:

* `sqrt(8)` ≈ 2.828... → return **2**
* `sqrt(16)` = 4 → return **4**
* `sqrt(1)` = 1 → return **1**

---

### 🔍 Line-by-line Explanation:

#### `class Solution:`

Defines a class named `Solution`. It's common in LeetCode-style problems.

#### `def mySqrt(self, x: int) -> int:`

This defines a method `mySqrt` that:

* Takes an integer `x`
* Returns an integer
* `self` refers to the instance of the class

---

### 👇 Loop:

#### `for i in range(x + 1):`

* This loops from `i = 0` to `i = x` (inclusive of `x`, because `range(x+1)` goes up to x).

#### `if i * i > x:`

* For each number `i`, this checks if `i²` is **greater** than `x`.

#### `return i - 1`

* If `i² > x`, the integer square root is `i - 1`, so it returns that.

#### `return x`

* This line is only reached if `x = 0` or `x = 1`, where `i*i > x` never becomes true during the loop.
* Example: if `x = 0`, then loop only does `i = 0`, `0*0 = 0`, never greater than `x`, so it returns `x`.

---

### 🔁 Example Walkthrough: `x = 8`

Let's go through the loop:

| i | i \* i | i \* i > 8? | Action                 |
| - | ------ | ----------- | ---------------------- |
| 0 | 0      | No          | Continue               |
| 1 | 1      | No          | Continue               |
| 2 | 4      | No          | Continue               |
| 3 | 9      | **Yes**     | Return `3 - 1` → **2** |

🔚 Loop ends early because we found the first `i` such that `i*i > x`.

---

### 🔁 Another Example: `x = 16`

| i | i \* i | i \* i > 16? | Action                 |
| - | ------ | ------------ | ---------------------- |
| 0 | 0      | No           | Continue               |
| 1 | 1      | No           | Continue               |
| 2 | 4      | No           | Continue               |
| 3 | 9      | No           | Continue               |
| 4 | 16     | No           | Continue               |
| 5 | 25     | **Yes**      | Return `5 - 1` → **4** |

---

### 📌 Summary:

* The loop finds the **first** `i` where `i² > x`
* Then returns `i - 1`, which is the **largest integer** whose square is ≤ `x`
* This is a **brute-force** way to compute `floor(sqrt(x))`

---

 