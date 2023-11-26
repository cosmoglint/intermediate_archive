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
    0
  end

  def top_stack(stack) do
    Enum.at(stack, -1)
  end

  def traverse_parantheses("", _, max, index) do
    max
  end

  def traverse_parantheses(par_str, curr_stack, max, index) do
    curr_value = String.at(par_str, 0)
    cut_str = String.slice(par_str, 1..-1)
    IO.inspect(curr_stack)
    IO.inspect(index)

    cond do
      curr_value == "(" ->
        new_stack = curr_stack ++ [index]
        traverse_parantheses(cut_str, new_stack, max, index + 1)

      curr_value == ")" ->
        new_stack = Enum.slice(curr_stack, 0..-2)

        cond do
          new_stack == [] ->
            new_stack = new_stack ++ [index]
            traverse_parantheses(cut_str, new_stack, max, index + 1)

          true ->
            top_value = top_stack(new_stack)
            diff = index - top_value
            max = if diff > max, do: diff, else: max
            traverse_parantheses(cut_str, new_stack, max, index + 1)
        end
    end
  end

  def longest_valid_parentheses(s) do
    traverse_parantheses(s, [0], 0, 1)
  end
end
