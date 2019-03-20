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
  
        


path = 'train'
save_path = 'Dataset'
for label_folder in os.listdir(path):
	#print(subject_folder)
		#print (subject_folder)
	label_folder_path = os.path.join(path,label_folder)
	print(label_folder)
	print()
	for video_file in os.listdir(label_folder_path):
		print(video_file)
		video_path = os.path.join(label_folder_path,video_file)
		output_path = os.path.join(save_path,label_folder, video_file[0:3] + '_')
		FrameCapture(video_path, output_path)
		

	print()
