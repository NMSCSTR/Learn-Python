def bubble_sort_trace(arr):
    n = len(arr)
    print("Initial array:", arr)
    print("length: ", n)
    
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        
        for j in range(0, n - i - 1):
            print(f"  Comparing {arr[j]} and {arr[j + 1]}...", end=" ")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"swapped → {arr}")
            else:
                print("no change") 
        if not swapped:
            print("  No swaps in this pass, array is sorted.")
            break
        else:
            print("  Array after this pass:", arr)
    print("\nSorted array:", arr)
    
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_trace(data)


