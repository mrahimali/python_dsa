def char_freq(tx):
    my_dict=dict()
    for i in range(0,len(tx)):
        if tx[i] in my_dict:
            my_dict[tx[i]] +=1
        else:
            my_dict[tx[i]]=1
    return my_dict

txt = 'heijoijeofeew'
ans = char_freq(txt)
print(ans['h'])