## 88. Merge Sorted Array

### Question

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

#### Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#### Example 2:

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

#### Example 3:

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in     nums1.
 
### Answer 

 
---

#### ✅ **Function Purpose**:

The `merge` function merges two sorted arrays, `nums1` and `nums2`, into one sorted array **in-place** in `nums1`.

* `nums1` has a size of `m + n`, where the first `m` elements are valid, and the rest (`n` elements) are zeros (placeholders).
* `nums2` has `n` elements.
* Both `nums1[:m]` and `nums2` are **sorted in non-decreasing order**.

---

### ✅ **Example Input**:

```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3
```

We want to merge them so that `nums1` becomes:

```python
[1, 2, 2, 3, 5, 6]
```

---

### ✅ **Step-by-Step Explanation**:

```python
p1, p2, p = m - 1, n - 1, m + n - 1
```

* `p1 = 2` → pointing at `3` in `nums1`
* `p2 = 2` → pointing at `6` in `nums2`
* `p = 5` → index where we place the next largest value

---

### ✅ **Main Loop: while p1 >= 0 and p2 >= 0**

This loop compares the current elements at `p1` and `p2`, placing the **larger** one at position `p` in `nums1`.

---

#### 🔁 First iteration:

```python
nums1[p1] = 3
nums2[p2] = 6
```

* Since `6 > 3`, we place `6` at `nums1[5]`.

```python
nums1 = [1, 2, 3, 0, 0, 6]
p2 = 1, p = 4
```

---

#### 🔁 Second iteration:

```python
nums1[p1] = 3
nums2[p2] = 5
```

* `5 > 3`, so we place `5` at `nums1[4]`.

```python
nums1 = [1, 2, 3, 0, 5, 6]
p2 = 0, p = 3
```

---

#### 🔁 Third iteration:

```python
nums1[p1] = 3
nums2[p2] = 2
```

* `3 > 2`, so we place `3` at `nums1[3]`.

```python
nums1 = [1, 2, 3, 3, 5, 6]
p1 = 1, p = 2
```

---

#### 🔁 Fourth iteration:

```python
nums1[p1] = 2
nums2[p2] = 2
```

* Equal values → pick from `nums2` (arbitrary, doesn't matter), place `2` at `nums1[2]`.

```python
nums1 = [1, 2, 2, 3, 5, 6]
p2 = -1, p = 1
```

* Loop ends because `p2 < 0`.

---

### ✅ **Handle Remaining Elements**

#### `while p1 >= 0`:

* `p1 = 1`, but all elements are already in the correct position, so this loop runs but doesn't change anything.

#### `while p2 >= 0`:

* Already `p2 = -1`, so this loop is skipped.

---

### ✅ Final Output:

```python
nums1 = [1, 2, 2, 3, 5, 6]
```

---

### ✅ Summary of Steps:

| Step | p1 | p2 | p | nums1                      | Action             |
| ---- | -- | -- | - | -------------------------- | ------------------ |
| 1    | 2  | 2  | 5 | \[1, 2, 3, 0, 0, 6]        | Place 6 from nums2 |
| 2    | 2  | 1  | 4 | \[1, 2, 3, 0, 5, 6]        | Place 5 from nums2 |
| 3    | 2  | 0  | 3 | \[1, 2, 3, 3, 5, 6]        | Place 3 from nums1 |
| 4    | 1  | 0  | 2 | \[1, 2, 2, 3, 5, 6]        | Place 2 from nums2 |
| 5    | 1  | -1 | 1 | \[1, 2, 2, 3, 5, 6] (done) | Merge complete     |

---

 