from magnesium.list import *
from magnesium.config import *
from magnesium.group import *

gr: Group = Group("mygroup", ["isinstance(obj, int)"], debug_group=True)

for i in range(100000):
    gr.add_member(i, label=f"number{i}")
    
