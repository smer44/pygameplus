

def stack_str(stack):
    return ", ".join(str(t[0]) for t in stack)

def dsfp(root,fn_children,fn_aggregate,fn_leaf, allow_loops = False, reverse_children = False):
    """
    dsfp is graph traversal order like dfs but after visiting
    children (and applying something to them) you visit their parent (and may ally something to it, using applied children)
    There must be no loops in graph, so loops are not visited or there is an error message.
    If allow_loops = True, edges what lead to loop are omitted during traversal.
    TODO - aggregation function should use some neutral value on the place, what leads to loop and what was omitted.
    """

    stack = [(root,False)]
    stack_set = set()
    visited_set = set()
    while stack:
        node,children_visited =  stack.pop()

        if children_visited:
            assert node in visited_set
            fn_aggregate(node)
            stack_set.remove(node)
        else:
            visited_set.add(node)
            children_result = fn_children(node)
            if children_result:
                if reverse_children:
                    children = reversed(children_result)
                else:
                    children = iter(children_result)
                filtered_children = []
                for child in children:
                    if child in stack_set:
                        if allow_loops:
                            pass
                        else:
                            raise RuntimeError(f"loop found having stack: {stack_str(stack)}; then child of last node: {child}")
                    else:
                        if child not in visited_set:
                            filtered_children.append(child)
                if filtered_children:
                    stack.append((node, True))
                    stack_set.add(node)
                    for child in filtered_children:
                        stack.append((child, False))
                else:
                    #the node has children_result but no filtered_children, so i just apply aggregation function to it.
                    fn_aggregate(node)
            else:
                fn_leaf(node)




