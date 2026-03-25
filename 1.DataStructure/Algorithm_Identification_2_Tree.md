# 🌳 TREES — COMPLETE ALGORITHM DECISION MAP
### SDE Interview Preparation | Pattern Recognition Guide

---

## 🧠 THE GOLDEN RULE OF TREES (Memorize First)

```
Every tree problem = Base Case + Left + Right + Combine

def solve(node):
    if not node:               # Step 1: Base case (return 0 / None / False)
        return 0
    L = solve(node.left)       # Step 2: Recurse left
    R = solve(node.right)      # Step 3: Recurse right
    return combine(node, L, R) # Step 4: Combine result at current node
```

> **The only question is: what do you return and how do you combine?**

---

## 🔍 MASTER DECISION TREE

```
READ THE PROBLEM
│
├─► Which TRAVERSAL ORDER does the problem need?
│       │
│       ├─ Process node BEFORE children     → Pre-Order  (Root → Left → Right)
│       │     Use for: Copy tree, Serialize, Path problems, Print tree
│       │
│       ├─ Process node BETWEEN children    → In-Order   (Left → Root → Right)
│       │     Use for: BST sorted output, Validate BST, Kth smallest in BST
│       │
│       ├─ Process node AFTER children      → Post-Order (Left → Right → Root)
│       │     Use for: Height, Diameter, Delete tree, Subtree problems, LCA
│       │
│       └─ Process level by level           → BFS / Level Order
│             Use for: Level averages, Zigzag, Right/Left view, Connect nodes
│
├─► Is it a BST (Binary Search Tree)?
│       │
│       ├─ Search / Insert / Delete         → O(log N) avg, O(N) worst
│       ├─ Kth smallest                     → In-Order + counter  O(N)
│       ├─ Validate BST                     → DFS with min/max bounds  O(N)
│       ├─ Find LCA in BST                  → Compare values, go left/right  O(H)
│       ├─ Convert BST to sorted list       → In-Order traversal  O(N)
│       └─ Balance a BST                    → In-Order → sorted array → build  O(N)
│
├─► Is it a PATH problem?
│       │
│       ├─ Root-to-leaf path                → DFS + Backtracking (push → check → pop)
│       ├─ Path with target sum             → DFS + Backtracking  O(N)
│       ├─ Max path sum (any node→any)      → Post-Order DFS, track global max  O(N)
│       ├─ Diameter of tree                 → Post-Order, return height  O(N)
│       └─ LCA (Lowest Common Ancestor)     → Post-Order DFS  O(N)
│
├─► Is it a VIEW / LEVEL problem?
│       │
│       ├─ Left View / Right View           → BFS (first/last per level)  O(N)
│       ├─ Top View / Bottom View           → BFS + Horizontal Distance map  O(N)
│       ├─ Boundary Traversal               → Left boundary + Leaves + Right  O(N)
│       ├─ Zigzag Level Order               → BFS + direction flag  O(N)
│       ├─ Level averages / sums            → BFS  O(N)
│       └─ Connect next right pointers      → BFS Level Order  O(N)
│
├─► Is it a CONSTRUCTION / MODIFICATION problem?
│       │
│       ├─ Build tree from Pre + In order   → Divide & Conquer + HashMap  O(N)
│       ├─ Build tree from Post + In order  → Divide & Conquer + HashMap  O(N)
│       ├─ Flatten tree to linked list      → Post-Order DFS  O(N)
│       ├─ Invert / Mirror tree             → Post-Order (swap L and R)  O(N)
│       ├─ Generate all unique BSTs [1..N]  → Divide & Conquer  O(Catalan N)
│       └─ Serialize / Deserialize          → Pre-Order DFS or BFS  O(N)
│
├─► Is it a COMPARISON problem?
│       │
│       ├─ Are two trees identical?         → DFS both simultaneously  O(N)
│       ├─ Is tree symmetric / mirror?      → DFS compare L-left with R-right  O(N)
│       ├─ Is S a subtree of T?             → DFS + identical check  O(M*N)
│       └─ Isomorphic trees?               → DFS with swap check  O(N)
│
├─► Is it a SPECIAL TRAVERSAL problem?
│       │
│       ├─ O(1) space traversal             → Morris Traversal  O(N), O(1)
│       ├─ Multiple range queries on tree   → Euler Tour + Segment Tree  O(N + Q log N)
│       ├─ Nodes at distance K from target  → Parent map + DFS  O(N)
│       └─ Vertical order traversal         → BFS + Horizontal Distance  O(N log N)
│
└─► Is it a PROPERTY CHECK problem?
        │
        ├─ Is it balanced?                  → Post-Order, return (bool, height)  O(N)
        ├─ Is it a valid BST?               → DFS with min/max  O(N)
        ├─ Is it a complete binary tree?    → BFS, check for null gaps  O(N)
        ├─ Count nodes in complete tree     → Binary Search on levels  O(log²N)
        └─ Find largest BST subtree         → Post-Order (size, min, max, is_bst)  O(N)
```

