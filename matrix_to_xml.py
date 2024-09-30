matrix = """
[  0.0000000,  0.0000000,  1.0000000;
   0.0000000,  1.0000000,  0.0000000;
  -1.0000000,  0.0000000,  0.0000000 ]
""".replace(";", ",")

python = eval(matrix)

print(f"m00=\"{python[0]}\" m01=\"{python[1]}\" m02=\"{python[2]}\" ")
print(f"m10=\"{python[3]}\" m11=\"{python[4]}\" m12=\"{python[5]}\" ")
print(f"m20=\"{python[6]}\" m21=\"{python[7]}\" m22=\"{python[8]}\" ")

