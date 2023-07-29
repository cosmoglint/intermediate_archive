# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=dynamic-programming
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

defmodule Solution do
  @spec rob(nums :: [integer]) :: integer
  def do_rob(houses_left, memomap) do
    houses_left_count = Enum.count(houses_left)

    cond do
      is_map_key(memomap, houses_left_count) ->
        {memomap[houses_left_count], memomap}

      true ->
        # calculate the max for robbing current house and leaving the next house vs
        # leaving the current house and proceeding forward
        {rob_cur, curmap} = do_rob(Enum.slice(houses_left, 1..-1), memomap)
        {leave_cur, curmap} = do_rob(Enum.slice(houses_left, 2..-1), curmap)

        max_robbable =
          max(
            rob_cur,
            Enum.at(houses_left, 0) + leave_cur
          )

        curmap = Map.put(curmap, houses_left_count, max_robbable)

        {max_robbable, curmap}
    end
  end

  def rob(nums) do
    {ans, _} = do_rob(nums, %{0 => 0})
    ans
  end
end
