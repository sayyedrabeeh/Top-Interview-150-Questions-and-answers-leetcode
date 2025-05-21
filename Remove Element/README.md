## 27. Remove Element

### Questions

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

#### Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
#### Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

## answer explaination 


Absolutely! Here's a line-by-line explanation of your code:

---

### ✅ **Full Code**

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        for i in nums:
            if i != val:
                nums[a] = i
                a += 1
        return a
```

---

### 🧩 **Explanation of Each Line**

---

#### `class Solution:`

* This defines a class named `Solution`.
* In coding platforms like LeetCode, this is the standard format to wrap your solution.
* All your methods (like `removeElement`) will go inside this class.

---

#### `def removeElement(self, nums: List[int], val: int) -> int:`

* This defines a method named `removeElement` inside the `Solution` class.
* `self`: refers to the current instance of the class.
* `nums: List[int]`: `nums` is a list of integers. This is the input array.
* `val: int`: `val` is the integer you want to remove from the array.
* `-> int`: This method will return an integer — specifically, the new length of the modified array.

---

#### `a = 0`

* This initializes a variable `a` to 0.
* `a` will keep track of the index where the next non-`val` element should be placed.
* Think of `a` as a “write pointer.”

---

#### `for i in nums:`

* This is a loop that iterates through each element `i` in the list `nums`.
* It checks each number to decide whether to keep it (if it's not equal to `val`).

---

#### `if i != val:`

* This checks if the current element `i` is **not equal** to `val`.
* If it’s not the value we want to remove, we keep it by placing it at index `a`.

---

#### `nums[a] = i`

* This line overwrites the element at index `a` in the list with the value `i`.
* It effectively moves the valid element (not equal to `val`) to the front portion of the list.

---

#### `a += 1`

* After placing a valid element at index `a`, we increment `a` by 1.
* This moves the write pointer forward for the next valid element.

---

#### `return a`

* After the loop ends, `a` holds the count of elements that are **not equal** to `val`.
* Since the list is modified in-place, the first `a` elements are the ones you should keep.
* This is the new "length" of the list with `val` removed.

---

### 💡 Example Walkthrough

Let’s walk through the example:

```python
nums = [3, 2, 2, 3]
val = 3
```

* Initially: `a = 0`
* Loop:

  * `i = 3`: skip (3 == val)
  * `i = 2`: keep → `nums[0] = 2`, `a = 1`
  * `i = 2`: keep → `nums[1] = 2`, `a = 2`
  * `i = 3`: skip
* Final array: `[2, 2, _, _]`
* Return value: `2`

So, the list is modified to `[2, 2]` (ignoring the rest), and the function returns `2`.

---

 