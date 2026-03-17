# 🧩 ARRAYS & STRINGS — COMPLETE ALGORITHM DECISION MAP
### SDE Interview Preparation | Pattern Recognition Guide

---

## 🔍 MASTER DECISION TREE

```
READ THE PROBLEM
│
├─► About SUBARRAY or SUBSTRING?
│       │
│       ├─ Window size K is FIXED           →  Sliding Window (Fixed)          O(N)
│       ├─ Window size VARIABLE, all +ve    →  Sliding Window (Variable)       O(N)
│       ├─ Has NEGATIVES, find sum = K      →  Prefix Sum + HashMap             O(N)
│       ├─ MAXIMUM subarray sum             →  Kadane's Algorithm               O(N)
│       ├─ XOR of subarray = K              →  Prefix XOR + HashMap             O(N)
│       └─ Count subarrays with condition   →  Prefix Sum / Two Pointer        O(N)
│
├─► Array is SORTED (or CAN be sorted)?
│       │
│       ├─ Find PAIR with sum = X           →  Two Pointers [0, N-1]            O(N)
│       ├─ Find TRIPLET with sum = X        →  Fix one + Two Pointers           O(N²)
│       ├─ SEARCH an element                →  Binary Search                    O(log N)
│       └─ MERGE two sorted arrays          →  Two Pointers                     O(N+M)
│
├─► SEARCH or OPTIMIZATION problem?
│       │
│       ├─ Find element in sorted array     →  Binary Search                    O(log N)
│       ├─ Minimize/Maximize a value        →  Binary Search on Answer Space   O(N log N)
│       └─ Rotated sorted array             →  Modified Binary Search           O(log N)
│
├─► FREQUENCY or COUNTING problem?
│       │
│       ├─ Duplicates, majority element     →  HashMap                          O(N)
│       │                                      OR Boyer-Moore Voting             O(N), O(1)
│       ├─ Range is [0, N] (small range)    →  Array-as-Hash (index trick)      O(N)
│       ├─ Anagram / permutation check      →  Frequency Array (size 26)        O(N)
│       └─ First missing positive           →  Index marking / Negation         O(N)
│
├─► NUMBERS or MATH?
│       │
│       ├─ GCD / HCF related               →  Euclidean Algorithm              O(log min(a,b))
│       ├─ Find all factors of N            →  Loop till √N                     O(√N)
│       ├─ Missing / extra number           →  XOR trick  OR  Math sum          O(N)
│       ├─ |A[i] - A[j]| maximize          →  Split into expressions → max-min  O(N)
│       └─ Absolute value expressions      →  ±sign expansion (2^k combos)      O(N)
│
├─► SPECIAL SORTING?
│       │
│       ├─ Range known [0, K]              →  Counting Sort / Bucket Sort        O(N+K)
│       ├─ Sort 0s, 1s, 2s (Dutch Flag)   →  Dutch National Flag                O(N)
│       ├─ Max gap in sorted form          →  Bucket Sort (PigeonHole)           O(N)
│       └─ Custom order sort              →  HashMap-based sort                  O(N)
│
├─► STACK-BASED pattern?
│       │
│       ├─ Next greater / smaller element  →  Monotonic Stack                   O(N)
│       ├─ Largest rectangle in histogram  →  Monotonic Stack                   O(N)
│       └─ Valid parentheses / nesting     →  Stack                             O(N)
│
└─► 2D MATRIX?
        │
        ├─ Submatrix sum queries            →  2D Prefix Sum                     O(N*M) build, O(1) query
        ├─ Search in sorted matrix          →  Eliminate row/column (top-right)  O(N+M)
        ├─ Rain water / area problems       →  Prefix arrays or Stack            O(N)
        └─ Sum of all rectangles            →  Contribution technique            O(N*M)
```

---

## 🧠 PATTERN MNEMONICS (Easy to Remember)

