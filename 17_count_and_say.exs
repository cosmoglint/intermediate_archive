# https://leetcode.com/problems/count-and-say/submissions/


#The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":



defmodule Solution do
  @spec count_and_say(n :: integer) :: String.t

  def forward_check(curval, %{count: count, loc_val: prev_val, acc: acc}) do
    cond do
      prev_val == curval->
        count = count + 1
        %{count: count, loc_val: curval, acc: acc}
      true ->
        new_acc = acc <> Integer.to_string(count) <> prev_val
        loc_val = curval
        count = 1
        %{count: count, loc_val: loc_val, acc: new_acc}
    end
  end

  def cut(val) do
    enmap = %{count: 1, loc_val: String.at(val, 0), acc: ""}
    strlist = String.slice(val, 1..-1) |>
              String.split("", trim: true)
    IO.inspect(strlist)
    %{acc: acc, count: count, loc_val: loc_val} = Enum.reduce(strlist, enmap, &forward_check/2)
    fin = acc <> Integer.to_string(count) <> loc_val
  end

  def recu(0, val) do
    val
  end

 def recu(n, val) do
    new_val = cut(val)
    IO.inspect(new_val)
    recu(n-1, new_val)
  end

  def count_and_say(n) do
    recu(n-1, "1")
  end
end
