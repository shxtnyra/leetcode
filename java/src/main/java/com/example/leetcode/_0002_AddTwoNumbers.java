package com.example.leetcode;

public class _0002_AddTwoNumbers {

    public ListNode solve(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        int mod = 0;

        while (l1 != null || l2 != null || mod != 0) {
            int sum = mod;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            cur.next = new ListNode(sum % 10);
            mod = sum / 10;
            cur = cur.next;
        }
        return dummy.next;
    }

    public class ListNode {
        private int val;
        private ListNode next;

        public ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        public ListNode(int val) {
            this.val = val;
            this.next = null;
        }

        public ListNode() {
            this.val = 0;
            this.next = null;
        }

        public int getVal() {
            return val;
        }

        public ListNode getNext() {
            return next;
        }
    }
}
