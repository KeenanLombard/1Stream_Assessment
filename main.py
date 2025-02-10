# Reverse String
def reverse_string(text):
    return text[::-1]

# Check if palindrome
def is_palindrome(text):
    # Normalize by removing spaces and making lowercase
    text = text.lower().replace(" ", "")
    return text == reverse_string(text)

# Sorting Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


text = "Racecar"
list = [5, 3, 8, 1, 2, 9, 7, 6, 4, 0]

print("Reversed String:", reverse_string(text)) 
print("Is", text,  "Palindrome:", is_palindrome(text))  
print("Bubble Sorted List:", bubble_sort(list)) 
    
    
