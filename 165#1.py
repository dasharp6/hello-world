import statistics

def mean(numList):
  if(len(numList)==0):
    return 0

  return statistics.mean(numList)

def median(numList):
  if(len(numList)==0):
    return 0
  return statistics.median(numList)

def mode(numList):
  if(len(numList)==0):
    return 0
  return statistics.mode(numList)

def main():
  numList=[32, 65, 99, 62, 82, 71, 49, 5]

  print("Mean:",mean(numList))
  print("Median:",median(numList))
  print("Mode",mode(numList))

if __name__=="__main__":
    main()
