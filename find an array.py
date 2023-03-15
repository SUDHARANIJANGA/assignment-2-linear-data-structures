def findDuplicates(arr, Len):
     
    # Initialize ifPresent as false
    ifPresent = False
 
    # ArrayList to store the output
    a1 = []
    for i in range(Len - 1):
        for j in range(i + 1, Len):
 
            # Checking if element is
            # present in the ArrayList
            # or not if present then break
            if (arr[i] == arr[j]):
                if arr[i] in a1:
                    break
                 
                # If element is not present in the
                # ArrayList then add it to ArrayList
                # and make ifPresent at true
                else:
                    a1.append(arr[i])
                    ifPresent = True
 
    # If duplicates is present
    # then print ArrayList
    if (ifPresent):
        print(a1, end = " ")
    else:
        print("No duplicates present in arrays")