def lang():
	global Retry
	global AttemptForEnter
	
	global Greet
	global MainMenu
	global InstMenu
	global EnterToQuit

	Retry = "Please Re-Enter the right choice"
	AttemptForEnter = "Press [Enter] to continue..."

	Greet = "=== MCinST remastered in Python ==="
	MainMenu = "--- Install and Update ---\
		\n1. Install Vanilla server (quick)\
		\n2. Browse unofficial servers\
		\n3. Update existing Vanilla server\
		\n--- Configuration ---\
		\n4. Guided config\
		\n5. Edit [server.properties]\
		\n6. Edit starting script\
		\n7. Extract World\
		\n--- Start and Stop ---\
		\n8. Start Default\
		\n9. Start selection\
		\n10. Stop\
		\n--- Misc ---\
		\n11. Modify MCinST\
		\n12. Uninstall selected server"
	InstMenu = "--- Welcome to MCinST the first time :3! ---\
		\nThere seems no server installed, wanna head straight to installation?\
		\n[Enter]: guided installation / [m]: Main Menu"
	EnterToQuit = "Press [Enter] to quit."
