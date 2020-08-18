import unreal, json, os

#Create Directoy for Folder Color UE4 Project#

#to create base folder structure with colors do the following code:
# import FolderDir
# reload(FolderDir)
# FolderDir.createColorFolderDir()

# to update new folder added with their folder colors do the following code:
# import FolderDir
# reload(FolderDir)
# FolderDir.getNewFolderCreated()

############################ Json for folder dictionary ###############################

path = "C:/Temp/UE4folderStruct.json"																		# Json File is saved to the C:/Temp file of the user
folders = {																									# json dic for folder structure
	'Art' : {
		'Effects' : {
			'Master_Materials' : None, 
			'Material_Functions':None, 
			'Material_Instances':None, 
			'Mesh': None, 
			'Particles' : None, 
			'Textures' : None
			},
		'Models' : {
			'Character' : {
				'Animations' : None,
				'Master_Materials' : None,
				'Material_Instances' : None,
				'Mesh' : None,
				'Skeleton' : None,
				'Textures' : None
				},
			'Environment' : {
				'Master_Materials' : None,
				'Material_Instances' : None,
				'Mesh' : None,
				'Textures' : None
				},
			'Props' : {
				'Animations' : None,
				'Master_Materials' : None,
				'Material_Instances' : None,
				'Mesh' : None,
				'Textures' : None,
				'Skeleton' : None
				},
			},
		'UI' : None,

	},
	'Audio':{
		'Character' : None,
		'Environment' : None,
		'WwiseEvents' : None,
		'WwiseSoundBanks' : None
		},
	'Blueprints' : {
		'Base_Blueprints' : None,
		'Character_Blueprints' : None,
		'General_Blueprints' : None,
		'Widget_Blueprints' : None,
		'Notifications' : None
		},
	'Maps' : {
		'Game_Maps' : {
			'Level_01' : None,
			'Level_Main' : None,
			'Level_Lobby' : None
			},
		'Test_Maps' : None
		},
	'Sequence' : None
}

with open(path, 'w') as f:																					# dumping the json files
	json.dump(folders, f)

############################ Creating folders with colors in ue4 ###############################

def setDirectoryColor(folders = '', color = None):
	''' this connects the script to the C++ in the project and changes the folder color '''
	unreal.FolderColors.set_folder_color(folders,color)

