Great 👍 Since you’re learning Python step-by-step, let’s cover **`try–except` from zero to confident level**, and then we’ll **practice together**.

---

# 1️⃣ What is `try–except`?

In Python, **errors (exceptions)** can stop your program.

Example ❌ (program crashes):

```python
x = 10
y = 0
print(x / y)
```

Output:

```
ZeroDivisionError: division by zero
```

💡 **Problem:** The program stops immediately.

✅ **Solution:** Use `try–except` to **handle errors safely**.

---

# 2️⃣ Basic `try–except` Syntax

```python
try:
    # code that may cause an error
except:
    # code that runs if error occurs
```

Example:

```python
try:
    x = 10
    y = 0
    print(x / y)
except:
    print("Error occurred")
```

Output:

```
Error occurred
```

✔ Program does **not crash**

---

# 3️⃣ Catching Specific Errors (IMPORTANT)

It’s **bad practice** to catch all errors blindly.

### Common Python Errors

| Error               | When it happens         |
| ------------------- | ----------------------- |
| `ZeroDivisionError` | divide by zero          |
| `ValueError`        | wrong value type        |
| `TypeError`         | wrong data type         |
| `IndexError`        | list index out of range |
| `KeyError`          | dictionary key missing  |

Example:

```python
try:
    num = int("abc")
except ValueError:
    print("Please enter a number")
```

✔ Handles only **ValueError**

---

# 4️⃣ Multiple `except` Blocks

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

✔ Different message for different errors

---

# 5️⃣ `else` with `try–except`

`else` runs **only if no error occurs**

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Zero not allowed")
except ValueError:
    print("Invalid input")
else:
    print("Calculation successful")
```

✔ Cleaner logic

---

# 6️⃣ `finally` Block (ALWAYS RUNS)

Used for **cleanup** (closing files, connections)

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Error occurred")
finally:
    print("Program finished")
```

✔ `finally` runs **no matter what**

---

# 7️⃣ Using `try–except` with User Input (Very Common)

❌ Without try-except:

```python
age = int(input("Enter age: "))
```

✅ With try-except:

```python
try:
    age = int(input("Enter age: "))
    print("Your age is", age)
except ValueError:
    print("Age must be a number")
```

---

# 8️⃣ Storing Error Message

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
```

Output:

```
Error: division by zero
```

---

# 9️⃣ When to Use `try–except`

✅ Use when:

* User input
* File handling
* API calls
* Database connections
* Calculations that may fail

❌ Don’t use to hide logic mistakes

---

# 🔟 Real-Life Example (File Handling)

```python
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Done")
```

---

# 🧠 Simple Rule to Remember

> **TRY → risky code**
> **EXCEPT → handle error**
> **ELSE → runs if no error**
> **FINALLY → always runs**

---

## 🧪 PRACTICE TIME (You Answer)

### Practice 1️⃣

What will this print?

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Cannot divide")
```


wers, and I’ll **correct + improve your code** step by step 👍
