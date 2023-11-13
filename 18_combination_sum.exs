# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

defmodule Solution do
  @spec combination_sum(candidates :: [integer], target :: integer) :: [[integer]]
  def map_push(times, acc_map) do
    curval = Map.get(acc_map, :curval)
    multiple = times * curval

    newlist = for _ <- 1..times, do: curval

    cond do
      Map.has_key?(acc_map, multiple) ->
        map_elem = Map.get(acc_map, multiple)
        fin_list = map_elem ++ [newlist]
        Map.put(acc_map, multiple, fin_list)

      true ->
        Map.put(acc_map, multiple, [newlist])
    end
  end

  def add_to_map(val, %{target: target} = acc_map) do
    times = Integer.floor_div(target, val)
    acc_map = Map.put(acc_map, :curval, val)

    new_map = Enum.reduce(1..times, acc_map, &map_push/2)

    cond do
      Map.has_key?(acc_map, val) ->
        new_map

      true ->
        new_map
    end
  end

  def combinate(og_list, elem) do
    IO.inspect(og_list)
    IO.inspect(elem)

    Enum.map(og_list, fn x ->
      Enum.map(elem, fn y ->
        x ++ y
      end)
    end)
  end

  def map_calculator(map, target, res) do
    map_keys = Map.keys(map)
    felem = Enum.at(map_keys, 0)

    cond do
      Map.has_key?(map, target - felem) ->
        res ++ combinate(Map.get(map, felem), Map.get(map, target - felem))
        nmap = Map.delete(map, [felem, target - felem])
        map_calculator(nmap, target, res)

      true ->
        res
    end
  end

  def generate_map(candidate_list, target) do
    new_map = Enum.reduce(candidate_list, %{target: target}, &add_to_map/2)
    new_map = Map.drop(new_map, [:target, :curval])

    IO.inspect(new_map)

    # cal_list =
    #   Enum.map(new_map, fn {k, v} ->
    #     cond do
    #       Map.has_key?(new_map, target - k) ->
    #         combinate(v, Map.get(new_map, target - k))

    #       true ->
    #         []
    #     end
    #   end)

    # IO.inspect(cal_list)
  end

  def combination_sum(candidates, target) do
    generate_map(candidates, target)
  end
end

IO.inspect(Solution.combination_sum([1, 2, 3, 4], 9))

# IO.inspect(Solution.combinate([[1, 2, 3, 4], [6, 8, 9, 0]], [[11, 22, 33, 44], [22, 44, 55, 66]]))
