import time

q = 0
w = 0
e = 0
r = 0

def display(a,s,d,f):
  print("-----------")
  print(f"| {a}{s} : {d}{f} |")
  print("-----------")

while True:
  replit.clear()
  display(q,w,e,r)
  time.sleep(0.9)
  r += 1
  if r > 9:
    e += 1
    r = 0
  if e > 5:
    w += 1
    e = 0
  if w > 9:
    q += 1
    w = 0
  if q > 5:
    q = 0
