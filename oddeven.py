a =float(input());
count =1;
if a<0:
  print("Invalid");
  count = 0;
while(count):
  if a%2==0:
    print("Even");
    count =0;
  else:
    print("Odd");
    count =0;
