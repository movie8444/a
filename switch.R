n = as.integer(readline("Enter a number between 1-10: "))
word <- switch(as.character(n),
  "1" = print("One"), "2" = print("Two"), "3" = print("Three"),
  "4" = print("Four"), "5" = print("Five"), "6" = print("Six"),
  "7" = print("Seven"), "8" = print("Eight"), "9" = print("Nine"),
  "10" = print("Ten"), print("Invalid input")
)
