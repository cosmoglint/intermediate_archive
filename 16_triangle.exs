# https://leetcode.com/problems/triangle/


# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


defmodule Solution do
  @spec minimum_total(triangle :: [[integer]]) :: integer
  def next_step(width, level, triangle) do
      current_row = Enum.at(triangle, level)
      val = Enum.at(current_row, width)
      next_row = Enum.at(triangle, level+1)
      case next_row do
        nil ->
          val
        _ ->
          left_step = next_step(width, level+1, triangle)
          right_step = next_step(width+1, level+1, triangle)
          endval = min(left_step, right_step)
          val + endval
    end
  end

  def minimum_total(triangle) do
    ans = next_step(0, 0, triangle)
    ans
  end
end
