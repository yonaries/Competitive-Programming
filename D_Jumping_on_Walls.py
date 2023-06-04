def can_escape(n, k, left_wall, right_wall):
    water_level = 1
    left_pos = 1
    right_pos = 1 + k

    while left_pos <= n or right_pos <= n:
        # Check if ninja is below water level
        if left_pos < water_level or right_pos < water_level:
            return "NO"
        # Check if ninja is in a dangerous area
        if left_wall[left_pos-1] == "X" or right_wall[right_pos-1] == "X":
            return "NO"
        # Check if ninja has escaped
        if left_pos > n or right_pos > n:
            return "YES"

            # Try to make a move
        if right_pos - left_pos > k:
            # Can't jump to other wall
            if left_wall[left_pos] == "-" and left_pos < right_pos - k:
                left_pos += 1
            elif left_wall[left_pos-1] == "-" and left_pos > right_pos - k:
                left_pos -= 1
            elif right_wall[right_pos-1] == "-" and right_pos > left_pos + k:
                right_pos -= 1
            else:
                return "NO"
        else:
            # Can jump to other wall
            if left_wall[left_pos] == "-" and left_pos < right_pos - k:
                left_pos += 1
            elif left_wall[left_pos-1] == "-" and left_pos > right_pos - k:
                left_pos -= 1
            elif right_wall[right_pos-1] == "-" and right_pos > left_pos + k:
                right_pos -= 1
            elif right_wall[right_pos+k-1] == "-" and right_pos + k <= n and right_pos + k < left_pos:
                right_pos += k
            else:
                return "NO"
        # Raise water level
        water_level += 1
    return "NO"
