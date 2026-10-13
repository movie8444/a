n <- as.integer(readline("Enter size of array: "))
arr <- numeric(n)
for(i in 1:n){ arr[i] <- as.integer(readline("Enter number: ")) }
print(arr)
cat("\n sorted array elements (ascending) are as follows: ")
print(sort(arr))
cat("\n sorted array elements (descending) are as follows: ")
print(sort(arr, decreasing=TRUE))
