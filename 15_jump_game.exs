# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# [2,3,0,1,4]

defmodule Solution do
  @spec jump(nums :: [integer]) :: integer

  def custom_min(:infinity, :infinity) do
    :infinity
  end

  def custom_min(val1, :infinity) do
    val1
  end

  def custom_min(:infinity, val2) do
    val2
  end

  def custom_min(val1, val2) do
    min(val1, val2)
  end

  def custom_add(val1, :infinity) do
    :infinity
  end

  def custom_add(val1, val2) do
    val1 + val2
  end

  def short_jump(nums, current, jumper, memomap) when jumper == current do
    memojump(Enum.slice(nums, current..-1), memomap)
  end

  def short_jump(nums, current, jumper, memomap) do
    custom_min(
      memojump(Enum.slice(nums, current..-1), memomap),
      short_jump(nums, current + 1, jumper, memomap)
    )
  end

  def memojump([_], memomap) do
    0
  end

  def memojump(nums, memomap) do
    cond do
      Map.has_key?(memomap, nums) ->
        nil

      true ->
        jumper = Enum.at(nums, 0)
        nums_len = Enum.count(nums)
        # IO.inspect(nums)
        # IO.inspect(jumper)
        # IO.inspect(nums_len)
        cond do
          nums_len > jumper + 1 ->
            case jumper do
              0 ->
                :infinity

              _ ->
                # rest_nums = Enum.slice(nums, 1..-1)
                # jumpable_slice = Enum.slice(nums, 1..jumper)
                shortest =
                  custom_add(
                    1,
                    short_jump(nums, 1, jumper, memomap)
                    # custom_min(
                    #   memojump(Enum.slice(nums, 1..-1), memomap),
                    #   memojump(Enum.slice(nums, jumper..-1), memomap)
                    # )
                  )

                # IO.inspect(shortest)
                shortest

                # Map.put(memomap, nums, shortest)
            end

          true ->
            # IO.puts("returning a 1")
            1
        end
    end
  end

  def jump(nums) do
    memojump(nums, %{})
  end
end
