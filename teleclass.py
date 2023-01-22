import os
#v1,v2,v3="Bca","maths","ch1.txt"
'''print([[v3==branch_var] for branch_var in sorted(os.listdir("branches"))])
print([[v3==sub_var] for sub_var in sorted(os.listdir(f"branches/Bca"))])
print([[v3==file_var] for file_var in sorted(os.listdir(f"branches/Bca/maths"))])
print([[file_var] for file_var in sorted(os.listdir(f"branches/Bca/maths"))])
print([[sub_var] for sub_var in sorted(os.listdir(f"branches/Bca"))])
print([[branch_var] for branch_var in sorted(os.listdir("branches"))])'''
#print(["maths"]in[[branch_var] for branch_var in sorted(os.listdir("branches/Bca/"))])
#[[fil_lst] for fil_lst in ]]

#directory = "branches/Bca/"
#subdirectories = os.listdir(directory)

#lut=list(map(lambda subdir: (sorted(os.listdir(f"{directory}/{subdir}"))), subdirectories))
file_path=[]
def file_path_va(path):
    file_path.append(path)
    return os.path.join(*file_path)
def file_path_va_cl(path):
    file_path.remove(path)


