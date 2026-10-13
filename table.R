n = as.integer(readline("Enter the no whose multiplication table is to be displayed: "))
for(i in 1:10) {
  cat("\n", n, " x ", i, " = ", n * i)
}
