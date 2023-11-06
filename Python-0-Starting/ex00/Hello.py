ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

ft_list[1] = "World!"

lst = list(ft_tuple)
lst[1] = "Morocco!"
ft_tuple = tuple(lst)

ft_set.discard("tutu!")
ft_set.add("benguerir!")

ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)