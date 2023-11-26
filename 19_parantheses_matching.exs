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

  def traverse_parantheses("", _, count, max) do
    max = if count > max, do: count, else: max
  end

  def traverse_parantheses(par_str, curr_stack, count, max, rev) do
    curr_value = String.at(par_str, 0)
    cut_str = String.slice(par_str, 1..-1)
    top_value = top_stack(curr_stack)

    cond do
      curr_value == "" ->
        0

      curr_value == "(" ->
        cond do
          top_value == "(" ->
            new_stack = curr_stack ++ ["("]
            traverse_parantheses(cut_str, curr_stack, count, max, rev)

          top_value == ")" ->
            rev = 0
            traverse_parantheses(cut_str, curr_stack, count, max, rev)
        end

      curr_value == ")" ->
        cond do
          top_value == nil ->
            max = if count > max, do: count, else: max
            traverse_parantheses(cut_str, [], 0, max, rev)

          top_value == "(" ->
            new_stack = Enum.slice(curr_stack, 0..-2)
            traverse_parantheses(cut_str, new_stack, count + 2, max, rev + 2)

          top_value == ")" ->
            new_stack = curr_stack ++ [")"]
            traverse_parantheses(cut_str, new_stack, count, max, rev)
        end
    end
  end

  def longest_valid_parentheses(s) do
    traverse_parantheses(s, [], 0, 0)
  end
end
