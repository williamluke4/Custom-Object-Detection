# Used for Compiling Protos on Windows with protoc version=3.6
import glob
import subprocess
import os
PROTOS_PATH = "object_detection/protos/"

proto_files = glob.glob(PROTOS_PATH+ "*.proto")

print("Compiling %d files in %s" % (len(proto_files), PROTOS_PATH))

for file in proto_files:
  try:
    complete = subprocess.run(
      ["protoc", file,"--python_out=."], 
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT, 
      shell=False, 
      check=True
    )
    print("Compiled: %s" % os.path.split(file)[1])
  except subprocess.CalledProcessError as suberror:
    print("Error Compiling: %s" % os.path.split(file)[1])
    print("Error Output") 
    print("===================================================")
    print(suberror.stdout.decode('utf-8'))
    print("===================================================")


