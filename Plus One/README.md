### Plus One

#### Question 

   You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the    integer. The digits are ordered from most significant to least significant in left-to-right order. The large    integer does not contain any leading 0's.
   
   Increment the large integer by one and return the resulting array of digits.

 

#### Example 1:

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].
#### Example 2:

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].
#### Example 3:

   Input: digits = [9]
   Output: [1,0]
   Explanation: The array represents the integer 9.
   Incrementing by one gives 9 + 1 = 10.
   Thus, the result should be [1,0].
    
#### explanation 

  
### 👩‍💻 Code:

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''.join(map(str, digits))
        b = int(a) + 1
        c = [int(i) for i in str(b)]
        return c
```

---

### ✅ Purpose:

This function simulates **adding one** to a number represented as a list of digits.

### 📌 Example Input:

```python
digits = [1, 2, 9]
```

This represents the number **129**, and we want to return **130** as a list: `[1, 3, 0]`.

---

## 🔍 Step-by-step Breakdown:

---

### 🔹 Line 1: `a = ''.join(map(str, digits))`

#### ✅ What it does:

* Converts each digit to a string and **joins them together** into a single string.

#### 🔄 Operation:

```python
map(str, digits) → ['1', '2', '9']
''.join(...) → '129'
```

#### ✅ Result:

```python
a = '129'  # String form of the number
```

---

### 🔹 Line 2: `b = int(a) + 1`

#### ✅ What it does:

* Converts the string `'129'` to an integer, adds `1` to it.

#### 🔄 Operation:

```python
int('129') → 129
129 + 1 → 130
```

#### ✅ Result:

```python
b = 130  # Integer after increment
```

---

### 🔹 Line 3: `c = [int(i) for i in str(b)]`

#### ✅ What it does:

* Converts the integer `130` back to a string `'130'`, then iterates over each character and converts it back to an integer.

#### 🔄 Operation:

```python
str(130) → '130'
[ int(i) for i in '130' ] → [1, 3, 0]
```

#### ✅ Result:

```python
c = [1, 3, 0]
```

---

### 🔹 Line 4: `return c`

#### ✅ What it does:

Returns the final list of digits after the +1 operation.

---

### ✅ Final Output:

```python
[1, 3, 0]
```

---

## 🔁 Recap with Example:

Input: `[1, 2, 9]`
Process:

* `'129'` → `130` → `'130'` → `[1, 3, 0]`
  Output: `[1, 3, 0]`

---

 