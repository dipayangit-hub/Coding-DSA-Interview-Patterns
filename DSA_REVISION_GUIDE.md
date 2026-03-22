# DSA Quick Revision Guide

## 1. **Two Pointers**
**What it does:** Use two pointers moving from different ends to solve problems efficiently.

**Key Operations:**
- Start with `left=0, right=len(arr)-1`
- Move pointers based on conditions
- Common for sorted arrays, linked lists

**Python Examples:**
```python
# Two Sum (sorted array)
def twosum(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            return [l + 1, r + 1]
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1
    return []

# Remove Duplicates (in-place)
def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[j-1]:
            nums[j] = nums[i]
            j += 1
    return j

# Max Area (Container with Most Water)
def maxArea(height):
    i, j = 0, len(height) - 1
    area = 0
    while i < j:
        area = max(area, (j - i) * (min(height[i], height[j])))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return area
```

**When to Use:**
- Sorted arrays/lists
- Need to find pairs or triplets
- Minimize/maximize something

**Repository:** `TwoPointersProblem.py`

---

## 2. **Fast and Slow Pointers**
**What it does:** Two pointers move at different speeds to detect cycles or find middle elements.

**Key Operations:**
- `slow` moves 1 step: `slow = slow.next`
- `fast` moves 2 steps: `fast = fast.next.next`
- Detect when they meet (cycle found)

**Python Examples:**
```python
# Detect Cycle in Linked List
def hasCycle(head):
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Find Cycle Start
def detectCycle(head):
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

# Happy Number (uses sums, not pointers)
def isHappy(n):
    def sq(n):
        ans = 0
        while n > 0:
            r = n % 10
            n //= 10
            ans += r * r
        return ans
    slow, fast = sq(n), sq(sq(n))
    while slow != fast and slow != 1 and fast != 1:
        slow = sq(slow)
        fast = sq(sq(fast))
    return slow == 1 or fast == 1
```

**When to Use:**
- Detect cycles in linked lists
- Find middle of linked list
- Find duplicate in array

**Repository:** `FastandSlowPointers.py`, `Slowandfastpointers.py`

---

## 3. **Sliding Window**
**What it does:** Maintain a window of elements that slide through the array to solve substring/subarray problems.

**Key Operations:**
- Expand window by moving `right` pointer
- Shrink window by moving `left` pointer
- Update result as you go

**Python Examples:**
```python
# Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    left = 0
    maxLen = 0
    visited = set()
    for right in range(len(s)):
        while visited.__contains__(s[right]):
            visited.remove(s[left])
            left += 1
        visited.add(s[right])
        maxLen = max(maxLen, right - left + 1)
    return maxLen

# Minimum Subarray Length
def minSubArrayLen(target, nums):
    left = 0
    sum_val = 0
    minsize = float('inf')
    for right in range(len(nums)):
        sum_val += nums[right]
        while sum_val >= target:
            minsize = min(minsize, right - left + 1)
            sum_val -= nums[left]
            left += 1
    return 0 if minsize == float('inf') else minsize

# Maximum Sum Subarray with K Distinct Elements
def maximumSubarraySum(nums, k):
    left, sum_val = 0, 0
    maxsum = 0
    visited = set()
    for right in range(len(nums)):
        while visited.__contains__(nums[right]) or len(visited) == k:
            visited.remove(nums[left])
            sum_val -= nums[left]
            left += 1
        sum_val += nums[right]
        visited.add(nums[right])
        if len(visited) == k:
            maxsum = max(maxsum, sum_val)
    return maxsum
```

**When to Use:**
- Find substring/subarray with certain properties
- Optimize brute force O(n²) to O(n)
- Pattern: expanding and contracting window

**Repository:** `SlidingWindow.py`

---

## 4. **Prefix Sum**
**What it does:** Precompute cumulative sums to answer range queries in O(1) time.

**Key Operations:**
- Build prefix array: `prefix[i] = prefix[i-1] + arr[i]`
- Query sum in range: `sum(l, r) = prefix[r] - prefix[l-1]`
- Use hashmap to find subarrays with specific sum

**Python Examples:**
```python
# Pivot Index (left sum equals right sum)
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        right = total - left - nums[i]
        if left == right:
            return i
        left += nums[i]
    return -1

# Subarray Sum = K (count subarrays)
def subarraySum(nums, k):
    map_dict = {}
    sum_val, count = 0, 0
    map_dict[0] = 1
    for i in range(len(nums)):
        sum_val += nums[i]
        if sum_val - k in map_dict:
            count += map_dict[sum_val - k]
        map_dict[sum_val] = map_dict.get(sum_val, 0) + 1
    return count

# Subarray Sum Divisible by K
def checkSubarraySum(nums, k):
    map_dict = {}
    sum_val = 0
    map_dict[0] = -1
    for i in range(len(nums)):
        sum_val += nums[i]
        rem = sum_val % k
        if rem in map_dict:
            if i - map_dict[rem] > 1:
                return True
        else:
            map_dict[rem] = i
    return False
```

