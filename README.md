# Notes to remember for myself

## Tree 🌳🌲🌵🌴

- **Recursion** ---> **Stack** (remember the the russian dolls exp.)
    - **DFS** uses **Recursion** so ---> **Stack**
- Questions like levelOrderTraversal or SideView that is kinda LevelbyLevel, use the **val** and saving it in a list tho! like these: [LevelOrder](https://leetcode.com/problems/binary-tree-level-order-traversal/) + [SideView](https://leetcode.com/problems/binary-tree-level-order-traversal/) 

- Problems that are asking for counting the nodes that have specific charachtristic(e.g. good points, related to their values) always consider amount initiallay then compare *(e.g. count= 1, max(count, sth))*  like these questions; [GoodPoints](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) 

- DFS has In/Pre/Post- Order, then in InOrder Version, we use Stack! And Ya initially go as far LEFT as ya can! Then at the first step, ya add the initial root to the stack, cause ya know that ya gonna pop back to that root (initial starting root) when ya are done traversing the left side tree! Then, **when ya reach a NULL, its time to go back to the prev node (in inorder case, the pre one will be the root)** but note that before getting to null, ya need to add that node into the Stack!
Then, once we pop out the node, we go to the right child! ONLY after ya process/visited that node! We gotta get to right child after we visit the node! (pop it out)