| Pattern | Mnemonic | One Line Rule |
|---|---|---|
| Two Pointers (sorted) | **"Squeeze from both ends"** | Sorted array + pair/triplet sum → [0, N-1] |
| Two Pointers (unsorted) | **"Expand and shrink"** | Sliding window for positive arrays |
| Prefix Sum + Map | **"Store what you've seen"** | Sum of subarray = current - past |
| Sliding Window | **"Move the frame"** | Contiguous subarray/substring problems |
| Binary Search | **"Halve the search"** | Sorted input OR answer has monotonic property |
| HashMap | **"Remember fast"** | Lookup in O(1), trade space for time |
| Kadane's | **"Keep or restart"** | Reset when running sum goes negative |
| Monotonic Stack | **"Kill smaller, keep larger"** | Next greater/smaller element |
| XOR Trick | **"Cancel duplicates"** | A^A=0, A^0=A — find single/missing number |
| Dutch Flag | **"3 buckets, 1 pass"** | Sort array with only 3 distinct values |
| Boyer-Moore | **"Survive majority"** | Element appearing > N/2 times survives cancellation |
| Bucket Sort | **"PigeonHole: empty buckets hold the gap"** | Max gap must span across an empty bucket |

---

## ⚡ QUICK KEYWORD → ALGORITHM TRIGGER TABLE

| You See This Keyword | Algorithm to Use | Time Complexity |
|---|---|---|
| subarray sum = K (positives only) | Sliding Window | O(N) |
| subarray sum = K (with negatives) | Prefix Sum + HashMap | O(N) |
| maximum subarray sum | Kadane's Algorithm | O(N) |
| longest substring with K distinct chars | Sliding Window (variable) | O(N) |
| longest substring without repeating | Sliding Window + HashSet | O(N) |
| count anagram windows of size K | Sliding Window + freq array | O(N) |
| XOR of subarray = K | Prefix XOR + HashMap | O(N) |
| pair with sum = X (sorted array) | Two Pointers [0, N-1] | O(N) |
| pair with sum = X (unsorted) | HashMap | O(N) |
| triplet with sum = X | Sort + Fix one + Two Pointers | O(N²) |
| two sum / three sum | Two Pointers or HashMap | O(N) / O(N²) |
| search in sorted array | Binary Search | O(log N) |
| find kth largest / smallest | QuickSelect or Heap | O(N) avg / O(N log K) |
| minimize maximum / maximize minimum | Binary Search on Answer Space | O(N log N) |
| majority element (>N/2) | Boyer-Moore Voting | O(N), O(1) |
| duplicates in array | HashMap or Index marking | O(N) |
| first missing positive | Index negation trick | O(N), O(1) |
| missing number / extra number | XOR or Math formula | O(N) |
| next greater element | Monotonic Stack | O(N) |
| largest rectangle in histogram | Monotonic Stack | O(N) |
| rain water trapping | Two Pointers or Prefix arrays | O(N) |
| sort 0s 1s 2s | Dutch National Flag | O(N) |
| max gap in sorted form | Bucket Sort | O(N) |
| range [0, N] elements | Counting Sort / Array as Hash | O(N) |
| GCD of array | Euclidean (iterative on pairs) | O(N log M) |
| all factors of N | Loop till √N | O(√N) |
| reverse string / array | Two Pointers [0, N-1] | O(N) |
| check palindrome | Two Pointers | O(N) |
| anagram check | Sort both OR freq count | O(N log N) / O(N) |
| longest common prefix | Sort + compare first & last | O(N log N) |
| string compression / encoding | Two Pointers / counter | O(N) |
| rotate array by K | Reverse trick (3 reverses) | O(N), O(1) |
| product of array except self | Prefix + Postfix product | O(N), O(1) |
| trap rain water | Prefix max L, Prefix max R | O(N) |
| merge intervals | Sort by start + greedy | O(N log N) |
| subarray XOR questions | Prefix XOR + HashMap | O(N) |
| absolute value maximize | Expand ± signs → max-min | O(N) |
| 2D matrix subarray sum | 2D Prefix Sum | O(NM) build, O(1) query |
| sum of all rectangles | Contribution of each cell | O(N*M) |

