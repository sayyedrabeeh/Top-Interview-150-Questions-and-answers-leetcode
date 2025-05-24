### Find the Index of the First Occurrence in a String

#### Question  

    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if    needle is not part of haystack.

 

#### Example 1:
   
   Input: haystack = "sadbutsad", needle = "sad"
   Output: 0
   Explanation: "sad" occurs at index 0 and 6.
   The first occurrence is at index 0, so we return 0.
#### Example 2:

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
### solution  explanation 

Let's break down the code and   how it works **line by line**, including what happens internally in Python:

---

### ✅ Full Code:

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

---

### 🔍 Line-by-Line Explanation:

#### `class Solution:`

* This defines a class named `Solution`.
* In many coding platforms (like LeetCode), the problem is wrapped in a class so that the method can be tested using a specific interface.

#### `def strStr(self, haystack: str, needle: str) -> int:`

* This defines a method named `strStr` inside the `Solution` class.
* It takes three arguments:

  * `self`: refers to the current instance of the class (required in instance methods).
  * `haystack`: a string where we are searching **from**.
  * `needle`: the substring we are searching **for**.
* The `-> int` means this function will return an **integer**.

#### `return haystack.find(needle)`

* This line performs the actual logic.
* `.find()` is a **built-in Python string method**:

  * It searches for the first occurrence of the substring (`needle`) in the main string (`haystack`).
  * If `needle` is found, it returns the **index** of the first occurrence (starting from 0).
  * If `needle` is not found, it returns `-1`.

---

### ⚙️ Example:

```python
sol = Solution()
print(sol.strStr("hello", "ll"))  # Output: 2
```

**Why 2?**

* `"ll"` starts at index 2 in `"hello"` (`h=0, e=1, l=2`...)

---

### ⚙️ What happens inside `.find()`?

Under the hood, Python's `str.find()` is implemented in C for speed (in CPython, the default Python interpreter). Internally, it uses an efficient string-search algorithm like:

* **Rabin-Karp**
* or **Boyer-Moore**
* or even simple sliding window in some cases

These are more optimized than manually checking each substring in a Python loop.

---

### 🔁 Manual alternative to `.find()`:

If we didn't use `.find()`, a basic version might look like:

```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
```

This uses a sliding window to compare substrings.

---

### Summary:

| Part                    | Role                                          |
| ----------------------- | --------------------------------------------- |
| `class Solution:`       | Organizes the function into a class           |
| `def strStr(...)`       | Defines a method to solve the problem         |
| `haystack.find(needle)` | Searches for `needle` inside `haystack`       |
| Return value            | Index of first occurrence, or -1 if not found |

 