#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for j in range(rows-i):
        print(" ", end="")
    print("\n", end="")