---

## 📊 ALGORITHM COMPLEXITY REFERENCE

```
┌──────────────────────────────────┬──────────────────┬──────────────┬──────────────────────────────┐
│ Algorithm / Pattern              │ Time Complexity  │ Space        │ Best Used When               │
├──────────────────────────────────┼──────────────────┼──────────────┼──────────────────────────────┤
│ Brute Force (nested loops)       │ O(N²) or O(N³)  │ O(1)         │ N ≤ 1000, simple logic       │
│ Two Pointers (sorted)            │ O(N)             │ O(1)         │ Sorted array, pair/triplet   │
│ Sliding Window (fixed)           │ O(N)             │ O(1) or O(K) │ Fixed window size K          │
│ Sliding Window (variable)        │ O(N)             │ O(N)         │ Longest/shortest subarray    │
│ Prefix Sum + HashMap             │ O(N)             │ O(N)         │ Subarray sum = K, negatives  │
│ Prefix XOR + HashMap             │ O(N)             │ O(N)         │ Subarray XOR = K             │
│ Kadane's Algorithm               │ O(N)             │ O(1)         │ Maximum subarray sum         │
│ Binary Search (sorted)           │ O(log N)         │ O(1)         │ Sorted array, find element   │
│ Binary Search on Answer          │ O(N log N)       │ O(1)         │ Min/Max optimization         │
│ HashMap / HashSet                │ O(N)             │ O(N)         │ Frequency, lookup, duplicate │
│ Boyer-Moore Voting               │ O(N)             │ O(1)         │ Majority element > N/2       │
│ Sorting (general)                │ O(N log N)       │ O(1) or O(N) │ When order helps simplify    │
│ Counting Sort                    │ O(N + K)         │ O(K)         │ Small range [0, K]           │
│ Bucket Sort                      │ O(N)             │ O(N)         │ Uniformly distributed range  │
│ Dutch National Flag              │ O(N)             │ O(1)         │ Sort 3 values in-place       │
│ Monotonic Stack                  │ O(N)             │ O(N)         │ Next greater/smaller element │
│ Prefix + Postfix Arrays          │ O(N)             │ O(N)         │ Rain water, product except   │
│ Index as Hash (negation trick)   │ O(N)             │ O(1)         │ Array vals in [1, N] range   │
│ XOR Trick                        │ O(N)             │ O(1)         │ Find missing / single number │
│ Euclidean GCD                    │ O(log min(a,b))  │ O(1)         │ GCD of two numbers           │
│ GCD of Array                     │ O(N log M)       │ O(1)         │ GCD of all elements          │
│ Factors of N                     │ O(√N)            │ O(√N)        │ Find all divisors            │
│ 2D Prefix Sum                    │ O(NM) build      │ O(NM)        │ Rectangle sum queries        │
│                                  │ O(1) query       │              │                              │
│ Contribution Technique           │ O(N) or O(NM)    │ O(1)         │ Sum over all subarrays       │
│ Reverse Trick (rotate array)     │ O(N)             │ O(1)         │ Rotate array by K positions  │
│ QuickSelect                      │ O(N) avg, O(N²)  │ O(1)         │ Kth largest/smallest         │
│ Merge Sort (divide & conquer)    │ O(N log N)       │ O(N)         │ Count inversions             │
└──────────────────────────────────┴──────────────────┴──────────────┴──────────────────────────────┘
```

---

## 🎯 QUESTION TYPE → ALGORITHM MAP (By Category)

---

### 1. 🔢 SUBARRAY PROBLEMS

