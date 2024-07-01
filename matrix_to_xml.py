matrix = """
[  0.0020578,  0.0009588, -0.9999974;
  -0.7656370,  0.6432721, -0.0009588;
   0.6432695,  0.7656370,  0.0020578 ]
""".replace(";", ",")

python = eval(matrix)

print(f"m00=\"{python[0]}\" m01=\"{python[1]}\" m02=\"{python[2]}\" ")
print(f"m10=\"{python[3]}\" m11=\"{python[4]}\" m12=\"{python[5]}\" ")
print(f"m20=\"{python[6]}\" m21=\"{python[7]}\" m22=\"{python[8]}\" ")

