set desktop_photo to POSIX path of (choose file with prompt "Choose a photo for your Desktop:")
tell application "System Events"
	tell every desktop
		set picture to desktop_photo
	end tell
end tell