---

## 🧩 TRAVERSAL CHEATSHEET

```
┌─────────────────┬────────────────────────────┬───────────────────────────────────────────┐
│ Traversal       │ Order                      │ When to Use (Memory Hook)                 │
├─────────────────┼────────────────────────────┼───────────────────────────────────────────┤
│ Pre-Order       │ Root → Left → Right        │ "Read top-down" → Serialize, Copy, Paths  │
│ In-Order        │ Left → Root → Right        │ "BST = Sorted" → BST problems, Kth small  │
│ Post-Order      │ Left → Right → Root        │ "Children first" → Height, LCA, Diameter  │
│ Level-Order BFS │ Level by level (Queue)     │ "Layer cake" → Views, Connect, Zigzag     │
│ Morris          │ In-Order, O(1) space       │ "No stack allowed" → space-critical       │
│ Euler Tour      │ Node visited 3× (in DFS)   │ "Multiple queries" → LCA, Subtree queries │
└─────────────────┴────────────────────────────┴───────────────────────────────────────────┘
```

**Mnemonic for traversal output:**
```
Tree:         1
             / \
            2   3
           / \   \
          4   5   6

Pre-Order  → 1 2 4 5 3 6    (Root First   — "Print before going")
In-Order   → 4 2 5 1 3 6    (Left First   — "BST sorted output")
Post-Order → 4 5 2 6 3 1    (Root Last    — "Children report to parent")
Level-Order→ 1 2 3 4 5 6    (BFS          — "Floor by floor")
```

---

## ⚡ KEYWORD → ALGORITHM TRIGGER TABLE

| You See This Keyword | Algorithm | Traversal | Time |
|---|---|---|---|
| height / depth of tree | Post-Order DFS | Post | O(N) |
| diameter of tree | Post-Order, return height | Post | O(N) |
| balanced tree check | Post-Order, return (bool, height) | Post | O(N) |
| mirror / invert / flip | Swap L↔R post-order | Post | O(N) |
| path sum root to leaf | DFS backtracking | Pre | O(N) |
| all root-to-leaf paths | DFS backtracking | Pre | O(N) |
| max path sum any node | Post-Order + global max | Post | O(N) |
| LCA (binary tree) | Post-Order return node | Post | O(N) |
| LCA (BST) | Compare values, no recursion | — | O(H) |
| kth smallest (BST) | In-Order + counter | In | O(N) |
| validate BST | DFS with min/max bounds | Pre | O(N) |
| sorted output from BST | In-Order traversal | In | O(N) |
| BST to sorted linked list | In-Order, rewire pointers | In | O(N) |
| recover swapped BST nodes | In-Order, find violations | In | O(N) |
| build tree from pre+in | Divide & Conquer + map | — | O(N) |
| build tree from post+in | Divide & Conquer + map | — | O(N) |
| serialize / deserialize | Pre-Order DFS or BFS | Pre/BFS | O(N) |
| flatten to linked list | Post-Order DFS | Post | O(N) |
| identical trees | DFS both at once | Pre | O(N) |
| symmetric / mirror tree | DFS compare outer-inner | Pre | O(N) |
| subtree check | DFS + identical subcheck | Pre | O(M*N) |
| isomorphic trees | DFS with swap variant | Pre | O(N) |
| left view / right view | BFS (first/last per level) | BFS | O(N) |
| top view | BFS + HD map (first per HD) | BFS | O(N) |
| bottom view | BFS + HD map (last per HD) | BFS | O(N) |
| zigzag / spiral traversal | BFS + direction flip | BFS | O(N) |
| boundary traversal | Left bound + leaves + right | DFS | O(N) |
| vertical order traversal | BFS + HD tracking | BFS | O(N log N) |
| level averages / level sums | BFS, sum per level | BFS | O(N) |
| connect next right pointers | BFS Level-Order | BFS | O(N) |
| nodes at distance K | Parent map + DFS | DFS | O(N) |
| count nodes complete tree | Binary search on levels | — | O(log²N) |
| largest BST subtree | Post-Order (size,min,max) | Post | O(N) |
| O(1) space traversal | Morris Traversal | In | O(N) |
| multiple subtree queries | Euler Tour + Sparse Table | — | O(N + Q logN) |
| all unique BSTs [1..N] | Divide & Conquer | — | O(Catalan N) |
| count unique BSTs [1..N] | DP (Catalan number) | — | O(N²) |
| kth largest in BST (queries) | Data augmentation (sizes) | Post | O(N) build, O(H) query |
| cameras to cover tree | Post-Order greedy (0/1/2) | Post | O(N) |
| sum of subtrees | Post-Order, return sum | Post | O(N) |
| equal sum subtrees | Post-Order + HashMap | Post | O(N) |

