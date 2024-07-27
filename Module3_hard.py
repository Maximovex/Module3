def flatten(flatted=[],*args):
    if len(args)==0: 
        return flatted
    else:
        if isinstance(args[0], int) or isinstance(args[0],str):
            flatted.append(args[0])
            flatten(flatted,*args[1:])
            return flatted
        elif isinstance(args[0], list) or isinstance(args[0],tuple) or isinstance(args[0],set):
            
            flatten(flatted,*args[0])
            flatten(flatted,*args[1:])
            return flatted
        elif isinstance(args[0],dict):
            dict_to_list=list(args[0].items())
            flatten(flatted,*dict_to_list)
            flatten(flatted,*args[1:])
            return flatted
        
            
def summarising(*args):
    if not args:
        return 0
    if isinstance(args[0],int):
        return args[0]+summarising(*args[1:])
    if isinstance(args[0],str):
        return len(args[0])+summarising(*args[1:])
    
def summ_flat(*args):
    return summarising(*flatten([],*args))
            

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


print(summ_flat(*data_structure))
