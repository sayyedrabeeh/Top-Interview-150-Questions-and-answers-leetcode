## Majority Element

### Question 
   Given an array nums of size n, return the majority element.

   The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

#### Example 1:

    Input: nums = [3,2,3]
    Output: 3
#### Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
 
### solution 


  Let's break down the code **line by line** and understand what it's doing:

```python
class Solution:
```

* This defines a class named `Solution`.
 
---

```python
    def majorityElement(self, nums: List[int]) -> int:
```

* This defines a **method** called `majorityElement` inside the `Solution` class.
* It takes one argument `nums`, which is a **list of integers**.
* The expected return type is an `int`.
* The problem assumes that a **majority element always exists**, which means some number appears **more than n/2 times** in the list.

---

```python
        nums.sort()
```

* This sorts the list `nums` in **ascending order**.
* Why? Because if an element appears more than `n/2` times, it will **always occupy the middle index** after sorting.
* Example: `nums = [3, 3, 4, 2, 3]` → after sorting: `[2, 3, 3, 3, 4]` → middle index = 2, value = 3.

---

```python
        return nums[len(nums)//2]
```

* This returns the element at the middle index of the sorted list.
* `len(nums) // 2` gives the **integer division** of the length, which is the middle.
* Because the majority element occurs **more than half the time**, this index is guaranteed to be that element.

---

### ✅ Summary:

This method works based on the property that in a sorted array, the majority element will always be at the center (or close to it). It's a simple and efficient way (O(n log n)) to solve the problem.

 