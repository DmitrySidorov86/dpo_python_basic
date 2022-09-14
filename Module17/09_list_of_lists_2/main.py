nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_nice_list = [x for three_lvl in nice_list for two_lvl in three_lvl for x in two_lvl ]

print(new_nice_list)
