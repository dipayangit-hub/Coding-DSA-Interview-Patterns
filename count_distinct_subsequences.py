def count_distinct_subsequences(s, x, y):
    target = y - x
    dp = {0: 1}  # net movement → count

    for ch in s:
        new_dp = dp.copy()
        for move, cnt in dp.items():
            if ch == 'r':
                new_move = move + 1
            else:
                new_move = move - 1

            new_dp[new_move] = new_dp.get(new_move, 0) + cnt

        dp = new_dp

    # subtract empty subsequence
    return dp.get(target, 0)


count_distinct_subsequences("rrlrlr",1,4)