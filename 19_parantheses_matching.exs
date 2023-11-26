# https://leetcode.com/problems/regular-expression-matching/

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

defmodule Solution do
  @spec longest_valid_parentheses(s :: String.t()) :: integer
  def push_stack(stack, element) do
  end

  def top_stack([]) do
    nil
  end

  def top_stack(stack) do
    Enum.at(stack, -1)
  end

  def traverse_parantheses("", curr_stack, count, max) do
    cond do
      Enum.count(curr_stack) > 0 ->
        max = if count > max, do: count, else: max

      _ ->
        nil
    end
  end

  def traverse_parantheses(par_str, curr_stack, count, max) do
    curr_value = String.at(par_str, 0)
    cut_str = String.slice(par_str, 1..-1)
    top_value = top_stack(curr_stack)

    cond do
      curr_value == "(" ->
        cond do
          top_value == "(" ->
            new_stack = curr_stack ++ ["("]
            traverse_parantheses(cut_str, new_stack, count, max)

          top_value == ")" ->
            traverse_parantheses(cut_str, curr_stack, count, max)
        end

      curr_value == ")" ->
        cond do
          top_value == nil ->
            max = if count > max, do: count, else: max
            traverse_parantheses(cut_str, [], 0, max)

          top_value == "(" ->
            new_stack = Enum.slice(curr_stack, 0..-2)
            traverse_parantheses(cut_str, new_stack, count + 2, max)

          top_value == ")" ->
            new_stack = curr_stack ++ [")"]
            traverse_parantheses(cut_str, new_stack, count, max)
        end
    end
  end

  def longest_valid_parentheses(s) do
    traverse_parantheses(s, [], 0, 0)
  end
end