def createColorFolderDir():
	'''this will create the folder structure based on the json file above and color them inside UE4'''

	with open(path, 'r') as f:
		folders = json.load(f)

	color = unreal.LinearColor(1, 1, 0, 1)																

	#hsv variables																		
	v = 1.0
	s = 1.0
	artColor = 269.0																						# magenta color
	audioColor = 58.5																						# yellow color
	bpColor = 200.0																							# light blue color
	mapsColor = 22.0																						# orange color
	sequenceColor = 116.0																					# green color

	rootPath = '/Game'																						# Root path to create the paths	for the folder structure. Its needs to be '/Game' in code although its referecing the "Contents" folder	

	MapPath = '{}/{}'.format(rootPath, (folders.keys())[0])													# Creates the Map Folder Path
	BpPath = '{}/{}'.format(rootPath, (folders.keys())[1])													# Creates the Bp Folder Path
	AudioPath = '{}/{}'.format(rootPath, (folders.keys())[2])												# Creates the Audio Folder Path
	ArtPath = '{}/{}'.format(rootPath, (folders.keys())[3])													# Creates the Art Folder Path
	SequencePath = '{}/{}'.format(rootPath, (folders.keys())[4])											# Creates the Sequence Folder Path

	#Creating the top Folders

	color.set_from_hsv(h = mapsColor, s = s, v = v)															# hsv color changed for Map Folder \n Creating Map folder and  \n changing its color in UE4
	unreal.EditorAssetLibrary.make_directory(MapPath)														
	setDirectoryColor(MapPath,color)																		

	color.set_from_hsv(h = bpColor, s = s, v = v)															# hsv color changed for Blueprint Folder \n Creating Blueprint folder and \n changing its color in UE4
	unreal.EditorAssetLibrary.make_directory(BpPath)														
	setDirectoryColor(BpPath, color)																		

	color.set_from_hsv(h = audioColor, s = s, v = v)														# hsv color changed for Audio Folder \n Creating Audio folder and \n changing its color in UE4
	unreal.EditorAssetLibrary.make_directory(AudioPath)														
	setDirectoryColor(AudioPath, color)																		

	color.set_from_hsv(h = artColor, s = s, v = v)															# hsv color changed for Art Folder \n Creating Art folder and \n changing its color in UE4
	unreal.EditorAssetLibrary.make_directory(ArtPath)														
	setDirectoryColor(ArtPath, color)																		

	color.set_from_hsv(h = sequenceColor, s = s, v = v)														# hsv color changed for sequence Folder \n Creating sequence folder and \n changing its color in UE4
	unreal.EditorAssetLibrary.make_directory(SequencePath)													
	setDirectoryColor(SequencePath, color)		

	# Creating the Folders under the Art folder

	color.set_from_hsv(h = artColor, s = s, v = v)															# hsv color changed for arts Folders 

	for art in folders['Art']:
		ArtFolderPath = '{}/Art/{}'.format(rootPath,art)													# Make the Art folder path \n Creating the files Directly under Art folder \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(ArtFolderPath)												
		setDirectoryColor(ArtFolderPath, color)																

	for vfx in folders['Art']['Effects']:
		ArtEffectsFolderPath = '{}/Art/Effects/{}'.format(rootPath,vfx)										# Make the folder paths /Game/Art/Effects \n Creating art folder structure under /Game/Art/Effects/ \n changing its color in ue4 
		unreal.EditorAssetLibrary.make_directory(ArtEffectsFolderPath)										
		setDirectoryColor(ArtEffectsFolderPath, color)														

	for mods in folders['Art']['Models']:
		ArtModelsFolderPath = '{}/Art/Models/{}'.format(rootPath,mods)										# Make the folder path /Game/Art/Models \n creating art folder structure under /Game/Art/Models/ \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(ArtModelsFolderPath)										
		setDirectoryColor(ArtModelsFolderPath, color)														

	for char in folders['Art']['Models']['Character']:
		ArtCharFolderPath = '{}/Art/Models/Character/{}'.format(rootPath,char)								# Make the folder paths /Game/Art/Models/Character  \n creating folder struct under /Game/Art/Models/Characters/ \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(ArtCharFolderPath)											
		setDirectoryColor(ArtCharFolderPath, color)															

	for env in folders['Art']['Models']['Environment']:
		ArtEnvFolderPath = '{}/Art/Models/Environment/{}'.format(rootPath,env)								# Make the folder paths /Game/Art/Models/Environment \n creating folder struct under /Game/Art/Models/Environment/ \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(ArtEnvFolderPath)											
		setDirectoryColor(ArtEnvFolderPath, color)															

	for prop in folders['Art']['Models']['Props']:
		ArtPropFolderPath = '{}/Art/Models/Props/{}'.format(rootPath,prop)									# Make the folder path /Game/Art/Models/Props \n creating folder struct under /Game/Art/Models/Props \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(ArtPropFolderPath)											
		setDirectoryColor(ArtPropFolderPath, color)															

	# Creating the Folders under the Audio Folder

	color.set_from_hsv(h = audioColor, s = s, v = v)														# hsv color changed for folders under Audio 

	for aud in folders['Audio']:
		AudioFolderPath = '{}/Audio/{}'.format(rootPath,aud)												# Make the folder path /Game/Audio/ \n creating folder struct under /Game/Audio \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(AudioFolderPath)											
		setDirectoryColor(AudioFolderPath, color)															

	# Creating the Folders under the Blueprint Folders

	color.set_from_hsv(h = bpColor, s = s, v = v)															# hsv color changed for folders under Blueprints 

	for bps in folders['Blueprints']:
		BpFolderPath = '{}/Blueprints/{}'.format(rootPath,bps)												# Make the folder paths /Game/Blueprints/  \n creating folder struct under /Game/Blueprints/ \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(BpFolderPath)												
		setDirectoryColor(BpFolderPath, color)																

	# Creating the Folders under the Map Folder

	color.set_from_hsv(h = mapsColor, s = s, v = v)															# hsv color changed for folders under Maps

	for maps in folders['Maps']:	
		MapFolderPath = '{}/Maps/{}'.format(rootPath,maps)													# Make the folder paths /Game/Maps/ \n creating folder struct under /Game/Maps/ \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(MapFolderPath)												
		setDirectoryColor(MapFolderPath, color)																

	for Gamemaps in folders['Maps']['Game_Maps']:
		GameMapFolderPath = '{}/Maps/Game_Maps/{}'.format(rootPath,Gamemaps)								# Make the folder paths /Game/Maps/Game_Maps  \n creating folder struct under /Game/Maps/Game_Maps/ \n changing its color in ue4
		unreal.EditorAssetLibrary.make_directory(GameMapFolderPath)											
		setDirectoryColor(GameMapFolderPath, color)	


	############################ This is to update the color on the new folders added ###############################

