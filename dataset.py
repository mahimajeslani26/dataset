import os
import cv2

def FrameCapture(path, opath): 
      
    # Path to video file 
    #print(opath)
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        count += 1
  
        # Saves the frames with frame-count 
        frame_path = opath + ("%05d.jpg" % count)
        #print(frame_path)
        cv2.imwrite(frame_path, image) 

    print(count)
  
        


path = 'Training Dataset'
save_path = 'DatasetFinal'
for subject_folder in os.listdir(path):
	#print(subject_folder)
		#print (subject_folder)
	folder_path = os.path.join(path,subject_folder)
	print(subject_folder)
	print()
	for category in os.listdir(folder_path):
		
		
		if (category == "noglasses") or (category == "glasses") : 
			print(category)
			category_path = os.path.join(folder_path, category)

			video_path = os.path.join(category_path, 'nonsleepyCombination.avi')
			Alert_path = 'Alert/' + subject_folder+ '_' + category + '_A_'
			#print(Alert_path)
			FrameCapture(video_path, os.path.join(save_path,Alert_path))

	print()