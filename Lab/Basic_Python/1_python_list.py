bbu_capuses = [
    "PP", "TK", "SH", "SR", "BB" , "BMC", "RK", "ST", "TB"
]


# positive and negative index
# positive index: >=0
print (f"(Index 5:{bbu_capuses}")

# Range index 0-3: ["PP", "TK","SH","SR"]
print(f"Index 0-3:{bbu_capuses[:4]}")

# ["SR", "BB","BMC","RK","ST","TB"]
print(f"Range Index 3-Last Index:{bbu_capuses[3:]}")

# negative index: <0
print(f"Index -4:{bbu_capuses[-4]}")

# ["BMC","RK","ST"]
print(f"Range negative index:{bbu_capuses[-4:-1]}")

# Add neww item into list
# append or insert method: build in method of list
# appsend use to add new item into last place
bbu_capuses.append("KP")
print(bbu_capuses)

# insert: use to add new item into any index
bbu_capuses.insert(1, "KD")
print(bbu_capuses)

# Upadte
# Update use index
bbu_capuses[0] = "Phnom Penh"
print(bbu_capuses)

# Delete:
# pop or remove
# pop is method use to remove item by index
bbu_capuses.pop(-1)
# remove is method use to remove item value
bbu_capuses.remove("KD")
print(bbu_capuses)

# CRUD =
#C - Create (បង្កើត ឬបញ្ចូលទិន្នន័យថ្មីចូលក្នុង Database)
#R - Read (អាន ឬទាញយកទិន្នន័យមកមើល)
#U - Update (កែប្រែ ឬអាប់ដេតទិន្នន័យដែលមានស្រាប់)
#D - Delete (លុប ឬបំបាត់ទិន្នន័យចោល)