```
Does array have NEGATIVE numbers?
│
├─ NO (all positive)
│     │
│     ├─ Fixed window size K?   →  Sliding Window (fixed)        O(N)
│     └─ Variable window?       →  Sliding Window (variable)     O(N)
│          (two pointers [0,0], expand right, shrink left)
│
└─ YES (has negatives)
      │
      ├─ Subarray sum = K?       →  Prefix Sum + HashMap          O(N)
      ├─ Longest subarray sum=0? →  Prefix Sum + HashMap          O(N)
      └─ Max subarray sum?       →  Kadane's Algorithm            O(N)

XOR of subarray = K?             →  Prefix XOR + HashMap         O(N)
```

**Interview Questions:**
- Maximum sum subarray → **Kadane's** `O(N)`
- Subarray with sum = K (positives) → **Sliding Window** `O(N)`
- Subarray with sum = K (negatives) → **Prefix Sum + Map** `O(N)`
- Longest subarray with zero sum → **Prefix Sum + Map** `O(N)`
- Count subarrays with XOR = K → **Prefix XOR + Map** `O(N)`
- Maximum of every window of size K → **Deque (Monotonic)** `O(N)`
- First negative in every window → **Deque + Sliding Window** `O(N)`
- Smallest subarray with sum ≥ X → **Sliding Window** `O(N)`
- Product of subarray except self → **Prefix × Postfix** `O(N)`

---

### 2. 👆 TWO POINTER PROBLEMS

```
Is array SORTED?
│
├─ YES →  Two Pointers [left=0, right=N-1]    O(N)
│           - Move inward based on sum vs target
│           - Works for pair, triplet, 4-sum
│
└─ NO  →  Sort first O(N log N), then two pointers
           OR use HashMap for O(N)
```

**Interview Questions:**
- Two sum (sorted) → **Two Pointers** `O(N)`
- Two sum (unsorted) → **HashMap** `O(N)`
- Three sum (triplet = 0) → **Sort + Fix one + Two Pointers** `O(N²)`
- Container with most water → **Two Pointers** `O(N)`
- Reverse array/string → **Two Pointers** `O(N)`
- Remove duplicates from sorted array → **Two Pointers** `O(N)`
- Move zeros to end → **Two Pointers** `O(N)`
- Sort 0s and 1s → **Two Pointers** `O(N)`
- Merge two sorted arrays → **Two Pointers** `O(N+M)`
- Rain water trapped → **Two Pointers** `O(N)` or **Prefix Arrays** `O(N)`

---

### 3. 🔎 BINARY SEARCH PROBLEMS

```
Is input SORTED?  OR  Does answer have a MONOTONIC property?
│
├─ YES, simple sorted array    →  Classic Binary Search           O(log N)
├─ Rotated sorted array        →  Modified Binary Search          O(log N)
├─ "Minimize the maximum"      →  Binary Search on Answer Space   O(N log N)
├─ "Maximize the minimum"      →  Binary Search on Answer Space   O(N log N)
└─ 2D sorted matrix            →  Eliminate row/column            O(N + M)
```

**Interview Questions:**
- Search in sorted array → **Binary Search** `O(log N)`
- Search in rotated sorted array → **Modified Binary Search** `O(log N)`
- Find first/last occurrence → **Binary Search** `O(log N)`
- Kth smallest in sorted matrix → **Binary Search on value** `O(N log(max-min))`
- Minimum in rotated sorted array → **Binary Search** `O(log N)`
- Allocate books / Painters partition → **Binary Search on Answer** `O(N log N)`
- Aggressive cows (maximize min distance) → **Binary Search on Answer** `O(N log N)`
- Square root of N (integer) → **Binary Search** `O(log N)`

---

### 4. 🗺️ HASHMAP / COUNTING PROBLEMS

```
Do you need to COUNT or LOOKUP elements quickly?
│
├─ Frequency of elements      →  HashMap { element: count }       O(N)
├─ Check if element exists    →  HashSet                           O(N) space, O(1) lookup
├─ Range is [0, N] (small)   →  Array as Hash (index trick)       O(N), O(1) extra
└─ Find majority element      →  Boyer-Moore Voting               O(N), O(1)
```