**When to Use:**
- Range sum queries
- Find subarrays with specific sum property
- Optimize from O(n²) to O(n) with hashmap

**Repository:** `PrefixSum.py`

---

## 5. **Merge Intervals**
**What it does:** Combine overlapping intervals efficiently.

**Key Operations:**
- Sort intervals by start time
- Check if current overlaps with previous
- Merge if overlapping, add new interval otherwise

**Python Examples:**
```python
# Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda l: l[0])
    res = [intervals[0]]
    e = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[e][1]:
            res[e][1] = max(res[e][1], intervals[i][1])
        else:
            e += 1
            res.append(intervals[i])
    return res

# Insert Interval
def insert(intervals, newInterval):
    res = []
    i = 0
    # Add all intervals that end before new interval starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    # Add remaining intervals
    while i < len(intervals):
        res.append(intervals[i])
        i += 1
    return res

# Maximum Non-Overlapping Intervals
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```

**When to Use:**
- Overlapping ranges
- Scheduling problems
- Activity selection

**Repository:** `MergeIntervals.py`

---

## 6. **Binary Search**
**What it does:** Efficiently search in sorted arrays by halving the search space.

**Key Operations:**
- Maintain `left` and `right` pointers
- Calculate `mid = (left + right) // 2`
- Adjust pointers based on comparison

**Python Examples:**
```python
# Basic Binary Search
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Search in 2D Matrix
def searchMatrix(matrix, target):
    left, right = 0, len(matrix) * len(matrix[0]) - 1
    m, n = len(matrix), len(matrix[0])
    while left <= right:
        mid = (left + right) // 2
        r, c = mid // n, mid % n
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Search in Rotated Sorted Array
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:  # Left side sorted
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right side sorted
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Ship Within Days (decision problem)
def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if canShip(weights, days, mid):
            right = mid
        else:
            left = mid + 1
    return left

def canShip(weights, days, capacity):
    daycount = 1
    current_sum = 0
    for w in weights:
        if current_sum + w > capacity:
            daycount += 1
            current_sum = 0
        current_sum += w
    return daycount <= days
```

**When to Use:**
- Sorted array search
- Decision problems (can we do it? → minimize/maximize)
- O(log n) time complexity

**Repository:** `BinarySearch.py`

---

## 7. **Dictionary/HashMap**
**What it does:** Fast key-value lookups in O(1) average time.

**Key Operations:**
- Store and retrieve: `map[key] = value`
- Check existence: `if key in map`
- Count frequencies: `map[key] = map.get(key, 0) + 1`

**Python Examples:**
```python
# Word Pattern
def wordPattern(pattern, s):
    map_dict = {}
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in map_dict:
            if words[i] in map_dict.values():
                return False
            map_dict[pattern[i]] = words[i]
        else:
            if map_dict[pattern[i]] != words[i]:
                return False
    return True

# Anagram Checking
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freq_map = {}
    for c in s:
        freq_map[c] = freq_map.get(c, 0) + 1
    for c in t:
        if c not in freq_map or freq_map[c] == 0:
            return False
        freq_map[c] -= 1
    return True

# Group Anagrams
def groupAnagrams(strs):
    map_dict = {}
    for word in strs:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        key = tuple(freq)
        if key in map_dict:
            map_dict[key].append(word)
        else:
            map_dict[key] = [word]
    return list(map_dict.values())
```

**When to Use:**
- Frequency counting
- Pattern matching
- Memoization in DP
- Two-pass problems

**Repository:** `Hashmaps.py`

---

## 8. **Stack**
**What it does:** LIFO (Last In First Out) data structure for tracking state and backtracking.

**Key Operations:**
- Push: `stack.append(x)`
- Pop: `stack.pop()`
- Peek: `stack[-1]`

