
if __name__ == "__main__":

  x = "train"

  words = [] 
  with open('wordle.txt','r') as f:

    for line in f: 
      word = line.strip()
      words.append(word)

  print("train" in words) # O(1)
  print("lyric" in words) # O(1)

