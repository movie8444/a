year = as.integer(readline("Enter a year to be checked: "))
if(year %% 4 == 0 | year %% 400 == 0){
  cat(year, "is a leap year\n")
} else {
  cat(year, "is not a leap year\n")
}
