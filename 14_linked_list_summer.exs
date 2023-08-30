# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
#
defmodule ListNode do
  @type t :: %__MODULE__{
          val: integer,
          next: ListNode.t() | nil
        }
  defstruct val: 0, next: nil
end

defmodule Solution do
  def adder(nil, nil, _) do
    nil
  end

  def adder(list1, list2, carry) do
    if list1.next == nil and list2.next == nil do
      # IO.puts("theyre both nil broooo")
    end

    myval = list1.val + list2.val + carry

    {myval, carry} =
      if myval >= 10 do
        {myval - 10, 1}
      else
        {myval, 0}
      end

    nexx = adder(list1.next, list2.next, carry)

    argsl = [val: myval, next: nexx]
    struct(ListNode, argsl)
  end

  @spec add_two_numbers(l1 :: ListNode.t() | nil, l2 :: ListNode.t() | nil) :: ListNode.t() | nil
  def add_two_numbers(l1, l2) do
    adder(l1, l2, 0)
  end
end

defmodule Main do
  def main do
    l1 = %ListNode{next: %ListNode{next: %ListNode{next: nil, val: 3}, val: 4}, val: 2}
    l2 = %ListNode{next: %ListNode{next: %ListNode{next: nil, val: 4}, val: 6}, val: 5}

    IO.inspect(Solution.add_two_numbers(l1, l2))
  end
end

Main.main()