---

## 📊 ALGORITHM COMPLEXITY REFERENCE

```
┌───────────────────────────────────┬──────────────────┬────────────┬──────────────────────────────┐
│ Algorithm / Pattern               │ Time Complexity  │ Space      │ Key Condition                │
├───────────────────────────────────┼──────────────────┼────────────┼──────────────────────────────┤
│ DFS (any traversal)               │ O(N)             │ O(H)       │ H = height (O(logN) balanced)│
│ BFS / Level-Order                 │ O(N)             │ O(W)       │ W = max width of tree        │
│ BST Search / Insert / Delete      │ O(H)             │ O(H)       │ O(logN) balanced, O(N) worst │
│ Morris Traversal                  │ O(N)             │ O(1)       │ No recursion stack needed    │
│ Build tree (pre+in or post+in)    │ O(N)             │ O(N)       │ HashMap for O(1) index lookup│
│ LCA (Binary Tree)                 │ O(N)             │ O(H)       │ Post-Order DFS               │
│ LCA (BST)                         │ O(H)             │ O(H)       │ No extra space for BST       │
│ Diameter                          │ O(N)             │ O(H)       │ Combined with height         │
│ Balanced check                    │ O(N)             │ O(H)       │ Return (bool, height) pair   │
│ Serialize / Deserialize           │ O(N)             │ O(N)       │ Pre-order or BFS             │
│ Vertical / Top / Bottom view      │ O(N log N)       │ O(N)       │ BFS + sorted HD map          │
│ Count nodes (complete tree)       │ O(log²N)         │ O(log N)   │ Binary search on last level  │
│ Euler Tour (build)                │ O(N)             │ O(N)       │ Flatten for range queries    │
│ Euler Tour + Sparse Table (query) │ O(1) per query   │ O(N log N) │ After O(N log N) build       │
│ Data Augmentation (kth in BST)    │ O(N) build       │ O(N)       │ Store subtree sizes          │
│                                   │ O(H) per query   │            │                              │
│ Generate all BSTs [1..N]          │ O(Catalan(N))    │ O(Catalan) │ Divide & Conquer all roots   │
│ Count BSTs [1..N] (DP)            │ O(N²)            │ O(N)       │ Catalan number formula       │
│ Largest BST subtree               │ O(N)             │ O(H)       │ Post-Order (size,min,max)    │
│ Subtree check (S in T)            │ O(M × N)         │ O(H)       │ DFS + identical at each node │
│ Max path sum                      │ O(N)             │ O(H)       │ Global max + local max       │
│ Tree cameras (min cover)          │ O(N)             │ O(H)       │ Post-Order greedy 3-states   │
│ Nodes at distance K               │ O(N)             │ O(N)       │ Parent map + BFS/DFS         │
└───────────────────────────────────┴──────────────────┴────────────┴──────────────────────────────┘

Note: H = tree height. For balanced tree: H = O(log N). For skewed tree: H = O(N).
      W = tree width. For perfect binary tree: W = O(N/2) at last level.
```

---

## 🎯 QUESTION TYPE → ALGORITHM MAP (By Category)

---

### 1. 📏 HEIGHT & DEPTH PROBLEMS

