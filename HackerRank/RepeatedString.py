s = "ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt"
n = 685118368975

# s = "bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc"
# n = 649606239668

# s = "ababa"
# n = 10

print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


# if len(s) >= n:
#     print(s[0:n].count('a'))
# else:
#     bulat = (n * s.count('a')) // len(s)
#     res = n % len(s)
#     resString = ''
#     if res != 0:
#         resString = s[0:res]
#     print(bulat + resString.count('a'))
# #