**Interview Questions:**
- Find duplicates → **HashMap** `O(N)`
- First non-repeating character → **HashMap (ordered)** `O(N)`
- Majority element (>N/2) → **Boyer-Moore** `O(N), O(1)`
- Find missing number → **XOR** or **Math sum** `O(N)`
- Find all elements appearing > N/3 → **Boyer-Moore (2 candidates)** `O(N)`
- Longest consecutive sequence → **HashSet** `O(N)`
- Top K frequent elements → **HashMap + Heap** `O(N log K)`
- First missing positive → **Index negation** `O(N), O(1)`
- Check anagram → **Frequency array** `O(N)`
- Group anagrams → **Sort key HashMap** `O(N*K log K)`

---

### 5. 📏 SLIDING WINDOW PROBLEMS

```
                    SLIDING WINDOW
                          │
         ┌────────────────┴─────────────────┐
    FIXED size K                      VARIABLE size
         │                                  │
   Deque / simple loop            Two pointer [i=0, j=0]
         │                                  │
  - Max in window                  - Longest with condition
  - Min in window                  - Shortest with sum ≥ K
  - Anagram count                  - K distinct characters
  - First negative                 - No repeating chars

KEY RULE: Sliding window only works when elements are POSITIVE
          (shrinking window reduces sum → valid for positive arrays)
          For negatives → use Prefix Sum + HashMap
```

**Fixed Window `O(N)`:**
- Maximum sum of K elements
- Maximum/minimum in each window of size K → Deque
- Count anagrams of pattern in string → Freq array
- First negative in every window of size K → Deque

**Variable Window `O(N)`:**
- Longest subarray with sum = K (positives) → Expand/shrink
- Longest substring with K distinct chars
- Longest substring without repeating chars → HashSet
- Smallest subarray with sum ≥ S
- Minimum window substring containing all chars

---

### 6. 📐 PREFIX / POSTFIX PROBLEMS

```
Question involves range [L, R] sum, product, XOR → BUILD prefix array

prefix[i] = prefix[i-1] + arr[i]
range_sum(L, R) = prefix[R] - prefix[L-1]

Combine with HashMap:
  prefix[i] = target  → subarray from 0..i is answer
  prefix[i] - K in map → subarray ending at i with sum K exists
```

**Interview Questions:**
- Range sum queries → **Prefix Sum** `O(N) build, O(1) query`
- Count subarrays with sum = K → **Prefix Sum + HashMap** `O(N)`
- Longest subarray with sum = 0 → **Prefix Sum + HashMap** `O(N)`
- Product of array except self → **Prefix × Postfix product** `O(N)`
- Max profit (stock prices) → **Prefix min** `O(N)`
- Maximum of prefix/suffix → Rain water, trapping problems
- GCD of subarray (delete one element) → **Prefix + Postfix GCD** `O(N)`

---

### 7. 🔢 XOR / BIT MANIPULATION

```
XOR Properties (Golden Rules):
  A ^ A = 0          (cancel duplicates)
  A ^ 0 = A          (identity)
  A ^ B = C  →  C ^ A = B  (reversible)

Prefix XOR:
  prefix_xor[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
  xor(L, R) = prefix_xor[R] ^ prefix_xor[L-1]
```

**Interview Questions:**
- Find single number in array (others appear twice) → **XOR all** `O(N), O(1)`
- Find missing number in [1..N] → **XOR with 1..N** `O(N), O(1)`
- Two missing numbers → **XOR + bit separation** `O(N)`
- Count subarrays with XOR = K → **Prefix XOR + HashMap** `O(N)`
- Check if bit is set → `A & (1 << bit)` `O(1)`
- Swap two numbers → `A ^= B; B ^= A; A ^= B` `O(1)`

---

### 8. 📊 SORTING-BASED PROBLEMS

```
When to Sort First?
  - Two/three sum problems (sorted enables two pointers)
  - Merge intervals (sort by start)
  - Anagram grouping (sort each word as key)
  - Find median of two sorted arrays

Special Sorts:
  Range [0, K] known       →  Counting Sort       O(N + K)
  3 distinct values        →  Dutch National Flag  O(N)
  Uniformly distributed    →  Bucket Sort          O(N)
  Max gap in sorted form   →  Bucket Sort          O(N)
```

