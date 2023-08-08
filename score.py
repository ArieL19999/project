
import os.path
import Utils

#
# get the last results reported in the score file
# If files still does not exist last_score = 0
#
def get_last_line(source_file):
  with open(source_file, "rb") as file:
    try:
      file.seek(-2, os.SEEK_END)
      while file.read(1) != b'\n':
        file.seek(-2, os.SEEK_CUR)
    except OSError:
      file.seek(0)
      
    last_score = file.readline().decode()
      
  print(f"this is the last score: {last_score}")
  return int(last_score)



# add new score to the score file
def add_score(difficulty, score_file):
  points_of_winning = (difficulty * 3) + 5
  last_score = get_last_line(score_file)
  new_score = int(last_score) + int(points_of_winning)
  print(f"user got a new score {new_score}")
  
  with open(score_file, 'a') as file:
    file.write("\n" + str(new_score))
  
  print("new score added to score file")
  
def main():
  file_name=Utils.SCORES_FILE_NAME
  #Create scores file if it does not exist
  # add score 0 to the file
  if not os.path.isfile(file_name):
    with open(file_name, 'w') as file:
      file.write("This is the scores file: \n0")  
    
  add_score(3, file_name)
  
  with open(file_name, 'r') as file:
    data = file.read()
  
  print (f"The file {file_name} contain these info: \n{data}")


if __name__ == "__main__":
    main()
    
    

    
