# Assignment 03 — CHANGES

**Name:** Ye Yint Tun Thant **Student ID:** 6705140016

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products were stored as tuples like `("Laptop", 1200.0, "electronics")` | Created a `Product` class with `name`, `price`, and `category` | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | Tier discounts and points used repeated `if tier == ...` logic | Created `Customer`, `Silver`, `Gold`, and `Platinum` classes with overridden methods | Inheritance / polymorphism | Ran `python Assignment_03.py` → PASS |
| 3 | Products, items, and orders were handled as raw data structures | Created `Product`, `OrderItem`, and `Order` objects that contain the related data and behavior | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 4 | Calculation logic was mixed with printing output | Moved calculations into methods such as `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` that return values | Encapsulation / separation of concerns | Ran `python Assignment_03.py` → PASS |
| 5 | Magic numbers and repeated business values were used directly in calculations | Added named constants such as `TAX_RATE`, `DISCOUNT_THRESHOLD`, and `BULK_DISCOUNT_RATE` | Encapsulation / named constants | Ran `python Assignment_03.py` → PASS |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> The biggest improvement was replacing the repeated tier `if` statements with customer subclasses and polymorphism. This makes the discount and points rules easier to understand and keep separate for each tier. Creating classes for products, order items, and orders also made the relationships between the data clearer. Keeping the behaviour identical required me to be careful with the original discount, tax, total, points, and receipt output. I checked the refactored program by running `python Assignment_03.py` and confirming that the self-test printed PASS.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | I asked for help completing Assignment 03 step-by-step | Helped refactor the legacy store system into classes, inheritance, polymorphism, and composition | Accepted and edited as needed | Ran `python Assignment_03.py` → PASS |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
