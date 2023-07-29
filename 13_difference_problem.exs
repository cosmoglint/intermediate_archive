# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


defmodule Solution do
  @spec two_sum(numbers :: [integer], target :: integer) :: [integer]
  def calc_target(nums, target, iter, mymap) do
    curval = Enum.at(nums, 0)

    cond do
      Enum.count(nums) == 0 ->
        false

      curval > target ->
        false

      curval == target ->


      is_map_key(mymap, curval) ->
        [mymap[curval], iter]

      true ->
        mymap = Map.put(mymap, target - curval, iter)
        calc_target(Enum.slice(nums, 1..-1), target, iter + 1, mymap)
    end
  end

  def two_sum(numbers, target) do
    mymap = %{}
    calc_target(numbers, target, 1, mymap)
  end
end


defmodule TwoPointerSolution do
  @spec two_sum(numbers :: [integer], target :: integer) :: [integer]
  def calc_target(nums, target, iter1, iter2) do
    val1 = Enum.at(nums, 0)
    val2 = Enum.at(nums, -1)

    cond do
      val1 + val2 == target ->
        [iter1, iter2]

      val2 + val1 > target ->
        calc_target(Enum.slice(nums, 0..-2), target, iter1, iter2 - 1)

      val2 + val1 < target ->
        calc_target(Enum.slice(nums, 1..-1), target, iter1 + 1, iter2)

      true ->
        false
    end
  end

  def two_sum(numbers, target) do
    calc_target(numbers, target, 1, Enum.count(numbers))
  end
end
