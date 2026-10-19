# %%
on = False

def switch():
    global on
    if (on):
        on = False
    else:
        on = True
print(on)
switch()
print(on)
switch()
print(on)
# %%
