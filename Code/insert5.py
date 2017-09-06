with open('data.txt', 'a') as f:
    f.writelines(['I want to add a third line\n', 'And mayve a fourth...'])
    
with open('data.txt', 'r') as f:
    print(f.readlines())