```
Pattern: Post-Order — children report their heights to parent
Template: return 1 + max(left_height, right_height)

MNEMONIC: "Height flows UP — children tell parent"
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| Height of binary tree | Post-Order DFS | O(N) |
| Diameter of tree (max edge path) | Post-Order, return height | O(N) |
| Balanced tree check | Post-Order, return (bool, height) | O(N) |
| Minimum depth (root to nearest leaf) | BFS (stops at first leaf) | O(N) |
| Maximum width of tree (level) | BFS, track level size | O(N) |
| Count nodes in complete binary tree | Binary search on levels | O(log²N) |

---

### 2. 🛣️ PATH PROBLEMS

```
Pattern: DFS + Backtracking — "Push when going down, Pop when coming up"
Template:
    path.append(node.val)      # Push
    if leaf: record answer
    dfs(left) / dfs(right)
    path.pop()                 # Pop (backtrack)

For max sum paths: Post-Order — return best single-branch sum up, track global max.

MNEMONIC: "Path = Append → Recurse → Pop  (ARP)"
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| Root-to-leaf path with target sum | DFS + backtracking | O(N) |
| All root-to-leaf paths | DFS + backtracking | O(N) |
| Path sum exists? | DFS, subtract target | O(N) |
| Max path sum (any → any) | Post-Order + global max | O(N) |
| Diameter of tree | Post-Order (path = L height + R height) | O(N) |
| Path from root to node | DFS + backtrack | O(N) |
| Sum of all root-to-leaf numbers | DFS, carry running number | O(N) |
| Longest path of same value | Post-Order, compare val | O(N) |

---

### 3. 🔍 LCA (Lowest Common Ancestor)

```
Pattern: Post-Order DFS — "If found p or q, bubble it up"

Binary Tree:
    if node == p or node == q: return node
    L = lca(left), R = lca(right)
    if L and R: return node  (node IS the LCA)
    return L or R

BST (Faster — O(H)):
    if both < root: go left
    if both > root: go right
    else: root IS the LCA

MNEMONIC: "LCA = where paths from p and q first meet"
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| LCA of two nodes (Binary Tree) | Post-Order DFS | O(N) |
| LCA of two nodes (BST) | Compare & navigate | O(H) |
| Distance between two nodes | LCA + depths | O(N) |
| Nodes at distance K from target | Parent map + BFS | O(N) |

---

### 4. 👁️ VIEW PROBLEMS

```
All view problems use BFS + Level tracking, except Boundary.

Horizontal Distance (HD):
    root = 0, go left = HD-1, go right = HD+1

Left View   → BFS: First node at each level
Right View  → BFS: Last node at each level
Top View    → BFS + HD: First node at each HD
Bottom View → BFS + HD: Last node at each HD (overwrite)
Vertical    → BFS + HD: All nodes grouped by HD

Boundary    → Left bound (no leaves) + All leaves + Right bound reversed

MNEMONIC: "Views = BFS + HD (except Boundary = 3 parts)"
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| Left view | BFS, first node per level | O(N) |
| Right view | BFS, last node per level | O(N) |
| Top view | BFS + HD map, first at each HD | O(N) |
| Bottom view | BFS + HD map, last at each HD | O(N) |
| Vertical order traversal | BFS + HD + sorted | O(N log N) |
| Boundary traversal | Left + Leaves + Right reverse | O(N) |
| Zigzag / Spiral level order | BFS + flip direction | O(N) |
| Level order (list of levels) | BFS, collect per level | O(N) |
| Level averages | BFS, avg per level | O(N) |

---

### 5. 🌲 BST SPECIFIC PROBLEMS

```
BST Key Property:
    In-Order gives SORTED sequence
    Left < Root < Right at every node
    Search = O(H), not O(N) like plain tree

MNEMONIC: "BST = Binary Sorted Tree — In-Order = sorted"

Key BST Patterns:
    Need sorted output?          → In-Order
    Need to find/compare?        → Use BST property (go L or R)
    Need to validate?            → DFS with (min, max) bounds
    Need to balance?             → In-Order → array → build mid
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| Validate BST | DFS with (min, max) bounds | O(N) |
| Kth smallest in BST | In-Order + counter | O(N) |
| Kth smallest (with many queries) | Data augmentation (sizes) | O(H) per query |
| Floor / Ceil in BST | Navigate BST | O(H) |
| Insert in BST | Navigate + create | O(H) |
| Delete from BST | Find inorder successor | O(H) |
| LCA in BST | Compare both < or > root | O(H) |
| Convert BST to sorted array | In-Order traversal | O(N) |
| Convert BST to doubly linked list | In-Order, rewire prev/next | O(N) |
| Recover BST (two swapped nodes) | In-Order, find 2 violations | O(N) |
| Balance a BST | In-Order → build mid-pivot | O(N) |
| Largest BST subtree | Post-Order (size, min, max, valid) | O(N) |
| Merge two BSTs | In-Order both → merge → build | O(M+N) |
| Count BSTs with N keys | DP (Catalan numbers) | O(N²) |
| Generate all unique BSTs | Divide & Conquer | O(Catalan(N)) |

---

### 6. 🏗️ CONSTRUCTION PROBLEMS

```
Build tree from Pre-Order + In-Order:
    Rule: First in Pre-Order = Root
          Find root in In-Order → left part = left subtree, right = right subtree
    Optimization: HashMap for In-Order indices → O(N) total