**Interview Questions:**
- Sort array of 0s, 1s, 2s → **Dutch National Flag** `O(N), O(1)`
- Maximum gap in sorted form → **Bucket Sort** `O(N)`
- Merge intervals → **Sort by start + greedy** `O(N log N)`
- Sort characters by frequency → **HashMap + sort** `O(N log N)`
- Largest number (custom sort) → **Comparator sort** `O(N log N)`
- Find kth largest → **QuickSelect** `O(N) avg` or **Heap** `O(N log K)`
- Count inversions → **Merge Sort** `O(N log N)`

---

### 9. 📚 STACK-BASED PROBLEMS

```
See "Next Greater / Smaller"?        →  Monotonic Stack     O(N)
See "Histogram / Rectangle area"?    →  Monotonic Stack     O(N)
See "Balanced brackets"?             →  Stack               O(N)
See "Evaluate expression"?           →  Stack               O(N)
```

**Interview Questions:**
- Next greater element → **Monotonic Stack** `O(N)`
- Next smaller element → **Monotonic Stack** `O(N)`
- Largest rectangle in histogram → **Monotonic Stack** `O(N)`
- Maximal rectangle in binary matrix → **Histogram + Stack** `O(N*M)`
- Valid parentheses → **Stack** `O(N)`
- Daily temperatures → **Monotonic Stack** `O(N)`
- Stock span problem → **Monotonic Stack** `O(N)`
- Trapping rain water → **Stack** OR **Two Pointers** `O(N)`

---

### 10. 🔤 STRING-SPECIFIC PROBLEMS

```
Check character frequency?  →  Array[26] or HashMap
Need all permutations?      →  Backtracking          O(N * N!)
Pattern matching?           →  KMP Algorithm         O(N + M)
Longest common substring?   →  DP (2D table)         O(N * M)
Palindrome check?           →  Two Pointers          O(N)
Longest palindromic substr? →  Expand around center  O(N²)
                               OR Manacher's          O(N)
```

**Interview Questions:**
- Reverse string → **Two Pointers** `O(N)`
- Check palindrome → **Two Pointers** `O(N)`
- Check anagram → **Freq array** `O(N)`
- Longest palindromic substring → **Expand center** `O(N²)` / **Manacher's** `O(N)`
- String compression → **Two Pointers** `O(N)`
- Valid parentheses → **Stack** `O(N)`
- Count and say → **Simulation** `O(N)`
- Longest common prefix → **Sort + compare ends** `O(N log N)`
- Minimum window substring → **Sliding Window** `O(N)`
- Word break → **DP + HashMap** `O(N²)`
- Decode ways → **DP** `O(N)`
- Zigzag conversion → **Math pattern** `O(N)`
- Rotate string (is rotation?) → **s in (s+s)** `O(N)`
- Implement strStr / indexOf → **KMP** `O(N+M)`
- Wildcard matching → **DP** `O(N*M)`

---

### 11. 🔢 MATH / GCD PROBLEMS

```
GCD Rules:
  gcd(a, 0) = a
  gcd(a, b) = gcd(b, a % b)     TC: O(log min(a,b))
  gcd(a, b, c) = gcd(a, gcd(b, c))

Factors:
  All factors of N → Loop i from 1 to √N  TC: O(√N)
  Perfect square has ODD number of factors

Sum formula: 1+2+...+N = N*(N+1)/2  → Use to find missing number
```

**Interview Questions:**
- GCD of two numbers → **Euclidean** `O(log min(a,b))`
- GCD of array → **Reduce with gcd** `O(N log M)`
- GCD of factorial array → **Answer is min(A)!**
- Max GCD after deleting one element → **Prefix + Postfix GCD** `O(N)`
- All factors of N → **Loop to √N** `O(√N)`
- Missing number in [1..N] → **N*(N+1)/2 - sum** or **XOR** `O(N)`
- Count trailing zeros in N! → **N/5 + N/25 + ...** `O(log N)`

