## Remove Duplicates from Sorted Array

###  Question

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

#### Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
#### Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 
### Solutions

#### solution 1 : 

break down your code **line by line**, and walk through it with an example:

---

### 🔸 Code:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[a]:
                a += 1
                nums[a] = nums[i]
        return a + 1
```

---

### 🧪 Example Input:

```python
nums = [1, 1, 2, 2, 3]
```

---

### ✅ Step-by-step Explanation:

#### `a = 0`

* This pointer `a` keeps track of the **position of the last unique element**.
* Initially, we assume the first element `nums[0] = 1` is unique.

#### `for i in range(1, len(nums))`

* We loop through the rest of the list, starting from index `1`.

---

### 🔄 Loop Iterations:

#### 🌀 i = 1:

* `nums[i] = nums[1] = 1`
* `nums[a] = nums[0] = 1`
* `1 == 1`, so it's a duplicate → **do nothing**.

#### 🌀 i = 2:

* `nums[i] = 2`, `nums[a] = 1`
* `2 != 1` → this is a **new unique element**
* `a += 1` → `a = 1`
* `nums[a] = nums[i]` → `nums[1] = 2`
* Now `nums = [1, 2, 2, 2, 3]`

#### 🌀 i = 3:

* `nums[i] = 2`, `nums[a] = 2`
* `2 == 2` → duplicate → **do nothing**

#### 🌀 i = 4:

* `nums[i] = 3`, `nums[a] = 2`
* `3 != 2` → new unique element
* `a += 1` → `a = 2`
* `nums[a] = nums[i]` → `nums[2] = 3`
* Now `nums = [1, 2, 3, 2, 3]`

---

### `return a + 1`

* `a = 2`, meaning we have 3 unique elements at indices 0, 1, 2
* So we return `3`

---

### ✅ Final Result:

```python
k = 3
nums[:k] = [1, 2, 3]  # unique elements
```

---

### 🧠 Summary:

* `a` points to where the next unique value should go.
* Every time we find a new unique value (`nums[i] != nums[a]`), we move it to the position after the last unique one.
* The function returns `a + 1` which is the count of unique values.

 


#### solution 2 :


  break down your code **line by line**, and walk through an example.

---

### 🔸 Code:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k = k + 1
        return k
```

---

### 🧪 Example Input:

```python
nums = [1, 1, 2, 2, 3]
```

---

### ✅ Line-by-Line Explanation:

---

#### `k = 1`

* `k` is the position where the **next unique number** should go.
* Since the first element is always unique, we start `k` from 1.

---

#### `for i in range(1, len(nums))`

* Start looping from the second element (`i = 1`) to the end of the list.

---

### 🔁 Loop Iterations:

#### ➤ `i = 1`

* `nums[i] = nums[1] = 1`
* `nums[i - 1] = nums[0] = 1`
* `1 == 1` → duplicate → skip

#### ➤ `i = 2`

* `nums[i] = 2`, `nums[i - 1] = 1`
* `2 != 1` → unique
* `nums[k] = nums[i]` → `nums[1] = 2`
* `k = k + 1` → `k = 2`
* Now `nums = [1, 2, 2, 2, 3]`

#### ➤ `i = 3`

* `nums[i] = 2`, `nums[i - 1] = 2`
* `2 == 2` → duplicate → skip

#### ➤ `i = 4`

* `nums[i] = 3`, `nums[i - 1] = 2`
* `3 != 2` → unique
* `nums[k] = nums[i]` → `nums[2] = 3`
* `k = k + 1` → `k = 3`
* Now `nums = [1, 2, 3, 2, 3]`

---

### `return k`

* `k = 3`, which means there are 3 unique elements.
* The modified list is: `nums[:k] = [1, 2, 3]`

---

### ✅ Final Output:

```python
k = 3
nums[:k] = [1, 2, 3]  # All unique elements, in-place
```

---

### 🧠 Summary:

| Variable | Meaning                                    |
| -------- | ------------------------------------------ |
| `i`      | Scans through the whole array              |
| `k`      | Tracks where to insert next unique element |

This method works **because the array is sorted** — so duplicates are **always next to each other**.

 