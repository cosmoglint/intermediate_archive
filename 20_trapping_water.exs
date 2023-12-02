# https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

defmodule Solution do
  @spec trap(height :: [integer]) :: integer
  # basically keep track of the max value of left and right and keep iterating the smaller one
  def fill_water([], _, _, ans) do
    ans
  end

  def fill_water(blocks, lmax, rmax, ans) do
    lval = Enum.at(blocks, 0)
    rval = Enum.at(blocks, -1)

    lmax = max(lval, lmax)
    rmax = max(rval, rmax)

    cond do
      lmax > rmax ->
        fill_water(Enum.slice(blocks, 0..-2), lmax, rmax, ans + rmax - rval)

      true ->
        fill_water(Enum.slice(blocks, 1..-1), lmax, rmax, ans + lmax - lval)
    end
  end

  def trap(height) do
    fill_water(height, 0, 0, 0)
  end
end