---

### 12. 🧮 2D MATRIX PROBLEMS

```
2D Prefix Sum:
  ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + mat[i][j]
  sum(r1,c1 → r2,c2) = ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]

Sorted Matrix Search: Start top-right corner
  If mat[r][c] > target → move left (c--)
  If mat[r][c] < target → move down (r++)
```

**Interview Questions:**
- Submatrix sum queries → **2D Prefix Sum** `O(NM) build, O(1) query`
- Search in sorted matrix → **Top-right elimination** `O(N+M)`
- Sum of all rectangles → **Contribution technique** `O(N*M)`
- Max sum rectangle → **Kadane's on column sums** `O(N² * M)`
- Rotate image 90° → **Transpose + Reverse rows** `O(N²)`
- Spiral matrix traversal → **Boundary simulation** `O(N*M)`
- Set matrix zeros → **Row/col markers** `O(N*M)`

---

### 13. 📐 ABSOLUTE VALUE / EXPRESSION PROBLEMS

```
Key Insight: |A - B| = max(A-B, B-A)

For K absolute values: |x1|+|x2|+...+|xk|
  Each xi can be ±, giving 2^k combinations.
  But by symmetry: 2^k / 2 = 2^(k-1) unique expressions.

Pattern:
  Maximize |A[i] - A[j]| + |i - j|
  → Split into 4 cases:
    (A[i]+i) - (A[j]+j) → max(X) - min(X)
    (A[i]-i) - (A[j]-j) → max(Y) - min(Y)
  Answer = max of all cases
```

**Interview Questions:**
- Maximize |A[i]-A[j]| + (i-j) → **2 expressions, max-min** `O(N)`
- Maximize |A1[i]-A1[j]| + |A2[i]-A2[j]| + |i-j| → **8 combos → 4 unique** `O(N)`
- Max absolute difference → **±sign expansion** `O(N)`

---

## 💡 FINAL CHEATSHEET: 5-QUESTION FILTER

```
Ask yourself these 5 questions when you see any Array/String problem:

Q1. Is it about a CONTIGUOUS subarray or substring?
    YES → Sliding Window (positive) OR Prefix Sum+Map (with negatives)

Q2. Is array SORTED or can sorting help?
    YES → Two Pointers (pair/triplet) OR Binary Search (find/optimize)

Q3. Is there a FREQUENCY or LOOKUP needed in O(1)?
    YES → HashMap / HashSet / Frequency Array[26]

Q4. Does it say MAXIMIZE or MINIMIZE something?
    YES → Binary Search on Answer Space OR Greedy (sort first)

Q5. Is there a NEXT GREATER/SMALLER or area/histogram?
    YES → Monotonic Stack
```

---

## 🗝️ ONE-LINE RULES TO MEMORIZE

```
1.  Sliding Window  = "Move a frame over array, expand right, shrink left"
2.  Prefix Sum      = "Store running total; use map to find past sums"
3.  Two Pointers    = "Squeeze from both ends on sorted, or race forward together"
4.  Binary Search   = "If answer space is monotonic, halve it each time"
5.  HashMap         = "Trade O(N) space to save O(N²) time"
6.  Kadane's        = "If running sum goes negative, restart from here"
7.  Monotonic Stack = "Kill elements that can never be the answer"
8.  XOR             = "Pairs cancel to zero; lone survivor remains"
9.  Bucket Sort     = "PigeonHole: empty bucket between two = max gap"
10. Dutch Flag      = "Three pointers: low, mid, high — one-pass 3-way sort"
11. Boyer-Moore     = "Majority survives cancellation — vote and counter"
12. Prefix×Postfix  = "What's to the left × what's to the right = contribution"
```

---
*Arrays & Strings Decision Map | SDE Interview Preparation*
