#!/usr/bin/python3
"""
unlocked boxes
take boxes
    create a set of keys
        go to first box
        iterate theough provided keys and open box that have similar index to the key provided
        iterate trhough the boxes evaulating if all the boxes can be unlocked
"""
def canUnlockAll(boxes):
    n = len(boxes)
    
    # set to monitor unlocked boxes
    unlocked_boxes = {0}
    
    # set of available keys
    available_keys = set(boxes[0])
    
    # Iterate keys and unlock new boxes
    while available_keys:
        key = available_keys.pop()
        
        # Check if the key corresponds to a valid box
        if key < n and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            available_keys.update(boxes[key])
    
    # Check if all boxes are unlocked
    return len(unlocked_boxes) == n
