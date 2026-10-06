function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
  
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    dummy = ListNode(0);
    cur = dummy
    mod = 0;

    while(l1 || l2 || mod) {
        sum = mod;
        if (l1) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        cur.next = ListNode(sum % 10);
        mod = sum / 10;
        cur = cur.next;
    }

    return dummy.next;
};