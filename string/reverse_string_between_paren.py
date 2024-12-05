def reverse_parentheses(s: str) -> str:
    stack = []
    current_string = ""

    for char in s:
        if char == '(':
            # 将当前字符串推入栈中，并重置
            stack.append(current_string)
            current_string = ""
        elif char == ')':
            # 反转当前字符串并与栈顶字符串连接
            current_string = stack.pop() + current_string[::-1]
        else:
            # 添加字符到当前字符串
            current_string += char

    return current_string


# 示例用法
input_string = "(abcd(efg)h)"
result = reverse_parentheses(input_string)
print(f"反转后的字符串: {result}")