**Python Examples:**
```python
# Valid Parentheses
def isValid(s):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            j = closing.index(char)
            if len(stack) == 0 or stack[-1] != opening[j]:
                return False
            stack.pop()
    return len(stack) == 0

# Next Greater Element
def nextGreaterElement(nums1, nums2):
    stack = []
    map_dict = {}
    for i in nums2:
        while len(stack) > 0 and stack[-1] < i:
            map_dict[stack.pop()] = i
        stack.append(i)
        if i not in map_dict:
            map_dict[i] = -1
    return [map_dict[i] for i in nums1]

# Simplify Path
def simplifyPath(path):
    stack = []
    words = path.split('/')
    for word in words:
        if word == "" or word == ".":
            continue
        elif word == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(word)
    return "/" + "/".join(stack) if stack else "/"
```

**When to Use:**
- Parentheses matching
- Expression evaluation
- DFS traversal
- Undo/redo functionality

**Repository:** `Stacks.py`

---

## 9. **Queue**
**What it does:** FIFO (First In First Out) data structure for BFS and level-order traversal.

**Key Operations:**
- Enqueue: `queue.append(x)`
- Dequeue: `queue.popleft()`
- Use `from collections import deque` for O(1) operations

**Python Examples:**
```python
from collections import deque

# Implement Queue using 2 Stacks
class MyQueue:
    def __init__(self):
        self.st1 = []  # For push
        self.st2 = []  # For pop

    def push(self, x):
        self.st1.append(x)

    def pop(self):
        if len(self.st2) == 0:
            while len(self.st1) > 0:
                self.st2.append(self.st1.pop())
        return self.st2.pop()

    def peek(self):
        if len(self.st2) == 0:
            while len(self.st1) > 0:
                self.st2.append(self.st1.pop())
        return self.st2[-1]

# Level Order Traversal (BFS)
def levelOrder(root):
    queue = deque()
    res = []
    if root is None:
        return res
    queue.append(root)
    res.append([root.val])
    while len(queue) > 0:
        temp = []
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                temp.append(node.left.val)
            if node.right:
                queue.append(node.right)
                temp.append(node.right.val)
        if temp:
            res.append(temp)
    return res
```

**When to Use:**
- BFS traversal
- Level-order tree traversal
- Producer-consumer problems
- Multi-source BFS

**Repository:** `Queues.py`

---

## 10. **Heaps**
**What it does:** Efficient priority queue for finding min/max elements quickly.

**Key Operations:**
- `import heapq` (min-heap by default)
- Push: `heapq.heappush(heap, x)`
- Pop: `heapq.heappop(heap)`
- For max-heap: push negative values `-x`

**Python Examples:**
```python
import heapq

# Kth Largest Element
def findKthLargest(nums, k):
    pq = []
    for i in nums:
        heapq.heappush(pq, i)
        if len(pq) > k:
            heapq.heappop(pq)
    return pq[0]

# Top K Frequent Elements
def topKFrequent(nums, k):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    pq = []
    for num, freq in freq_map.items():
        heapq.heappush(pq, (freq, num))
        if len(pq) > k:
            heapq.heappop(pq)
    return [num for freq, num in pq]

# Custom Comparator
class HeapKey:
    def __init__(self, key, ref_dict):
        self.key = key
        self.ref_dict = ref_dict

    def __lt__(self, other):
        return self.ref_dict[self.key] < self.ref_dict[other.key]
```

**When to Use:**
- Find Kth largest/smallest
- Merge K sorted lists
- Schedule tasks by priority
- Huffman coding

**Repository:** `Heaps.py`

---

## 11. **Tree**
**What it does:** Hierarchical data structure for representing relationships.

**Key Operations:**
- Traverse (in-order, pre-order, post-order)
- DFS recursion
- Level-order with queue

**Python Examples:**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Max Depth
def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# Same Tree
def isSameTree(p, q):
    if q is None and p is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Symmetric Tree (Iterative)
def isSymmetric(root):
    from collections import deque
    queue = deque()
    if root:
        queue.append((root.left, root.right))
    while queue:
        p, q = queue.popleft()
        if p is None and q is None:
            continue
        if p is None or q is None or p.val != q.val:
            return False
        queue.append((p.left, q.right))
        queue.append((p.right, q.left))
    return True
```

**When to Use:**
- Hierarchical data
- Binary search trees
- Expression trees
- File systems

**Repository:** `Trees.py`

---

## 12. **Graph**
**What it does:** Represents connections between nodes/vertices.

**Key Operations:**
- DFS: recursive traversal
- BFS: level-order traversal with queue
- Adjacency matrix or list representation

**Python Examples:**
```python
from collections import deque

