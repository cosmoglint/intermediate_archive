# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=dynamic-programming
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

defmodule Solution do
  @spec rob(nums :: [integer]) :: integer
  def do_rob(houses_left) do
    houses = Enum.count(houses_left)

    cond do
      houses == 0 ->
        0

      true ->
        # calculate the max for robbing current house and leaving the next house vs
        # leaving the current house and proceeding forward
        max(
          do_rob(Enum.slice(houses_left, 1..-1)),
          Enum.at(houses_left, 0) + do_rob(Enum.slice(houses_left, 2..-1))
        )
    end
  end

  def rob(nums) do
    do_rob(nums)
  end
end
