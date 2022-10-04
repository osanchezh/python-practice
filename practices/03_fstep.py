x = int(input("enter a string: "));
if(x==0):
    print("Zero");
elif x == 1:
    print("one");
else:
    print("nothing");

words = ["abc","def","ghi"];
for w in words:
    print(w, len(w));

users = {"HA":"active", "BA":"inactive","HA1":"active", "BA2":"inactive"};

for user, act in users.copy().items():
    print("user->"+user+", act->"+act);

for i in range(7):
    print("numero="+ str(i));
exit();