# Create Adjacency List
def create_adj_list():
    v = 3
    adj = [[] for _ in range(v)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    return adj

# Flood Fill (DFS)
def floodFill(image, sr, sc, color):
    oldcolor = image[sr][sc]
    if oldcolor != color:
        dfs(image, sr, sc, len(image), len(image[0]), color, oldcolor)
    return image

def dfs(image, sr, sc, rows, cols, newcolor, oldcolor):
    if sr < 0 or sc < 0 or sr >= rows or sc >= cols or image[sr][sc] != oldcolor:
        return
    image[sr][sc] = newcolor
    dfs(image, sr-1, sc, rows, cols, newcolor, oldcolor)  # Up
    dfs(image, sr+1, sc, rows, cols, newcolor, oldcolor)  # Down
    dfs(image, sr, sc-1, rows, cols, newcolor, oldcolor)  # Left
    dfs(image, sr, sc+1, rows, cols, newcolor, oldcolor)  # Right

# Oranges Rotting (Multi-source BFS)
def orangesRotting(grid):
    queue = deque()
    m, n = len(grid), len(grid[0])
    fresh_count = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                queue.append([r, c])
            elif grid[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0
    if len(queue) == 0:
        return -1

    time = -1
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while queue:
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append([nr, nc])
                    fresh_count -= 1
        time += 1

    return time if fresh_count == 0 else -1
```

**When to Use:**
- Social networks
- Web crawling
- Game maps
- Dependencies resolution

**Repository:** `Graphs.py`, `BFS.py`, `DFS.py`

---

## 13. **Trie**
**What it does:** Prefix tree for efficient string search and autocomplete.

**Key Operations:**
- Insert: traverse/create path for each character
- Search: verify full word exists
- StartsWith: check prefix existence

**Python Examples:**
```python
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
        node.isEnd = True
        node.word = word

    def search(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if node.children[index]:
                node = node.children[index]
            else:
                return False
        return node.isEnd

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if node.children[index]:
                node = node.children[index]
            else:
                return False
        return True

    def getSuggestions(self, prefix):
        node = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if node.children[index]:
                node = node.children[index]
            else:
                return []

        res = []
        def dfs(node):
            if node.isEnd:
                res.append(node.word)
            for child in node.children:
                if child:
                    dfs(child)

        dfs(node)
        return res
```

**When to Use:**
- Autocomplete
- Spell checker
- IP routing
- Dictionary implementation

**Repository:** `Trie.py`

---

## 14. **Greedy Algorithms**
**What it does:** Make locally optimal choices to find global optimum.

**Key Operations:**
- Sort by relevant criteria
- Make greedy choice at each step
- Verify it leads to optimal solution

**Python Examples:**
```python
# Can Jump (Jump Game)
def canJump(nums):
    maxjump = 0
    for i in range(len(nums)):
        if maxjump < i:
            return False
        maxjump = max(maxjump, nums[i] + i)
        if maxjump >= len(nums) - 1:
            return True
    return True

# Jump Game II (Minimum jumps)
def jump(nums):
    if len(nums) <= 1:
        return 0
    maxjump, end, ans = 0, 0, 0
    for i in range(len(nums)):
        maxjump = max(maxjump, nums[i] + i)
        if maxjump >= len(nums) - 1:
            return ans + 1
        if end == i:
            ans += 1
            end = maxjump
    return ans

# Gas Station Circuit
def canCompleteCircuit(gas, cost):
    total_gas = sum(gas)
    total_cost = sum(cost)
    if total_gas < total_cost:
        return -1

    pos, remaining = 0, 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            remaining = 0
            pos = i + 1
    return pos
```

**When to Use:**
- Activity selection
- Huffman coding
- Fractional knapsack
- Interval scheduling

**Repository:** `GreedyAlgorithms.py`

---

## 15. **Dynamic Programming**
**What it does:** Break problems into overlapping subproblems and store results to avoid recomputation.

**Key Operations:**
- **Memoization** (Top-down): Recursion + caching
- **Tabulation** (Bottom-up): Build table iteratively
- **Space optimization**: Keep only necessary previous states

**Python Examples:**
```python
# Fibonacci with Memoization (Top-down)
def fib_memoization(n, dp=None):
    if dp is None:
        dp = [-1] * (n + 1)
    if n == 0 or n == 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib_memoization(n - 1, dp) + fib_memoization(n - 2, dp)
    return dp[n]

# Fibonacci with Tabulation (Bottom-up)
def fib_tabulation(n):
    dp = [-1] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Fibonacci with Space Optimization
def fib_spaceoptimized(n):
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

# House Robber (Space optimized DP)
def rob(nums):
    if len(nums) < 2:
        return nums[0]
    prev2 = nums[-1]
    prev1 = max(nums[-2], nums[-1])
    for i in range(len(nums) - 3, -1, -1):
        take = nums[i] + prev2
        nottake = prev1
        prev2, prev1 = prev1, max(take, nottake)
    return prev1
```

**When to Use:**
- Fibonacci
- Coin change
- Longest increasing subsequence
- Knapsack problems
- Edit distance

**Repository:** `Dynamic_Programming.py`, `2D_DP.py`

---

## 16. **Backtracking**
**What it does:** Explore all possible solutions by recursively building and undoing choices.

**Key Operations:**
- **Add** current choice to result
- **Recurse** with new state
- **Remove** choice (backtrack) to explore other paths

**Python Examples:**
```python
# Subsets (Power Set)
def subsets(arr):
    def backtrack(i, curr, res):
        res.append(curr.copy())
        for i in range(i, len(arr)):
            curr.append(arr[i])
            backtrack(i + 1, curr, res)
            curr.pop()
        return res

    return backtrack(0, [], [])

# Rat in Maze
def ratinamaze(mat):
    n = len(mat)
    visited = [[False] * n for _ in range(n)]
    res = []
    if mat[0][0] == 1:
        backtrack(0, 0, n, mat, "", visited, res)
    return res

def backtrack(i, j, n, mat, curr, visited, res):
    if i == n - 1 and j == n - 1:
        res.append(curr)
        return

    dirs = [[1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U']]
    visited[i][j] = True

    for dr, dc, move in dirs:
        nr, nc = i + dr, j + dc
        if (0 <= nr < n and 0 <= nc < n and not visited[nr][nc]
            and mat[nr][nc] == 1):
            backtrack(nr, nc, n, mat, curr + move, visited, res)

    visited[i][j] = False  # Backtrack
```

**When to Use:**
- Permutations/combinations
- N-Queens
- Sudoku solver
- Word search
- Maze problems

**Repository:** `Backtracking.py`

---

## 17. **Bitwise Operations**
**What it does:** Manipulate individual bits for efficient computation.

**Key Operations:**
- `&` (AND): Both bits 1
- `|` (OR): At least one bit 1
- `^` (XOR): Bits different
- `<<` (Left shift): Multiply by 2
- `>>` (Right shift): Divide by 2
- `~` (NOT): Flip all bits

**Python Examples:**
```python
# Set Bit at Position i
def setBit(num, i):
    return num | (1 << i)

# Clear Bit at Position i
def clearBit(num, i):
    return num & ~(1 << i)

# Check if Bit at Position i is Set
def isBitSet(num, i):
    return (num & (1 << i)) != 0

# Smallest Number with Set Bits
def smallestNumber(n):
    k = n.bit_length()
    for i in range(k):
        if n & (1 << i) == 0:
            n = n | (1 << i)
    return n

# Count Set Bits
def countBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Power of Two Check
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0
```

**When to Use:**
- Optimization (fast operations)
- Flags/permissions
- Find single number (XOR property)
- Subset generation
- Bit masking

**Repository:** `BitwiseOperations.py`

---

## Quick Reference Table

| Topic | Time | Space | Use Case |
|-------|------|-------|----------|
| Two Pointers | O(n) | O(1) | Sorted arrays, pair problems |
| Fast/Slow Pointers | O(n) | O(1) | Cycle detection, middle finding |
| Sliding Window | O(n) | O(k) | Substring/subarray optimization |
| Prefix Sum | O(n) | O(n) | Range queries, subarray sum |
| Merge Intervals | O(n log n) | O(n) | Overlapping intervals |
| Binary Search | O(log n) | O(1) | Sorted array search |
| HashMap | O(1) avg | O(n) | Frequency, pattern matching |
| Stack | O(1) | O(n) | Matching, expression eval |
| Queue | O(1) | O(n) | BFS, level-order |
| Heap | O(log n) | O(n) | Priority queue, Kth element |
| Tree | O(n) | O(h) | Hierarchical data |
| Graph | O(V+E) | O(V) | Connectivity, paths |
| Trie | O(m) | O(26n) | Autocomplete, word search |
| Greedy | Varies | O(1) | Optimization problems |
| DP | O(n) | O(n) | Overlapping subproblems |
| Backtracking | O(n!) | O(n) | Combinations, permutations |
| Bitwise | O(1) | O(1) | Bit manipulation |

---

## Problem-Solving Strategy

1. **Understand the problem** → Input, output, constraints
2. **Identify the pattern** → Which DSA technique applies?
3. **Design solution** → Step-by-step approach
4. **Code it up** → Implement carefully
5. **Test cases** → Edge cases, examples
6. **Optimize** → Time/space if needed

---

Good luck with your DSA revision! 🚀
