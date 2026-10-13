flist = c("Lily", "Rose", "Jasmine", "Tulip")
print(flist)
fname = readline("Enter flower name: ")
if(fname %in% flist){
  print("Entered flower present in the list")
} else {
  print("Entered flower is not present in the list")
}
