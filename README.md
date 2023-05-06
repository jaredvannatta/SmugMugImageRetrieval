# API Call to Smug Mug to Retrieve Random Images with Description

## Directory Structure: 

SmugMug
- README.txt
  - .github
    - workflows
     - build-macos-executable.yaml 
- image_call.spec ## IGNORE THIS
- image_call.py ## SOURCE CODE
- build
 - image_call (all build code that allows program to run as an executable, don't mess with this)
 - dist (contains windows executable)
 - image_call.exe (This is the actual application, you just double click this and it will run on your machine)
 - image_returns (all retrievals are stored here, every day you run the script it will create another folder with the Year/Month/Day the image was pulled down)
   - Year/Month/Day Folder
    - Photo 
    - Caption.txt