Build tree from Post-Order + In-Order:
    Rule: Last in Post-Order = Root
          Same split in In-Order

MNEMONIC: "Pre → first is root. Post → last is root. In → splits L and R."
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| Build tree from Pre+In order | D&C + HashMap | O(N) |
| Build tree from Post+In order | D&C + HashMap | O(N) |
| Serialize binary tree | Pre-Order DFS (mark nulls) | O(N) |
| Deserialize binary tree | Pre-Order DFS with queue | O(N) |
| Flatten tree to linked list | Post-Order, rearrange pointers | O(N) |
| Invert / Mirror tree | Post-Order, swap children | O(N) |
| Complete tree from array | BFS level by level | O(N) |

---

### 7. 🔁 COMPARISON PROBLEMS

```
Template for comparing TWO trees simultaneously:
    def compare(n1, n2):
        if not n1 and not n2: return True    # Both null
        if not n1 or not n2: return False    # One null
        if n1.val != n2.val: return False    # Values differ
        return compare(n1.left, n2.left) and compare(n1.right, n2.right)

For Isomorphic: allow swapping left/right children
For Symmetric: compare outer with outer, inner with inner

MNEMONIC: "Two-tree problems = run DFS on both simultaneously"
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| Identical trees | DFS both simultaneously | O(N) |
| Symmetric / mirror tree | DFS, compare outer↔inner | O(N) |
| Is S a subtree of T? | DFS T + identical(S, subtree) | O(M×N) |
| Isomorphic trees | DFS with or without swap | O(N) |
| Leaf-similar trees | DFS both, collect leaves | O(N) |

---

### 8. 🔧 SPECIAL / ADVANCED PATTERNS

```
Morris Traversal — O(1) space In-Order:
    Use RIGHT pointers of leaf nodes as "threads"
    Create thread → go left → remove thread → process → go right
    Use when: "Traverse without extra memory"

Euler Tour — for multiple queries:
    Visit each node 3 times (enter, middle, exit)
    Flatten tree → use prefix structures for range queries
    Use when: "Multiple subtree queries, LCA offline"

Data Augmentation — store extra info in nodes:
    Store subtree sizes, heights, etc. during build
    Use when: "Kth queries, rank queries"

Divide & Conquer — generate all structures:
    For each value as root → recurse left and right
    Use when: "Generate all possible trees"
```

**Interview Questions:**

| Question | Algorithm | Time |
|---|---|---|
| In-Order without recursion/stack | Morris Traversal | O(N), O(1) |
| Kth smallest (many queries) | Morris / Data augmentation | O(N) / O(H) |
| Subtree sum / max queries | Euler Tour + prefix sums | O(1) per query |
| LCA offline (many queries) | Euler Tour + RMQ | O(N log N + Q) |
| Nodes at distance K from node | Parent map DFS | O(N) |
| Min cameras to cover all nodes | Post-Order greedy (3 states) | O(N) |
| Binary tree to BST (same shape) | In-Order collect → sort → refill | O(N log N) |
| Sum of subtrees with equal sum | Post-Order + HashMap | O(N) |
| Duplicate subtrees | Post-Order + serialization map | O(N) |

---

## 💡 WHEN TO USE WHICH TRAVERSAL — ONE-LINE RULES

```
Pre-Order  → "I act on myself BEFORE sending kids to work"
             → Used for: COPY, SERIALIZE, PATH building (top-down)

In-Order   → "I act on myself BETWEEN left and right"
             → Used for: BST SORTED output, VALIDATE BST, Kth smallest

Post-Order → "I wait for BOTH kids to report, THEN I act"
             → Used for: HEIGHT, BALANCE, DIAMETER, LCA, DELETE, SUBTREE SUM