def getNewFolderCreated():
	''' this will get the content folder directory, make a content dictionary of all the folders, and their colors'''

	ue4FolderDirectory = unreal.SystemLibrary.get_project_content_directory()								# this is to get the root of the file for the Context of the game
	ue4ContextDirectory = os.listdir(ue4FolderDirectory)													

	contentDict = {}																						# empty folder to add to a context dictionary

	for folder in ue4ContextDirectory:																		# goes through and adds keys to the content dict and makes the default value 0.0
		contentDict[folder] = 0.0

	new =  os.chdir('{}'.format(ue4FolderDirectory))														# changes the working directory to the content folder path of the UE4 file

	# this is to add values to the folders that need color changes

	contentDict['Blueprints'] = 200.0																		# light blue color
	contentDict['Art'] = 269.0																				# magenta color
	contentDict['Audio'] = 58.5
	contentDict['Maps'] = 22.0
	contentDict['Sequence'] = 116.0

	color = unreal.LinearColor(1, 1, 0, 1)																	# this is to get the color linear color variable		

	for dirs in ue4ContextDirectory:
		currentDir = "{}{}".format(ue4FolderDirectory, dirs)												# this gets the current path dict and appends the top folder (the one after the content folder)
		gameDir = '/Game/{}'.format(dirs)																	# this make the /Game/ a root and appends the top folder to it. This is so the folder can change colors later
		parentColor = contentDict[dirs]																		# this reads the contentDict and what color it is and adds it to the parent color variable. this is so it can be used later in hsv

		color.set_from_hsv(h = (parentColor), s = 1, v = 1)													# makes the rgb color a hsv color
		paintChildren(currentDir, color, gameDir)															# calls the paint children recursion function

def paintChildren(parentDirectory = '', color = None, gameDir = ''):
	''' This is to paint the newly created folders so they match their parent folder color '''
	for root, dirs, files in os.walk(parentDirectory):														# this will do a slow crawl recursive os.walk function down each of the branches 
		for dir in dirs:
			newParentDirectory = "{}/{}".format(parentDirectory, dir)										# this takes the "current directory" from the getNewFolderCreated function and appends the folders underneath it
			newGameDir = "{}/{}".format(gameDir, dir)														# This takes the "gameDir" from the getNewFolderCreated function and appends the folders underneath it
			paintChildren (newParentDirectory, color, newGameDir)											# this makes it recursively happen and doesnt kill the computer thank god
			setDirectoryColor(newGameDir,color)																# changes the folder colors so its matches the folder structure


											