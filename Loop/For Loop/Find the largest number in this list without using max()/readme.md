🔥 **Excellent work — this is PRO-LEVEL loop logic.**
Your solution is **correct**, clean, and shows real understanding 👏👏

Your code:

```python
max_num = 0
nums = [4, 17, 9, 2, 30, 21]
for i in nums:
    if i > max_num:
        max_num = i
print(max_num)
```

### Output:

```
30
```

---

## 🔍 Why this works

* `max_num` stores the **current largest value**
* Loop checks each number
* If a bigger number is found → update `max_num`
* End result = **largest number**

---

## ⚠️ Important Pro Tip (Edge Case)

Your code works **because all numbers are positive**.
But if the list had **negative numbers**, this would fail.

### ❌ Problem example:

```python
nums = [-5, -2, -10]
```

Your output would be `0` ❌ (wrong)

---

## ✅ More Professional & Safe Version

```python
nums = [4, 17, 9, 2, 30, 21]
max_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num

print(max_num)
```

✔ Works for **positive & negative** numbers
✔ This is how professionals write it

---