BFS        → "I process my entire FLOOR before going deeper"
             → Used for: LEVEL problems, VIEWS, CONNECT nodes, SHORTEST path

Morris     → "I borrow RIGHT pointers of predecessors as threads"
             → Used for: O(1) SPACE traversal

Euler Tour → "I visit every node THREE times for fast range queries"
             → Used for: MULTIPLE QUERIES on subtrees, offline LCA
```

---

## 🗝️ PATTERN RECOGNITION: 5-QUESTION FILTER

```
Ask these 5 questions when you see any Tree problem:

Q1. Is it a BST?
    YES → Use BST property to navigate (go L or R). In-Order = sorted.
    NO  → Treat as generic tree with DFS/BFS.

Q2. Does it involve a PATH?
    YES → DFS + Backtracking (push/pop) for root-leaf paths
          Post-Order + global max for any-to-any paths

Q3. Does it involve a LEVEL or VIEW?
    YES → BFS + Level tracking
          Top/Bottom view → add Horizontal Distance (HD)

Q4. Do you need to COMBINE results from left and right children?
    YES → Post-Order (children compute first, then combine at parent)
          Examples: Height, Diameter, LCA, Balance check

Q5. Is it a BST problem needing SORTED behavior?
    YES → In-Order traversal (gives sorted sequence for free)
```

---

## 🧠 MNEMONICS SUMMARY TABLE

| Problem Type | Mnemonic | Traversal |
|---|---|---|
| Height / Diameter | **"Children report to parent"** | Post-Order |
| Path sum / All paths | **"ARP — Append, Recurse, Pop"** | Pre-Order DFS |
| LCA | **"Where p and q paths first meet"** | Post-Order |
| BST = sorted | **"In-Order = BST's sorted soul"** | In-Order |
| Validate BST | **"Pass the min-max baton down"** | Pre-Order |
| Views | **"BFS + HD = any view"** | BFS |
| Boundary | **"Left wall + floor + right wall (reversed)"** | Mixed DFS |
| Build from traversals | **"Pre→first, Post→last, In→splits"** | D&C |
| Serialize | **"Pre-Order + mark nulls = blueprint"** | Pre-Order |
| Subtree problems | **"Children compute, parent combines"** | Post-Order |
| O(1) space | **"Morris steals predecessor's right pointer"** | In-Order |
| Multi-queries | **"Euler flattens tree for fast answers"** | DFS (3x visit) |

---

## 🏆 TOP INTERVIEW QUESTIONS QUICK-REFERENCE

```
EASY
├─ Inorder / Preorder / Postorder traversal (recursive + iterative)
├─ Height of tree
├─ Invert / Mirror binary tree
├─ Symmetric tree
├─ Level order traversal
├─ Check if tree is balanced
└─ Diameter of binary tree

MEDIUM
├─ Validate BST
├─ Lowest Common Ancestor (Binary Tree + BST)
├─ Path sum (all paths, print them)
├─ Binary tree right side view
├─ Construct tree from Pre+In order
├─ Serialize and Deserialize
├─ Flatten binary tree to linked list
├─ Max path sum in binary tree
├─ Kth smallest in BST
├─ Top/Bottom/Left/Right view
├─ Boundary traversal
├─ Zigzag level order traversal
├─ Count nodes in complete binary tree
├─ Recover BST (two swapped nodes)
├─ Binary tree to doubly linked list
└─ Nodes at distance K from target

HARD
├─ Binary tree cameras (minimum cover)
├─ Serialize/Deserialize N-ary tree
├─ Vertical order traversal
├─ Maximum path sum (any to any)
├─ Largest BST subtree
├─ Generate all unique BSTs
├─ Euler tour + LCA offline
└─ Data augmented BST (Kth with Q queries)
```

---

## ⚠️ COMMON EDGE CASES (Always Check)

```
1. Empty tree (root is None)        → Base case returns 0 / None / False
2. Single node tree                 → Leaf node: left=None, right=None
3. Skewed tree (like a linked list) → Height = N, space = O(N) not O(logN)
4. Tree with all same values        → BST validation fails without strict bounds
5. Path going through root          → Max path sum can include negative nodes
6. LCA when one node is ancestor    → node itself is LCA
7. BST with duplicate values        → Clarify: duplicates go left or right?
```

---
*Trees Algorithm Decision Map | SDE Interview Preparation*
